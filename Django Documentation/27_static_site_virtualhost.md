Create `domain.com.conf` file in `/etc/apache2/sites-available`

Verify apache2 configuration and enable site

    apachectl configtest
    a2ensite domain.com.conf
    systemctl reload apache2

To install SSL,run certbot to issue SSL for the conf file.

    sudo certbot --apache -d domain.com -d www.domain.com

This will go through the issuing proccess and ask the following.

    # Output
    Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    1: No redirect - Make no further changes to the webserver configuration.
    2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
    new sites, or if you're confident your site works on HTTPS. You can undo this
    change by editing your web server's configuration.
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    Select the appropriate number [1-2] then [enter] (press 'c' to cancel):

Reload apache to take affect the changes

    systemctl reload apache2
