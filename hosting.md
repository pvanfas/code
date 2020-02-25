# DEPLOYING ON PYTHONANYWHERE
	
Assume manage.py is at https://www.pythonanywhere.com/user/username/files/home/username/project/manage.py

1. open console,clone the project to the root directory and apply the command
```
mkvirtualenv venv -p python3

pip install -r r.txt

pip install mysqlclient
```

2. Go to Dashboard

3. Create a Web app with Manual Config

4. Choose Manual Configuration

5. Enter the name of your virtualenv in the Virtualenv section on the web tab (venv)

6. Open WSGI file, Delete everything except the Django section and then uncomment that section.

7. Replace mysite with projectname

8. Create and update database settings
    
```
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

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

```
Go to the Consoles tab, start a bash console, navigate to manage.py

```
./manage.py migrate
``` 
Drop database

```
mysql -u username -h username.mysql.pythonanywhere-services.com -p 'username$project'
drop database username$project;
```

Activate venv
```
workon venv
python manage.py collectstatic
```

