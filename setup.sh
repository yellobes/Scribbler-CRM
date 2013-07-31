#!/bin/bash


# Local settings location
local_settings="assets/assets/local_settings.py"

# Django secret key
secret_key="$(python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])')"
# This files location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# setup virtual env
echo 'Setting up virtual environment (env)'
virtualenv --no-site-packages env
echo 'Activating virtual environment'
source env/bin/activate

# Install requirements
pip install --use-mirrors --download-cache ~/.pip-cache/ -r requirements.txt

if [ ! -f  $local_settings ]; then
  echo "

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '$DIR/scribbler.db',
    }
}

SECRET_KEY = '$secret_key'

STATIC_ROOT = '$DIR/static/'
MEDIA_ROOT = '$DIR/media/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


GRAPPELLI_ADMIN_TITLE = 'Scribbler CRM'
" > $local_settings
fi
