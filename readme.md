## Jupyter hub with github auth and docker spawner

1. Fill env variables inside run.sh.sample and rename it to run.sh
2. Create docker network with the same name you have given in sh file (NETWORK_NAME)

```
docker network create <NETWORK_NAME>
```

3. Run by attaching the network

```
docker run --name lab -d --net <NETWORK_NAME> -p 80:80 -v /home/ubuntu/hub_data:/home -v /var/run/docker.sock:/var/run/docker.sock jupyter-lab:alpha
```
