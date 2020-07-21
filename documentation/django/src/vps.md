```
a2dissite domain.com.conf
systemctl reload apache2
```
```
a2ensite domain.com.conf
systemctl reload apache2
```
```
<VirtualHost *:80>
        ServerName domain.com
        ServerAlias www.domain.com
        Redirect permanent / https://domain.com/

        RewriteEngine on
        RewriteCond %{SERVER_NAME} =domain.com [OR]
        RewriteCond %{SERVER_NAME} =www.domain.com
        RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<VirtualHost *:443>
        ServerAdmin admin@domain.com
        ServerName domain.com
        ServerAlias www.domain.com
        
        DocumentRoot /home/srv/domain
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        Alias /static /home/srv/domain/domain/static
        <Directory /home/srv/domain/domain/static>
                Require all granted
        </Directory>

        Alias /media /home/srv/domain/domain/media
        <Directory /home/srv/domain/domain/media>
                Require all granted
        </Directory>

        <Directory /home/srv/domain/domain/domain>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        SSLEngine on
        SSLCertificateFile    /etc/letsencrypt/live/domain.com/cert.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/domain.com/privkey.pem
        SSLCertificateChainFile /etc/letsencrypt/live/domain.com/fullchain.pem

        WSGIDaemonProcess    domain python-path=/home/srv/domain/domain python-home=/home/srv/domain/venv
        WSGIProcessGroup domain
        WSGIScriptAlias / /home/srv/domain/domain/domain/wsgi.py
</VirtualHost>
```
```
sudo certbot --apache -d domain.com -d www.domain.com
```
