c = get_config()
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '0.0.0.0'
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
