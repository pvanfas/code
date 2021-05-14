```
sudo apt install gdebi git tasksel -y
```
# select lamp server
# install lamp
gedit /etc/apache2/sites-available/000-default.conf #change root
directory to /var/www/
sudo service apache2 restart
sudo mkdir -p /var/www/techpe/
chown -R pvanfas:pvanfas /var/www/techpe

# phpMyadmin
sudo apt-get update
sudo apt-get install phpmyadmin -y

# phppgadmin
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib phppgadmin
sudo su
apt install python python-dev libpq-dev python-setuptools -y
apt install postgresql postgresql-contrib phppgadmin -y
sudo apt install python-pip -y
pip install virtualenv virtualenvwrapper

#Python 3 install
sudo apt-get update
sudo apt-get install python3-distutils -y
sudo apt-get install python3.6

#Venv change
virtualenv venv -p python3
pip install django

#For getting emmet in sublime text 3
Preferences->package-settings->package-control->settings-user

#insert the following json key value
"channels": [
	"https://packagecontrol.io/channel_v3.json",
	"https://erhan.in/channel_v3.json"
]

# react-native
# 1.install npm LTS
```
sudo apt install npm
sudo npm install -g react-native-cli
```
React Native requires a recent version of the Java SE Development Kit (JDK)
```
sudo add-apt-repository ppa:linuxuprising/java
sudo apt-get updatesudo apt install oracle-java11-installer
sudo apt install oracle-java11-set-default
```
#2. Install Android Studio
```
sudo add-apt-repository ppa:maarten-fonville/android-studio
sudo apt install android-studio
sudo apt update
```
#error permission denied for /dev/kvm
```
sudo a
pt install qemu-kvm
sudo a
dduser pvanfas kvm
sudo c
hown pvanfas /dev/kvm
```
#3. Configure the ANDROID_HOME environment variable

##Add the following lines to your ​ $HOME/.bash_profile​ config file:
```
export ANDROID_HOME​ = ​ $HOME​ /Android/sdk
export PATH​ = ​ $PATH​ :$ANDROID_HOME/emulator
export PATH​ = ​ $PATH​ :$ANDROID_HOME/tools
export PATH​ = ​ $PATH​ :$ANDROID_HOME/tools/bin
export PATH​ = ​ $PATH​ :$ANDROID_HOME/platform-tools
```
```

    #source $HOME/.bash_profile
    #echo $PATH
```
#4. Create React Native application
```
react-​ native​ init ProjectName /* project name should be Camel Case */
cd ProjectName
react-native ​ run​ -android
```
# Exit error
```
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
```
