from .common import *


SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['blog.zybz.fun', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'x.x.x.x',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'xxxx',
    }
}