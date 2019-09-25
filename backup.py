# DEVELOPMENT COMPUTER SETUP -------------------------------------
sudo apt-get update
sudo apt-get install aptana
sudo apt-get install python-pip python-dev python3-pip python3-dev python3-venv
sudo apt-get install libpq-dev postgresql postgresql-contrib nginx
sudo apt-get install code
sudo pip3 install virtualenv

sudo apt-get update
Postgres=# CREATE DATABASE project;
Postgres=# CREATE USER user WITH PASSWORD 'password';
Postgres=# ALTER ROLE user SET client_encoding TO 'utf8';
Postgres=# ALTER ROLE user SET default_transaction_isolation TO 'read committed';
Postgres=# ALTER ROLE user SET timezone TO 'UTC';
Postgres=# GRANT ALL PRIVILEGES ON DATABASE project TO user;
Postgres=# \q
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

#DJANGO SETUP ----------------------------------------------------

mkdir dev
cd dev
mkdir django
cd django
mkdir femme
cd femme
mkdir src
virtualenv venv
source venv/bin/activate
which python
cd src
pip install django==1.11.23
pip install pillow psycopg2
pip freeze
django-admin.py startproject femme
cd femme
mkdir static media templates
python manage.py runserver

##Define template directory in femme/settings.py
### One
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

### Two

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/talrop/django/femme/src/femme/media/'
STATIC_URL = '/static/'
STATIC_FILE_ROOT = '/home/talrop/django/femme/src/femme/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/talrop/django/femme/src/femme/static/',
)

###second tab

source ../../venv/bin/activate 
python manage.py startapp web

#register web app in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'web'
]

#add following url to the array in src/femme/femme/urls.py

from django.conf.urls import url ,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('web.urls',namespace="web"))
]

#create new file in src/femme/web/urls.py and paste following code

from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
]
  
#edit src/femme/web/views.py

from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect


def index(request):
	return HttpResponse("Hello World")


# URL REDIRECT --------------------------------------------------------

# edit views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponseRedirect(reverse())

# femme/urls.py
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^about/$', views.about,name="about"),

]

# web/urls.py
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^about/$', views.about,name="about"),

]

#views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponseRedirect(reverse('web:about'))


def about(request):
    return HttpResponse('Hello from about')

# TEMPLATE RENDERING ----------------------------------------------------

# Remove redirect, Add assets into /static and html into /templates/web

	Add {% load static %} after <head> and Change directory path to href="{% static 'location' %}"
	example <script type="text/javascript" src="{% static 'js/script.js' %}"></script>

# edit views

from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	return render(request,'web/index.html')


# CONFIGURE DATABASE -------------------------------------------------

sudo su postgres
createdb femme
createuser techpe -P
psql
grant all privileges on database femme to techpe;
\q
exit

#change database in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'femme',
        'USER': 'techpe', 
        'PASSWORD': 'techpe123',
        'HOST':'localhost',
        'PORT': '',
    }
}

# DJANGO MODELS ------------------------------------------------------

# Import "_" and Add class in web/migrations/models.py

from django.utils.translation import ugettext_lazy as _
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    education = models.CharField(max_length=128)
    dob = models.TextField()
    message = models.TextField()

    class Meta:
        db_table = 'web_registration'
        verbose_name = ('registration')
        verbose_name_plural = ('registrations')

    def __unicode__(self):
        return self.name

# Import model and define list display in admin.py

from __future__ import unicode_literals
from django.contrib import admin
from web.models import Registration


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','dob','education','message')

admin.site.register(Registration,RegistrationAdmin)

# Open shell and another terminal tab, Activate venv, migrate changes
python manage.py makemigrations
python manage.py migrate

# We can change admin url at ^admin/ femme/urls.py
# Add superuser
python manage.py createsuperuser
# A new section will be displayed in administrator window
# Section name can be edited at verbose_name_plural = ('new name') in web/models.py


# Add a new model in models.py

class About(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to="web/about/")

    class Meta:
        db_table = 'web_about'
        verbose_name = "about"
        verbose_name_plural = "about"

    def __unicode__(self):
        return self.title


# migrate changes into app and database (femme/src/femme)
python manage.py makemigrations
python manage.py migrate

# Import About and Register in admin.py

from web.models import Registration, About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','content','image')

