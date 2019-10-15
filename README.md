DEVELOPMENT SYSTEM SETUP

If you are using Ubuntu 16.04 or an older version, first add the following repository:

```sudo add-apt-repository ppa:deadsnakes/ppa```

Executes the following commands to install the latest Python 3 distribution:

```
sudo apt-get update

sudo apt-get install python3.6
```
Install pip for our Python 3.6.2 version and virtualenv:

```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
sudo pip3.6 install virtualenv

sudo apt-get update
sudo apt-get install aptana
sudo apt-get install python-pip python-dev python3-pip python3-dev python3-venv
sudo apt-get install libpq-dev postgresql postgresql-contrib nginx
sudo apt-get install code
sudo pip3 install virtualenv

sudo apt-get update
Postgres=# CREATE DATABASE project;
Postgres=# CREATE USER user WITH PASSWORD 'password';
Postgres=# ALTER ROLE user SET client_encoding TO 'utf8';
Postgres=# ALTER ROLE user SET default_transaction_isolation TO 'read committed';
Postgres=# ALTER ROLE user SET timezone TO 'UTC';
Postgres=# GRANT ALL PRIVILEGES ON DATABASE project TO user;
Postgres=# \q
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
```

DJANGO SETUP

```
virtualenv venv
source venv/bin/activate
mkdir src
cd src
pip install django==1.11.23
pip install pillow psycopg2
pip freeze
django-admin.py startproject project
cd project
mkdir static media templates
python manage.py runserver
```
DJANGO COMMANDS
```
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py loaddata initial_data notification permissions user_groups
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
GIT USER CONFIG

```git config --global user.name "Anfas PV"
git config --global user.email "pvanfas.talrop@gmail.com"
```

