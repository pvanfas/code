# DigitalOcean Server Setup

DigitalOcean, Inc. is an American cloud infrastructure provider headquartered in New York City with data centers worldwide. DigitalOcean provides developers cloud services that help to deploy and scale applications that run simultaneously on multiple computers.

## Server Setup

### Update system

    sudo apt-get update
    sudo apt-get upgrade

### Install python

    sudo apt-get install python3-distutils -y
    sudo apt-get install python3

### Install essential python libraries

[`Reference`](https://gist.github.com/pvanfas/6da287111dee1b08d325b33c984505a6#development-system-setup)

### Add ServerName and Allow WSGI Authorization

    nano /etc/httpd/conf/httpd.conf or
    nano /etc/apache2/apache2.conf

Add the following line to the end of the file:

    ServerName 127.0.0.1
    WSGIPassAuthorization On
