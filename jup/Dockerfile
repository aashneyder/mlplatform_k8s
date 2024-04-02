FROM jupyterhub/jupyterhub:4

WORKDIR /srv/jupyterhub

RUN pip install jupyterhub-dummyauthenticator jupyter_core jupyter_server && useradd -ms /bin/bash test
COPY ./jupyterhub_config.py .

CMD ["jupyterhub", "-f", "jupyterhub_config.py"]

