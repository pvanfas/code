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

# NEW PAGE ----------------------------------------------------


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

# update link in index
    {% url 'web:about' %}

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


# TEMPLATE EXTENDING (PAGES) -------------------------------------------------

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


# TEMPLATE EXTENDING (GENERAL) -------------------------------------------------

    # create base.html
        -------- header here --------
        {% block content %}
        {% endblock%}
        ------- footer here --------

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


    ---------------------------- finished ----------------------------