admin.site.register(About,AboutAdmin)

# To open images import serve, settings and define url in urls.py

from django.views.static import serve
from django.conf import settings

    # include in urlpatterns
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),

## DATA RENDERING -----------------------------------------------------

# Assign title and caption for html (edit in views.py)

def index(request):
    context = {
        "title" : "Femme",
        "caption" : "Femme caption",
    }
    return render(request, 'web/index.html',context)
# Rewrite as needed
	<title>{{title}} | {{caption}}</title>
	
## DYNAMIC CONTENT RENDERING ------------------------------------------

from web.models import About

def index(request):
    about_datas = About.objects.all()
    context = {
        "title" : "Femme",
        "caption" : "Femme Caption",
        "about_datas" : about_datas
    }
    return render(request, 'web/index.html',context)

            # Note: Possible extensions
            all()
            filter(id=1)
            filter(name="x")
            filter(name__icontains="x")
            exclude(name="x")
            get()
            # note end here

# Add to html file

<ul>
    {% for about in about_datas %}
        {{about.image.url}}
        {{about.title}}
        {{about.content}}
    {% endfor %}
    <li></li>
</ul>

# with if condition

{% if about_datas %}
    <p>content here</p>
{% else %}
    <p>Nothing Found</p>
{% endif %}

# Current year update
{% now 'Y' %}

# CREATING PAGE -------------------------------------------------------

# Define a new views.py entry
def about(request):
    context = {
        "title" : "Femme", 
        "caption" : "Femme Caption",
    }
    return render(request, 'web/about.html',context)
# Specify in url patterns (web/views.py)
url(r'^about$', views.about,name="about"),

# Create a new page about.html and load http://localhost:8000/about


# CONTEXT PROCESSORS -------------------------------------------------

# Create a new file web/context_processors.py
def main_context(request):

    return {
        "caption" : "Femme Caption"
    }
# Add to settings.py (TEMPLATES/OPTIONS)

'web.context_processors.main_context',

Replace <title>caption</title> with <title>{{caption}}</title>

==================================================================================================================
# FORM SUBMISSIONS -------------------------------------------------

# Define a new url in web
    url(r'^registration$', views.registration,name="registration"),

# add name to input fields, update action and method
<form action="{% url 'web:registration' %}" method="post">
{% csrf_token %}

#Import Registration in view
from web.models import About, Registration
# Define a new view
def registration(request):
    if request.method:
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        education = request.POST.get('education')
        message = request.POST.get('message')
        
        Registration.objects.create(
            name = name,
            email = email,
            phone = phone,
            dob = dob,
            education = education,
            message = message
        )

        return HttpResponse("Form Submitted")
    else:
        return HttpResponse("Invalid Request")

# ..............................................................
# DJANGO FORM SUBMISSION

# Create a file web/forms.py 
from django import forms
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _
from web.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

# Import RegistrationForm to views.py
from web.forms import RegistrationForm
# Pass form variable and update context in views.py
def index(request):
    about_datas = About.objects.all()
    form = RegistrationForm()
    context = {
        "title" : "Home",
        "caption" : "Femme Caption",
        "about_datas" : about_datas
        "form" : form
    }
    return render(request, 'web/index.html',context)

# Replace input tag in html
        <p class="first">
            <label for="{{form.name.id_for_label}}">{{form.name.label}}</label>
            {{form.name}}
        </p>

    # Alternative 1
            {% for field in form %}
                <p class="first">
                    <label for="{{field.id_for_label}}">{{field.label}}</label>
                    {{field}}
                </p>
            {% endfor %}

    # Alternative 2
            {{form.as_p}}

# Adding classes and placeholder, Updating error messages and labels in forms.py
from django import forms
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import ugettext_lazy as _
from web.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'email': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Email'}),
            'phone': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Phone'}),
            'education': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Education'}),
            'message': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Message'}),
            'dob': TextInput(attrs={'class': 'required form-control', 'placeholder': 'DOB'} blank=True,null=True),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'email': {
                'required': _("Email field is required."),
            },
            'phone': {
                'required': _("Phone field is required."),
            },
            'education': {
                'required': _("Education field is required."),
            },
            'dob': {
                'required': _("DOB field is required."),
            },
            'message': {
                'required': _("Message field is required."),
            },
        }
        labels = {
            'name' : "What we should call you ?",
            'phone' : "And your phone number ?",
            'message' : "What is in your mind ?",
        }

