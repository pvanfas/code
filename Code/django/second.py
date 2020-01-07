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

## DYNAMIC CONTENT RENDERING ------------------------------------------

def index(request):
    about_datas = About.objects.all()
    context = {
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


# Updating additional requiremets

    # Define fields in models.py
    subheading = models.CharField(max_length=128)
    date_added = models.DateField()
    # Make migrations and migrate
    # Update html with required tags

    ---------------------------- finished ----------------------------
