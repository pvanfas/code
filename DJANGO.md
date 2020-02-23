1. Setting up virtual environment (python 3)
```
virtualenv venv -p python3
source venv/bin/activate
pip install django
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

4. Define template directory in TEMPLATES

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
6. Set media url

```
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_URL = '/static/'
STATIC_FILE_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
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

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

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
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
import json, datetime


def index(request):
    context = {
        "title" : "HOME",
        "caption" : "The ultimate solution provider",
        "is_home" : True
    }
    return render(request, 'web/index.html',context)

```

10. Template rendering
```
    (i). Add assets into /static and html into /templates/web
    (ii). Add {% load static %} after <head> tag and Change directory path to href="{% static 'location' %}"
    (iii). example:
        <script src="{% static 'js/script.js' %}"></script>
```
11. Setup database
```
sudo su postgres
createdb project
createuser user -P
psql
grant all privileges on database db to user;
\q
exit
```

12. Django models
```
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Blog(models.Model):
    heading = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(upload_to='images/blog')
    time = models.DateTimeField()
    video_url = models.URLField()

    class Meta:
        db_table = 'web_blog'
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')

    def __unicode__(self):
        return str(self.pk)
```

13. Import model and define list display in admin.py
```
from __future__ import unicode_literals
from django.contrib import admin
from web.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading','content','image','time','video_url')

admin.site.register(Blog,BlogAdmin)
```
14.To change admin header
```
admin.site.site_header = "PROJECT Admininistration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Researcher Portal"
```
15. To remove user,groups from admin panel
```
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)

```
16. migrating changes into app and database and adding superuser
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
17. Getting data and passing through context
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
```

```
	<title>{{title}} | {{caption}}</title>

    {% for blog in blog_datas %}
        <li>
            {{blog.image.url}}
            {{blog.title}}
            {{blog.content}}
        </li>
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
18. Template extending

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
19. Fix hyperlinks
```
        href="{% url 'web:index' %}
        href="{% url 'web:about' %}
        href="{% url 'web:index' %}#features
```
20. Including template parts
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
21. Database export and import
```
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
22. Delete migrations
```
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
```
23. response and Redirect
```
def index(request):
    return HttpResponseRedirect(reverse('web:about'))


def about(request):
    return HttpResponse('Hello from about')
```
24. Removing sensitive info
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

EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL= config('DEFAULT_FROM_EMAIL')
DEFAULT_BCC_EMAIL= config('DEFAULT_BCC_EMAIL')

SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')
SOCIAL_AUTH_TWITTER_KEY =config('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET =config('SOCIAL_AUTH_TWITTER_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY =config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET =config('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
```
create .env file
```
SECRET_KEY = 1-syzfqfafqffcqfqdq8lcs-25#ts7jb^4q1cxevsuvg1t$u3

DEBUG = True
ALLOWED_HOSTS = *
TEMPLATES = templates

# database credentials
ENGINE = django.db.backends.postgresql_psycopg2
DB_NAME = db
DB_USER = user
DB_PASSWORD = password
DB_HOST = localhost

# email authentication credentials
EMAIL_HOST = smtp-relay.sendinblue.com
EMAIL_PORT = 587
EMAIL_HOST_USER = anfaspv.info@gmail.com
EMAIL_HOST_PASSWORD = 2cgwrgrgr
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = verification@awardize.com
DEFAULT_BCC_EMAIL =verification@awardize.com

# social authentication credentials
SOCIAL_AUTH_GITHUB_KEY= 2cgwrgrgrgegwgwsgsg599b930
SOCIAL_AUTH_GITHUB_SECRET= 2cgwrgrgrgegwgwsgsg599b930
SOCIAL_AUTH_TWITTER_KEY = 2cgwrgrgrgegwgwsgsg599b930
SOCIAL_AUTH_TWITTER_SECRET = 2cgwrgrgrgegwgwsgsg599b930
SOCIAL_AUTH_FACEBOOK_KEY = 2cgwrgrgrgegwgwsgsg599b930
SOCIAL_AUTH_FACEBOOK_SECRET = 2cgwrgrgrgegwgwsgsg599b930

```
25. Context processors
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

    current_theme = 'cyan-600'
    current_role = "user"

    if request.user.is_authenticated:
        recent_notifications = Notification.objects.filter(user=request.user,is_deleted=False)
    else:
        recent_notifications = []

    active_parent = request.GET.get('active_parent')
    active = request.GET.get('active')

    return {
        'app_title' : "Purple",
        "profile" : profile,
        "confirm_delete_message" : "Are you sure want to delete this item. All associated data may be removed.",
        "revoke_access_message" : "Are you sure to revoke this user's login access",
        "confirm_delete_selected_message" : "Are you sure to delete all selected items.",
        "confirm_read_message" : "Are you sure want to mark as read this item.",
        "confirm_read_selected_message" : "Are you sure to mark as read all selected items.",
        'domain' : request.META['HTTP_HOST'],
        "current_theme" : current_theme,
        "is_superuser" : is_superuser,
        "active_parent" : active_parent,
        "active_menu" : active,
        "recent_notifications" : recent_notifications,
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
26. Adding (changeble)initial value into form (views.py)
```
form = CustomerForm(initial={
        "name" : "Default Name",
        "email" : "Default Email"
    })
```
27. Decorators
@login_required
```
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    pass
```
@require_http_methods
```
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
```
@group_required

Sometimes we need to protect some views, to allow a certain group of users to access it. Instead of checking within it if the user belongs to that group/s, we can use the following decorator
```
from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated:
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)


# The way to use this decorator is:
@group_required(‘admins’, ‘seller’)
def my_view(request, pk)
    ...
```
@anonymous_required

This decorator is based on the decorator login_required of Django, but looks for the opposite case, that the user is anonymous, otherwise the user is redirected to the website defined in our settings.py and can be useful when we want to protect logged user views, such as the login or registration view
```
def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = settings.LOGIN_REDIRECT_URL

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous(),
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


# The way to use this decorator is:
@anonymous_required
def my_view(request, pk)
    ...
```
@superuser_only

This is the same case as when we want to allow certain groups access to a view, but in this case only super users can visit it.
```
from django.core.exceptions import PermissionDenied


def superuser_only(function):
  """Limit view to superusers only."""

   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied           
       return function(request, *args, **kwargs)
   return _inner


# The way to use this decorator is:
@superuser_only
def my_view(request):
    ...
```
@ajax_required

This decorator check if the request is an AJAX request, useful decorator when we are working with Javascript frameworks as jQuery and a good way to try to secure our application
```
from django.http import HttpResponseBadRequest


def ajax_required(f):
   """
   AJAX request required decorator
   use it in your views:

   @ajax_required
   def my_view(request):
       ....

   """   

   def wrap(request, *args, **kwargs):
       if not request.is_ajax():
           return HttpResponseBadRequest()
       return f(request, *args, **kwargs)

   wrap.__doc__=f.__doc__
   wrap.__name__=f.__name__
   return wrap


# The way to use this decorator is:
@ajax_required
def my_view(request):
    ...
```
@timeit

This decorator is very helpful if you need to improve the response time of one of then our views or if you just want to know how long it takes to run.
```
def timeit(method):

   def timed(*args, **kw):
       ts = time.time()
       result = method(*args, **kw)
       te = time.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result

   return timed


# The way to use this decorator is:
@timeit
def my_view(request):
    ...

```