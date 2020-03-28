DEVELOPMENT SYSTEM SETUP

Install pip for our Python 3 version and virtualenv:

```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install virtualenv
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
sudo apt-get update

sudo su
apt-get update && apt-get upgrade
apt-get dist-upgrade
apt-get install build-essential python-dev python-setuptools python-pip python-smbus python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev

```

DJANGO SETUP

```
virtualenv venv -p python3
source venv/bin/activate

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```
DJANGO COMMANDS

```
python manage.py loaddata initial_data notification permissions user_groups
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
GIT USER CONFIG

```
git config --global user.name "Anfas PV"
git config --global user.email "pvanfas.talrop@gmail.com"
```

Install atom text editor
```
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
```

Install vscode
```
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code
```
Install chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
