from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index,name="index"),
    path('contact/', views.contact,name="contact"),
    path('blog/<str:slug>/', views.blogview,name="blogview"),
]