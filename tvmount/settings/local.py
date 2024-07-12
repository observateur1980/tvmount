from .base import*
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT ='/static/'

