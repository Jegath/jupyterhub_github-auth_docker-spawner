# FROM jupyterhub/jupyterhub
FROM ubuntu:20.04

RUN apt-get update && apt-get -y update
RUN apt-get install -y build-essential python3.6 python3-pip python3-dev
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt -y install nodejs
RUN npm install -g configurable-http-proxy
RUN pip3 -q install pip --upgrade
RUN python3 -m pip install jupyterhub

RUN pip install notebook
RUN pip install netifaces

RUN pip install nbgrader

RUN pip install oauthenticator

RUN pip install dockerspawner


# RUN jupyter nbextension install --sys-prefix --py nbgrader --overwrite
# RUN jupyter nbextension enable --sys-prefix --py nbgrader
# RUN jupyter serverextension enable --sys-prefix --py nbgrader



EXPOSE 80

ADD ./jupyterhub_config.py .

COPY run.sh .

ENTRYPOINT ["/bin/bash", "run.sh"]