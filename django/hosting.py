# DEPLOYING ON PYTHONANYWHERE

    git clone https://github.com/pvanfas/myproject.git
    mkvirtualenv --python=/usr/bin/python3.4 venv
    pip install django==1.11.23
    pip install psycopg2
    pip install pillow
    pip install mysqlclient

    pip install -r requirements.txt #if you have a requirements.txt
    # Create a Web app with Manual Config
    # Choose Manual Configuration
    # Enter the name of your virtualenv in the Virtualenv section on the web tab (venv)
    # Enter path to code
    # Edit  WSGI file, Delete everything except the Django section and then uncomment that section.
    # Replace mysite with projectname
    # Create and update database settings
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['cre/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'cre.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pvanfas$cre',
            'USER': 'pvanfas',
            'PASSWORD': 'tesla123',
            'HOST':'pvanfas.mysql.pythonanywhere-services.com',
            'PORT': '',
        }
    }

    # Update allowed hosts
        pvanfas.pythonanywhere.com
    # Go to the Consoles tab, start a bash console, navigate to manage.py
    ./manage.py migrate
    
# Drop database
mysql -u pvanfas -h pvanfas.mysql.pythonanywhere-services.com -p 'pvanfas$crm'
drop database pvanfas$crm;

# Activate venv
workon venv
python manage.py collectstatic

# Add to settings file if got error as
# You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
