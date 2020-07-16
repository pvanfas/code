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
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip3 install virtualenv
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
sudo apt-get update

sudo su
apt-get update
apt-get install build-essential python-dev python-setuptools python-pip python-smbus
apt-get install python3-pip python3-dev python3-venv libpq-dev postgresql postgresql-contrib
apt-get install libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev
apt install libreadline-dev libtk8.5 libdb4o-cil-dev libpcap-dev phppgadmin

```
## Install a text editor
### Atom
```
sudo add-apt-repository ppa:webupd8team/atom
sudo apt-get update
sudo apt-get install atom
```

### VS Code
```
sudo apt update
sudo apt install software-properties-common apt-transport-https wget
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code
```
### Sublime text
```
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```
## Install git & configure
```
sudo apt install git -y
```
```
git config --global user.name "Name"
git config --global user.email "example@gmail.com"
```

## Install chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
