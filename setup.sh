#!/bin/bash

# setup virtual env
echo 'Setting up virtual environment (env)'
virtualenv --no-site-packages env
echo 'Activating virtual environment'
source env/bin/activate

# install dependencies
pip install --use-mirrors --download-cache ~/.pip-cache/ -r requirements.txt
