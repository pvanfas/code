
Create `domain.com.conf` file in `/etc/apache2/sites-available`
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

        SSLEngine off

        WSGIDaemonProcess    domain python-path=/home/srv/domain/domain python-home=/home/srv/domain/venv
        WSGIProcessGroup domain
        WSGIScriptAlias / /home/srv/domain/domain/domain/wsgi.py
</VirtualHost>
```
Verify apache2 configuration and enable site
```
apachectl configtest
a2ensite domain.com.conf
systemctl reload apache2
```
This will serve the website in an insecure page (as of no installed SSL but redirected to https). 
Now run certbot to issue SSL for the conf file.
```
sudo certbot --apache -d domain.com -d www.domain.com
```
This will go through the issuing proccess and ask the following.
```
# Output
Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel):
```
Since we already defined the redirect rule, enter `1` and enter. Once the ssl is issued, change the conf file to include SSL Path
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
Reload apache to take affect the changes
```
systemctl reload apache2
```
If you dont need SSL, You can use the following virtualhost file instead
```
<VirtualHost *:80>
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

        WSGIDaemonProcess    domain python-path=/home/srv/domain/domain python-home=/home/srv/domain/venv
        WSGIProcessGroup domain
        WSGIScriptAlias / /home/srv/domain/domain/domain/wsgi.py
</VirtualHost>
```