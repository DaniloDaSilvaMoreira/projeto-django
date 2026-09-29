import os
from pathlib import Path

# CORREÇÃO: Define o BASE_DIR subindo 3 níveis para encontrar a raiz real do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}