# Setting up virtual environment (python 3)

virtualenv venv -p python3 && source venv/bin/activate
pip install django psycopg2-binary python-decouple
django-admin startproject project
cd project && mkdir static media templates

# Migrate changes to the database

python manage.py makemigrations && python manage.py migrate
python manage.py runserver

# Starting a new app

python manage.py startapp web
