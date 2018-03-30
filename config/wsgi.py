import os
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
ROOT_DIR = environ.Path(__file__) - 2
env = environ.Env()
environ.Env.read_env(ROOT_DIR.file('.env'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env('DJANGO_ENVIRONMENT'))

application = get_wsgi_application()
