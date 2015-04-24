import sae
from djangoTest import wsgi

application = sae.create_wsgi_app(wsgi.application)
