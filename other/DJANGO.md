1. Setting up virtual environment (python 3)
```
virtualenv venv -p python3
source venv/bin/activate
pip install django psycopg2-binary django-registration-redux python-decouple
django-admin.py startproject project
cd project && mkdir static media templates
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
```
2. Starting a new app
```
python manage.py startapp web
```
3. Register in INSTALLED APPS
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

	'web',
]
```

4. Define template directory in TEMPLATES
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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
```

5. Define DATABASES
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbname',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT': '',
    }
}
```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
6. Set settings.py file
```
import os
from decouple import config, Csv


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['localhost','127.0.0.1']
```
```
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL= config('DEFAULT_FROM_EMAIL')
DEFAULT_BCC_EMAIL= config('DEFAULT_BCC_EMAIL')
DEFAULT_REPLY_TO_EMAIL = config('DEFAULT_REPLY_TO_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')
ADMIN_EMAIL = config('ADMIN_EMAIL')

```
```
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMIN_MEDIA_PREFIX = '/static/admin'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_URL = '/static/'
STATIC_FILE_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

```
```

SECRET_KEY = &w-7okw38wks+(3=64#36&tde+kl0tv3qa^)6f9#+t6e#+*p(b

DEBUG = True

# database credentials
ENGINE = django.db.backends.postgresql_psycopg2
DB_NAME = database
DB_USER = database_dbuser
DB_PASSWORD = ZQ5FUDUYTE3XC
DB_HOST = localhost

EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
EMAIL_PORT = 587
EMAIL_HOST = smtp-relay.sendinblue.com
EMAIL_HOST_USER = mail@gmail.com
EMAIL_HOST_PASSWORD = password

DEFAULT_FROM_EMAIL = mail@gmail.coms
DEFAULT_BCC_EMAIL = mail@gmail.coms
DEFAULT_REPLY_TO_EMAIL = mail@gmail.coms
SERVER_EMAIL = mail@gmail.coms
ADMIN_EMAIL = mail@gmail.coms
```
7. Define urlpatterns in project/urls.py

```
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('web.urls',namespace='web'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_FILE_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
8. Create web/urls.py and paste the following
```
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
]
```
9. Edit web/views.py
```
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json


def index(request):
    context = {
        "title" : "HOME",
        "caption" : "The ultimate solution provider",
        "is_home" : True
    }
    return render(request, 'web/index.html',context)
```
```
//With save
def function(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Registration successfully updated"
            }
        else:
            print (form.errors)
            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = NewsletterForm()
        context = {
            "form" : form,
        }
        return render(request, 'web/index.html',context)

```
```
//with file submission
def function(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Registration successfully updated"
            }
        else:
            message = generate_form_errors(form)

            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = NewsletterForm()
        context = {
            "title" : "Updates",
            "form" : form,
        }
        return render(request, 'web/index.html',context)
```
10. Template extending

base.html
```
    -------- header here --------
    {% block content %}
    {% endblock%}
    ------- footer here --------
```
index.html
```
    {% extends 'web/base.html' %}
    {% load static %}

    {% block content %}
    -------- content here --------
    {% endblock%}
```
11. Static file rendering
```
    (i). Add assets into /static and html into /templates/web
    (ii). Add {% load static %} after <head> tag and Change directory path to href="{% static 'location' %}"
    (iii). example:
        <script src="{% static 'js/script.js' %}"></script>
```

12. GIT-IGNORE

```
### Django ###
*.log
*.pot
*.pyc
migrations/*.py
__pycache__/
!__init__.py
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

```
13. Setup database
```
sudo su postgres
createdb project
createuser user -P
psql
grant all privileges on database db to user;
\q
exit
```
14. Django models
```
from django.utils.translation import ugettext_lazy as _
from django.db import models


CATEGORY_CHOICES = (
    ('personal', 'Personal'),
    ('business', 'Business'),
)

class Blog(models.Model):
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    name = models.CharField(max_length=128)
    customer = models.ForeignKey('customers.Customer',limit_choices_to={'is_deleted': False},on_delete=models.CASCADE)
    email = models.EmailField(blank=True,null=True)
    image = models.ImageField(upload_to='images/blog')
    content = models.TextField()
    time = models.DateTimeField()
    video_url = models.URLField()
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES,default="personal")
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'web_blog'
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')

    def __str__(self):
        return str(self.pk)

```
15. Django forms
```
from django import forms
from django.utils.translation import ugettext_lazy as _
from web.models import Registration
from django.forms.widgets import TextInput, Textarea, EmailInput, CheckboxInput, Select, NumberInput, RadioSelect, FileInput, NumberInput


class CategoryForm(forms.ModelForm):
    category = forms.ChoiceField(widget=forms.RadioSelect(),choices=CATEGORY_CHOICES)
    class Meta:
        model = Category
        exclude = ['creator']
        widgets = {}

```
```
from django.forms.widgets import TextInput, Textarea, EmailInput, CheckboxInput, Select, NumberInput, RadioSelect, FileInput, NumberInput


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Name'}),
            'message': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Message'}),
            'banner_image': FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'country' : Select(attrs={'class': 'form-control',}),
            'whatsapp_number' : NumberInput(attrs={'class': 'form-control', 'placeholder': 'Whatsapp Number'}),
            'active' : CheckboxInput(attrs={}),
        }
        error_messages = {
            'name': {
                'required': _("Name field is required."),
            },
            'message': {
                'required': _("Message field is required."),
            },
        }
        labels = {
            'name' : "What we should call you ?",
            'message' : "What is in your mind ?",
        }
```
16. Import model and define list display in admin.py
```
from __future__ import unicode_literals
from django.contrib import admin
from web.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading','content','image','time','video_url')

admin.site.register(Blog,BlogAdmin)
```
17.To change admin header
```
admin.site.site_header = "PROJECT Administration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Admin Portal"
```
18. To remove user,groups from admin panel
```
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

```
19. migrating changes into app and database and adding superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
20. Getting data and passing through context
```
from web.models import Blog


def index(request):
    blog_datas = Blog.objects.all()

    context = {
        "title" : "HOME",
        "caption" : "The ultimate solution provider",
        "blog_datas" : blog_datas,
        "is_home" : True
    }
    return render(request, 'web/index.html',context)


def registration(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()

            response_data = {
                "status" : "true",
                "title" : "Successfully Submitted",
                "message" : "Registration successfully updated"
            }
        else:
            message = generate_form_errors(form)

            response_data = {
                "status" : "false",
                "stable" : "true",
                "title" : "Form validation error",
                "message" : message
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        form = NewsletterForm()
        context = {
            "title" : "Updates",
            "form" : form,
        }
        return render(request, 'web/updates.html',context)

```
```
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@9.15.3/dist/sweetalert2.all.min.js"></script>
```
```
$(document).on('submit', 'form.ajax', function(e) {
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var action_url = $this.attr('action');
    var isReset = $this.hasClass('reset');
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');

    $.ajax({
        url: action_url,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function(data) {

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
            var redirect = data.redirect;
            var redirect_url = data.redirect_url;

            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                Swal.fire({
                    title: title,
                    text: message,
                    icon: 'success',
                }).then(function() {
                    if (redirect == 'true') {
                        window.location.href = redirect_url;
                    }
                    if (reload == 'true') {
                        window.location.reload();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                Swal.fire({
                    title: title,
                    text: message,
                    icon: "error"
                });

            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            Swal.fire({
                title: title,
                text: message,
                icon: "error"
            });
        }
    });
});


$(document).on('click', '.action-button', function(e) {
    e.preventDefault();
    $this = $(this);
    var text = $this.attr('data-text');
    var id = $this.attr('data-id');
    var url = $this.attr('href');
    var title = $this.attr('data-title');
    if (!title) {title = "Are you sure?";}

    Swal.fire({
        title: title,
        text: text,
        icon: "warning",
        showCancelButton: true
    }).then(result => {
        if (result.value) {
            window.setTimeout(function() {
                $.ajax({
                    type: 'GET',
                    url: url,
                    dataType: 'json',
                    data: { pk: id },

                    success: function(data) {
                        var message = data.message;
                        var status = data.status;
                        var reload = data.reload;
                        var redirect = data.redirect;
                        var redirect_url = data.redirect_url;
                        var title = data.title;

                        if (status == "true") {
                            if (title) {
                                title = title;
                            } else {
                                title = "Success";
                            }

                            Swal.fire({
                                title: title,
                                text: message,
                                icon: "success"
                            }).then(function() {
                                if (redirect == 'true') {
                                    window.location.href = redirect_url;
                                }
                                if (reload == 'true') {
                                    window.location.reload();
                                }
                            });

                        } else {
                            if (title) {
                                title = title;
                            } else {
                                title = "An Error Occurred";
                            }
                            Swal.fire({ title:title, text: message, icon: "error"});

                        }
                    },
                    error: function(data) {
                        var title = "An error occurred";
                        var message = "An error occurred. Please try again later.";
                        Swal.fire({ title:title, text: message, icon: "error"});
                    }
                });
            }, 100);
        } else {
            console.log("action cancelled");
        }
    });
});

```

**functions.py**
```
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
```
**Template**
```
<form action="" method="post">

    {% csrf_token %}

    {{form.as_p}}

    <button type="submit">Submit</button>

<form>
```
```
<form action="" method="post">

    {% csrf_token %}

    {% for field in form %}
        <div class="form-group">
            <label for="{{field.id_for_label}}">{{field.label}}</label>
            {{field}}
        </div>
    {% endfor %}

    <button type="submit">Submit</button>

<form>
```
```
<form action="" method="post">

    {% csrf_token %}

    <div class="form-group">
        <label for="{{form.name.id_for_label}}">{{form.name.label}}</label>
        {{form.name}}
    </div>

    <div class="form-group">
        <label for="{{form.email.id_for_label}}">{{form.email.label}}</label>
        {{form.email}}
    <div class="form-group">

    <button type="submit">Submit</button>

<form>
```
```
	<title>{{title}} | {{caption}}</title>

    {% for blog in blog_datas %}
        <li>
            {{blog.image.url}}
            {{blog.title}}
            {{blog.content}}
        </li>
	{% empty %}
		No data found
    {% endfor %}
```
with if condition
```
    {% if blog_datas %}
        <p>content here</p>
    {% else %}
        <p>Nothing Found</p>
    {% endif %}
```
Get current year
```
    {% now 'Y' %}
```
possible filtering
```
all()
filter(id=1)
filter(name="x")
filter(name__icontains="x")
exclude(name="x")
get()
```
21. Fix hyperlinks
```
    href="{% url 'web:index' %}
    href="{% url 'web:about' %}
    href="{% url 'web:index' %}#features
```
22. Including template parts
```
    "is_home" : True
    "is_about" : True
```
```
    {% if is_home %}
        {% include 'web/includes/index-spotlight.html' %}
    {% elif is_about %}
        {% include 'web/includes/about-spotlight.html' %}
    {% endif %}
```
23. Database export and import
```
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
24. Delete migrations
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
```
25. response and Redirect
```
def index(request):
    return HttpResponseRedirect(reverse('web:about'))


def about(request):
    return HttpResponse('Hello from about')
````
26. Registration Redux
```
pip install django-registration-redux

add to installed apps

'registration',

#registration redux settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

REGISTRATION_EMAIL_SUBJECT_PREFIX = ''
SEND_ACTIVATION_EMAIL = False
REGISTRATION_OPEN = False


path('app/accounts', include('registration.backends.default.urls')),


{% url 'auth_password_change' %}
{% url 'auth_logout' %}
{% url 'auth_login' %}
{% url 'auth_password_reset' %}
{% url 'registration_register' %}
```
27. Removing sensitive info (python-decouple)
```
pip install python-decouple
```
```
import os
from decouple import config, Csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

LOGIN_URL = '/app/accounts/login/'
LOGOUT_URL = '/app/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

REGISTRATION_EMAIL_SUBJECT_PREFIX = ''
SEND_ACTIVATION_EMAIL = True
REGISTRATION_OPEN = True

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL= config('DEFAULT_FROM_EMAIL')
DEFAULT_BCC_EMAIL= config('DEFAULT_BCC_EMAIL')
DEFAULT_REPLY_TO_EMAIL = config('DEFAULT_REPLY_TO_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')
ADMIN_EMAIL = config('ADMIN_EMAIL')
EMAIL_BACKEND= config('EMAIL_BACKEND')

```
create .env file
```

SECRET_KEY = 5h!q83i3@87m!+9

DEBUG = True

# database credentials
ENGINE = django.db.backends.postgresql_psycopg2
DB_NAME = db
DB_USER = user
DB_PASSWORD = S3CR3ET
DB_HOST = localhost

EMAIL_BACKEND= django.core.mail.backends.smtp.EmailBackend
EMAIL_PORT = 587
EMAIL_HOST = smtp-relay.sendinblue.com
EMAIL_HOST_USER = hello@example.com
EMAIL_HOST_PASSWORD = S3CR3ET
DEFAULT_FROM_EMAIL = hello@example.com
DEFAULT_BCC_EMAIL = hello@example.com
DEFAULT_REPLY_TO_EMAIL = hello@example.com
SERVER_EMAIL = hello@example.com
ADMIN_EMAIL = hello@example.com

```
28. Context processors
```
import datetime


def main_context(request):
    today = datetime.date.today()
    is_superuser = False
    if "set_user_timezone" in request.session:
        user_session_ok = True
        user_time_zone = request.session['set_user_timezone']
    else:
        user_session_ok = False
        user_time_zone = "Asia/Kolkata"

    current_role = "user"

    active_parent = request.GET.get('active_parent')
    active = request.GET.get('active')

    return {
        'app_title' : "Metrica",
        "confirm_delete_message" : "Are you sure want to delete this item. All associated data may be removed.",
        "revoke_access_message" : "Are you sure to revoke this user's login access",
        "confirm_delete_selected_message" : "Are you sure to delete all selected items.",
        "confirm_read_message" : "Are you sure want to mark as read this item.",
        "confirm_read_selected_message" : "Are you sure to mark as read all selected items.",
        'domain' : request.META['HTTP_HOST'],
        "is_superuser" : is_superuser,
        "active_parent" : active_parent,
        "active_menu" : active,
    }
```
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [config('TEMPLATES')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.main_context',
            ],
        },
    },
]
```
29. Ajax

```
$(document).ready(function() {

    $(document).on('submit','form.ajax_file', function(e) {
        e.preventDefault();
        var $this = $(this);
        var data = new FormData(this);
        var isReset = $this.hasClass('reset');
        var isReload = $this.hasClass('reload');
        var isRedirect = $this.hasClass('redirect');
        show_loader();

        $.ajax({
            url: window.location.pathname,
            type: 'POST',
            data: data,
            cache: false,
            contentType: false,
            processData: false,
            dataType: "json",

            success: function(data) {
                remove_popup();

                var status = data.status;
                var title = data.title;
                var message = data.message;
                var pk = data.pk;
                var redirect = data.redirect;
                var redirect_url = data.redirect_url;

                if (status == "true") {
                    if (title) {title = title;}
                    else {title = "Success";}
                    swal({title: title,text: message,type: "success"});

                    swal({title: title,text: message,type: "success"},
                    function () {
                        if (isRedirect && redirect == 'true') {
                            window.location.href = redirect_url;
                        }
                        if (isReload) {
                            window.location.reload();
                        }
                        if (isReset) {
                            $this[0].reset();
                        }
                    });
                }
                else {
                    title = "An Error Occurred";
                    swal(title, message, "error");
                }
            },
            error: function(data) {
                remove_popup();
                var title = "An error occurred";
                var message = "Upload a valid image. The file you uploaded was either not an image or a corrupted image.";
                swal(title, message, "error");
            }
        });
    });
```

```

$(document).on('submit', 'form.ajax', function(e) {
    
    e.preventDefault();
    var $this = $(this);
    var data = new FormData(this);
    var isReset = $this.hasClass('reset');
    var isReload = $this.hasClass('reload');
    var isRedirect = $this.hasClass('redirect');

    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        dataType: "json",

        success: function(data) {

            var status = data.status;
            var title = data.title;
            var message = data.message;
            var pk = data.pk;
            var redirect = data.redirect;
            var redirect_url = data.redirect_url;

            if (status == "true") {
                if (title) {
                    title = title;
                } else {
                    title = "Success";
                }

                swal({
                    title: title,
                    text: message,
                    icon: "success",
                    type: "success"
                }).then(function() {
                    if (isRedirect && redirect == 'true') {
                        window.location.href = redirect_url;
                    }
                    if (isReload) {
                        window.location.reload();
                    }
                    if (isReset) {
                        $this[0].reset();
                    }
                });

            } else {
                if (title) {
                    title = title;
                } else {
                    title = "An Error Occurred";
                }
                swal({
                    title: title,
                    text: message,
                    icon: "error",
                    type: "error"
                });
            }
        },
        error: function(data) {
            var title = "An error occurred";
            var message = "something went wrong";
            swal({
                title: title,
                text: message,
                type: "error"
            });
        }
    });
});

```

30. Humanise
```
#add following to your INSTALLED_APPS in setting:

django.contrib.humanize

#In template, load the template tags:

{% load humanize %}

#sample
{% extends 'base.html' %}

{% load humanize %}

{% block content %}
  <ul>
    {% for notification in notifications %}
      <li>
        {{ notification }}
        <small>{{ notification.date|naturaltime }}</small>
      </li>
    {% empty %}
      <li>You have no unread notification.</li>
    {% endfor %}
  </ul>
{% endblock %}


Note : The for tag can take an optional {% empty %} clause whose text is displayed if the given array is empty or could not be found:

#available template filters:
apnumber    1                      becomes  one
intcomma	4500000                becomes  4,500,000
intword     1200000                becomes  1.2 million
naturalday	08 May 2016            becomes  yesterday
naturaltime	09 May 2016 20:54:31   becomes  29 seconds ago
ordinal 	3                      becomes      3rd

```
31. Adding (changeble)initial value into form (views.py)
```
form = CustomerForm(initial={
        "name" : "Default Name",
        "email" : "Default Email"
    })
```
```
# Default template tags
{{instance.date|date:"d/m/Y"}}

# Custom template tags
    mkdir main/templatetags/
    touch main_template_tags.py __init__.py

    # on main_template_tags.py
    @register.filter
    def to_fixed_to(value):
        return "{:10.2f}".format(value)

# on required template
{% load main_template_tags %}

{{instance.date|to_fixed_to}}

```
33. ManytoMany Field
```
#models
assign_to  = models.ManyToManyField('employees.Employee')

#form
from django.forms.widgets import SelectMultiple

widgets = {
    'assign_to' : SelectMultiple(attrs={'class': 'required form-control'}),
}

#template
{% for i in instance.assign_to.all %}
        <a href="{% url 'employees:profile' pk=i.pk %}">{{ i }}</a>,
{% endfor %}