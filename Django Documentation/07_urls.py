# Create web/urls.py and paste the following
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", TemplateView.as_view(template_name="web/about.html")),
]
