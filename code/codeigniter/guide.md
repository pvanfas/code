1. Install composer & Update php & xampp
```
sudo apt install wget php-cli php-zip unzip
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
HASH="$(wget -q -O - https://composer.github.io/installer.sig)"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
composer
```
```
sudo apt-add-repository ppa:ondrej/php
sudo apt-get install 7.3
sudo apt install php7.3-xdebug php7.3-curl php7.3-gd php7.3-xml php7.3-xmlrpc php7.3-mysql php7.3-mbstring php7.3-soap php 7.3-intl


```
```
sudo apt-get install mysql-server
mysql_secure_installation
systemctl status mysql.service
mysqladmin -p -u root version
sudo service mysql stop
run sudo /opt/lampp/xampp start
```
```
wget https://www.apachefriends.org/xampp-files/5.6.20/xampp-linux-x64-5.6.20-0-installer.run
sudo chmod +x xampp-linux-x64-5.6.20-0-installer.run
sudo ./xampp-linux-x64-5.6.20-0-installer.run
sudo /opt/lampp/xampp start
```

2. Initiate codeigniter
```
composer create-project CodeIgniter/framework project-name

composer create-project codeigniter4/appstarter project-name
```
3. Inital Setup
```
cd project-name
rm -rf readme.rst  user_guide contributing.md  license.txt

```

Set Base URL (application/config/config.php)

```
$config['base_url'] = 'http://localhost:3000';
```
Setup Database Credential
```
$db['default'] = array(
    'dsn'   => '',
    'hostname' => 'localhost',
    'username' => 'root',
    'password' => 'root',
    'database' => 'project',
    'dbdriver' => 'mysqli',
    'dbprefix' => '',
    'pconnect' => FALSE,
    'db_debug' => (ENVIRONMENT !== 'production'),
    'cache_on' => FALSE,
    'cachedir' => '',
    'char_set' => 'utf8',
    'dbcollat' => 'utf8_general_ci',
    'swap_pre' => '',
    'encrypt' => FALSE,
    'compress' => FALSE,
    'stricton' => FALSE,
    'failover' => array(),
    'save_queries' => TRUE
);

```
Run project
```
php -S localhost:3000
```

Remove index.php Using .htaccess
```
//  Find the below code
    $config['index_page'] = "index.php"
//  Remove index.php
    $config['index_page'] = ""
```
Create .htaccess File

```
 RewriteEngine on
 RewriteCond $1 !^(index.php|resources|robots.txt)
 RewriteCond %{REQUEST_FILENAME} !-f
 RewriteCond %{REQUEST_FILENAME} !-d
 RewriteRule ^(.*)$ index.php/$1 [L,QSA]
```
