from .common import *


SECRET_KEY = '10%xnn(^awgkp^s)*j7$4u7secp*c*=rnt6kn-_0u^u9ad0^vf'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '192.168.0.51',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': '1234',
    }
}