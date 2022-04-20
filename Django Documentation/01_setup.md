### Development System Setup

##### Update system

    sudo apt-get update
    sudo apt-get upgrade

##### Install python

    sudo apt-get install python3-distutils -y
    sudo apt-get install python3

##### Install essential python libraries

    sudo apt-get update
    sudo apt-get install build-essential python-dev python-setuptools -y
    sudo apt-get install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib -y
    sudo apt-get install libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev 
    sudo apt-get install libssl-dev openssl libffi-dev -y
    sudo apt install libreadline-dev libdb4o-cil-dev libpcap-dev phppgadmin -y
    sudo apt-get install python-pip python-smbus libtk8.5 -y

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3 get-pip.py
    sudo pip3 install virtualenv
    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install virtualenv

    sudo apt-get install apache2 python3-certbot-apache postgresql postgresql-contrib python3-pip apache2 libapache2-mod-wsgi-py3 -y
    sudo a2enmod rewrite
    sudo a2enmod wsgi
    sudo a2enmod ssl
    sudo apt-get update

    pip install django pillow django-registration-redux psycopg2-binary django-versatileimagefield django-crispy-forms

GDAL is an excellent open source geospatial library that has support for reading most vector and raster spatial data formats. Currently, GeoDjango only supports GDAL’s vector data capabilities [2]. GEOS and PROJ should be installed prior to building GDAL.

    sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable

    sudo apt-get install gdal-bin
    sudo apt-get install python3-gdal
    
wkhtmltopdf and wkhtmltoimage are open source (LGPLv3) command line tools to render HTML into PDF and various image formats using the Qt WebKit rendering engine

    sudo apt-get install wkhtmltopdf wkhtmltoimage

##### Install a text editor

###### Atom

    sudo add-apt-repository ppa:webupd8team/atom
    sudo apt-get update
    sudo apt-get install atom -y

###### VS Code

    sudo apt update
    sudo apt install software-properties-common apt-transport-https wget
    wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
    sudo apt update
    sudo apt install code -y

###### Sublime text

    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    sudo apt-get update
    sudo apt-get install sublime-text -y

##### Install git & configure

    sudo apt install git -y

    git config --global user.name "Name"
    git config --global user.email "example@gmail.com"

##### Install chrome

    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo dpkg -i google-chrome-stable_current_amd64.deb
