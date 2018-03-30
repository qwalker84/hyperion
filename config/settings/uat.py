from .base import *

SECRET_KEY = env('SECRET_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
