# Create web/urls.py and paste the following
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('about/', views.about,name="about"),
]