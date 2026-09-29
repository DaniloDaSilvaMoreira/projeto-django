import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-q9uc3ccpy@8&9#6kt5^kxz)+5hy#a&qxwn-tp)nt%=343l$2!s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'ProjetoAdmin.urls'

WSGI_APPLICATION = 'ProjetoAdmin.wsgi.application'
