# jupyterhub_config.py file
import netifaces
from jupyter_client.localinterfaces import public_ips
import os
c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.DockerSpawner.image = "jupyter/scipy-notebook"
c.Spawner.debug = True
# Specify a timeout for starting the image
c.DockerSpawner.start_timeout = 600

# the Hub's API listens on localhost by default,
# but docker containers can't see that.
# Tell the Hub to listen on its docker network:
docker0 = netifaces.ifaddresses('eth0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]

c.JupyterHub.hub_ip = '0.0.0.0'  # docker0_ipv4['addr']
c.JupyterHub.hub_connect_ip = docker0_ipv4['addr']

network_name = os.environ['NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = {'network_mode': network_name}

# Allows multiple single-server per user
c.JupyterHub.allow_named_servers = False

# https on :443
c.JupyterHub.port = 80

# use GitHub OAuthenticator for local users
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True

# specify users and admin
# c.Authenticator.allowed_users = {'rgbkrk', 'minrk', 'jhamrick'}
c.Authenticator.admin_users = {'jegath'}
