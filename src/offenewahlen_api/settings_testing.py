import os
from offenewahlen_api.settings import *


TESTING = True
SQLALCHEMY_ECHO = True

if 'TRAVIS' in os.environ:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    if 'SECRET_KEY' in os.environ:
        SECRET_KEY = os.getenv('SECRET_KEY')
    else:
        print('SECRET_KEY is missing.')
else:
    from offenewahlen_api.settings_user import *
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'app.sqlite3')
            }
    }
