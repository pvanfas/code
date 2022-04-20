from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.Index.as_view(),name='index'),

    path('units/', views.UnitList.as_view(),name='unit_list'),
    path('new/unit/', views.UnitForm.as_view(),name='new_unit'),
    path('view/unit/<str:pk>/', views.UnitDetail.as_view(),name='view_unit'),
    path('update/unit/<str:pk>/', views.UnitUpdate.as_view(),name='update_unit'),
    path('delete/unit/<str:pk>/', views.UnitDelete.as_view(),name='delete_unit'),
]
