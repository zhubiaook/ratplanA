from .common import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['blog.zybz.fun', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'blog.db.backends.mysql',
        'HOST': os.environ['DJANGO_DB_HOST'],
        'NAME': os.environ['DJANGO_DB_NAME'],
        'USER': os.environ['DJANGO_DB_USER'],
        'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
    }
}