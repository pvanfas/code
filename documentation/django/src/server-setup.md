# DEVELOPMENT SYSTEM SETUP

## Update system
```
sudo apt-get update
sudo apt-get upgrade
```
## Install python
```
sudo apt-get install python3-distutils -y
sudo apt-get install python3
```
## Install essential python libraries
```
sudo su
apt-get update
apt-get install build-essential python-dev python-setuptools -y
apt-get install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib -y
apt-get install libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev -y
apt install libreadline-dev libdb4o-cil-dev libpcap-dev phppgadmin -y
apt-get install python-pip python-smbus libtk8.5 -y

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install virtualenv
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
sudo apt-get update
sudo apt-get install python3-certbot-apache
sudo apt-get install libapache2-mod-wsgi-py3
sudo a2enmod rewrite
sudo a2enmod ssl
sudo apt install postgresql postgresql-contrib
pip install django pillow django-registration-redux psycopg2-binary django-versatileimagefield django-crispy-forms
```
### Add ServerName
```
sudo nano /etc/httpd/conf/httpd.conf
```
Add the ServerName 127.0.0.1 line to the end of the file:
```
ServerName 127.0.0.1
```
