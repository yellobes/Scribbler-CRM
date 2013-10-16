import os

THISPATH = os.path.dirname(os.path.realpath(__file__))
APP_ROOT = os.path.join(THISPATH, '..')
PROJECT_ROOT = os.path.join(APP_ROOT, '..')

ALLOWED_HOSTS = [
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '%s/fsd.db' % PROJECT_ROOT,      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


"""
Two things are wrong with Django's default `SECRET_KEY` system:

1. It is not random but pseudo-random
2. It saves and displays the SECRET_KEY in `settings.py`

This snippet
1. uses `SystemRandom()` instead to generate a random key
2. saves a local `secret.txt`

The result is a random and safely hidden `SECRET_KEY`.
"""
try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(APP_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random
            SECRET_KEY = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

