# DEPLOYING ON PYTHONANYWHERE
	
Assume manage.py is at https://www.pythonanywhere.com/user/username/files/home/username/project/manage.py

clone the project to the root directory

mkvirtualenv venv -p python3

pip install -r r.txt

pip install mysqlclient

Go to Dashboard

Create a Web app with Manual Config

Choose Manual Configuration

Enter the name of your virtualenv in the Virtualenv section on the web tab (venv)

Open WSGI file, Delete everything except the Django section and then uncomment that section.

Replace mysite with projectname

Create and update database settings
    

	DEBUG = True

	ALLOWED_HOSTS = ['username.pythonanywhere.com']

	TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['project/templates'],
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

    WSGI_APPLICATION = 'project.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'username$project',
            'USER': 'username',
            'PASSWORD': 'db-password',
            'HOST':'username.mysql.pythonanywhere-services.com',
            'PORT': '',
        }
    }

Go to the Consoles tab, start a bash console, navigate to manage.py

```
   ./manage.py migrate
``` 
Drop database

```
mysql -u username -h username.mysql.pythonanywhere-services.com -p 'username$crm'
drop database username$crm;
```

Activate venv
```
workon venv
python manage.py collectstatic
```

Add to settings file if got error as
You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path
```
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

```