# Registration can be redefined simply when using django forms
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print form.errors
            return HttpResponse("Validation Error")

        return HttpResponse("Form Submitted")
    else:
        return HttpResponse("Invalid Request")

# Customising Error messages
    # Create a new file web/functions.py

    def generate_form_errors(args,formset=False):
        message = ''
        if not formset:
            for field in args:
                if field.errors:
                    message += field.errors
            for err in args.non_field_errors():
                message += str(err)

        elif formset:
            for form in args:
                for field in form:
                    if field.errors:
                        message +=field.errors
                for err in form.non_field_errors():
                    message += str(err)
        return message

    # Import in views
    from web.functions import generate_form_errors

    # Update registration function
    def registration(request):
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print form.errors
                errors = generate_form_errors(form,formset=False)
                return HttpResponse(errors)

            return HttpResponse("Form Submitted")
        else:
            return HttpResponse("Invalid Request")

# AJAX Form submission
    # Upadate script.js with ajax function
    # add ajax,reload class to form tag

    # add show_loader(),remove_popup() functions to script.js
        function show_loader(){
            $('.popup-bg').show();
            $('.popup-box').remove();
            $('body').append('<div class="popup-box"><div class="preloader pl-xxl"><svg viewBox="25 25 50 50" class="pl-circular"><circle r="20" cy="50" cx="50" class="plc-path"/></svg></div></div><span class="popup-bg"></span>');
        }
        
        function remove_popup(){
            $('.popup-box,.popup-bg').remove();
        }
    # Update registration model in views.py

        def registration(request):
            if request.method == "POST":
                form = RegistrationForm(request.POST)
                if form.is_valid():
                    form.save()
                    
                    response_data = {

                        "status" : "true",
                        "title" : "Successfully Submitted",
                        "message" : "Registration successfully updated"
                    }
                else:
                    message = generate_form_errors(form,formset=False)

                    response_data = {
                        "status" : "false",
                        "stable" : "true",
                        "title" : "Form validation error",
                        "message" : message
                    }

                return HttpResponse(json.dumps(response_data), content_type='application/javascript')
            else:
                return HttpResponse("Invalid Request")

    # Import json in views.py
         import json

    # Add sweatalert.css and sweatalert.min.js to static folder
    # Link in html head tag
    # Add loader form styles of popup in style.css
    
# Removing Required fields

    # Add  (blank=True, null=True) to models.py
    # Remove required class and associated error messages from forms.py
    # Migrate changes

# Template extending
    # create about page
    # Define in urlpatterns
    url(r'^about/$', views.about,name="about"),

    # Define in views
    def about(request):
    about_datas = About.objects.all()
    context = {
        "title" : "About",
        "caption" : "Femme Caption",
        "about_datas" : about_datas,
    }
    return render(request, 'web/about.html',context)

    # update link in index 
    {% url 'web:about' %}


# Template extension - general

    # create base.html
        {% block content %}
        {% endblock%}

    # index.html
        {% extends 'web/base.html' %}
        {% load static %}
        {% block content %}
        -------- content here --------
        {% endblock%}

    # Update about page
    # Fix hyperlinks
        href="{% url 'web:index' %}
        href="{% url 'web:about' %}
        href="{% url 'web:index' %}#features

    # Fixing spotlight content
        add additional lines to views/index and views/about
        "is_home" : True
        "is_about" : True
    # create a new dir web/includes
    # Create two files index-spotlight.html and about-spotlight.html
    # Move the content from base to respective file and edit as needed
    # Paste the condition in spotlight position in base.html
        {% if is_home %}
            {% include 'web/includes/index-spotlight.html' %}
        {% elif is_about %}
            {% include 'web/includes/about-spotlight.html' %}
        {% endif %}

# Updating additionsl requiremets

    # Define fields in models.py
    subheading = models.CharField(max_length=128)
    date_added = models.DateField()
    # Make migrations and migrate
    # Update html with required tags

# Dropping database
    find . -path "*/migrations/*.pyc"  -delete
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    # Drop the current database
    # Create the initial migrations and generate the database schema:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser


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


    ---------------------------- finished ----------------------------
