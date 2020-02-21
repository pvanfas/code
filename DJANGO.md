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
    path('',include('web.urls',namepace='web'))

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
17. Passing data and context into templates
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
