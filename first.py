source: https://books.agiliq.com/projects/djenofdjango/en/latest/index.html

#setting up virtual environment (python 2)
mkdir project && cd project && mkdir src
virtualenv venv
source venv/bin/activate
cd src && pip install django==1.11.15 && pip install pillow psycopg2
django-admin.py startproject project
cd project && mkdir static media templates
python manage.py runserver

#setting up virtual environment (python 3)
mkdir project && cd project && mkdir src
virtualenv venv -p python3
source venv/bin/activate
cd src && pip install django && pip install pillow
django-admin.py startproject project
cd project && mkdir static media templates
python manage.py runserver

#start a new app
python manage.py startapp web

#register in INSTALLED APPS
'web'

#define template directory in TEMPLATES
'templates'

#define DATABASES
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

#set media url
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

#define urlpatterns in project/urls.py
from django.conf.urls import url ,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('web.urls',namespace="web")),

    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),
]

admin.site.site_header = "PROJECT Admininistration"
admin.site.site_title = "PROJECT Admin Portal"
admin.site.index_title = "Welcome to PROJECT Researcher Portal"

#create web/urls.py and paste the following
from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index,name="index"),
    #url(r'^about/', views.about,name="about")
]

#edit web/views.py
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	return HttpResponse("Hello World")

#template rendering
    #Add assets into /static and html into /templates/web
    #Add {% load static %} after <head> tag and Change directory path to href="{% static 'location' %}"
    #example:
        <script src="{% static 'js/script.js' %}"></script>

#setup database
sudo su postgres
createdb project
createuser user -P
psql
grant all privileges on database femme to techpe;
\q
exit

#django models
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

# Import model and define list display in admin.py
from __future__ import unicode_literals
from django.contrib import admin
from web.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading','content','image','time','video_url')

admin.site.register(Blog,BlogAdmin)

# migrate changes into app and database
python manage.py makemigrations
python manage.py migrate

# Add superuser
python manage.py createsuperuser

#database export and import
python manage.py dumpdata > database.json
python manage.py loaddata database.json

#delete migrations
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

#change view into render, pass context,get objects in web/views.py
from web.models import Blog

def index(request):
    blog_datas = Blog.objects.all()

    context = {
        "title" : "HOME",
        "caption" : "The ultimate solution provider",
        "blog_datas" : blog_datas,
    }
    return render(request, 'web/index.html',context)

# pass context and data into template
	<title>{{title}} | {{caption}}</title>

    {% for blog in blog_datas %}
    <li>
        {{blog.image.url}}
        {{blog.title}}
        {{blog.content}}
    </li>
    {% endfor %}

    # with if condition

    {% if blog_datas %}
        <p>content here</p>
    {% else %}
        <p>Nothing Found</p>
    {% endif %}

    # Current year update
    {% now 'Y' %}
    
#You have successfully configured the basics......................................................
