
```
# models.py
from django.db import models
from main.models import BaseModel
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.urls import reverse


class Category(BaseModel):
    code = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Product Category')
        verbose_name_plural = ('Product Categories')

    @property
    def product_count(self):
        return Product.objects.filter(category=self,is_deleted=False).count()

    def get_absolute_url(self):
        return reverse('products:view_category', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('products:update_category', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('products:delete_category', kwargs={'pk': self.pk})

    def __str__(self):
        return str(f"{self.code} - {self.name}")

# urls.py
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('categories/', views.CategoryList.as_view(),name='category_list'),
    path('view/category/<str:pk>/', views.CategoryDetail.as_view(),name='view_category'),
    path('new/category/', views.CategoryForm.as_view(),name='new_category'),
    path('update/category/<str:pk>/', views.CategoryUpdate.as_view(),name='update_category'),
    path('delete/category/<str:pk>/', views.CategoryDelete.as_view(),name='delete_category'),
]


# views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Category


class CategoryList(ListView):
    queryset = Category.objects.filter(is_deleted=False)


class CategoryDetail(DetailView):
    model = Category


class CategoryForm(CreateView):
    model = Category
    fields = ['name','code','description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Category"
        return context


class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name','code','description']
    template_name_suffix = '_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Edit Category -"
        return context


class CategoryDelete(DeleteView):
    model = Category
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('products:category_list')


# admin.py
from django.contrib import admin
from django.apps import apps

app = apps.get_app_config('products')

for model_name, model in app.models.items():
    admin.site.register(model)

# templates/model/category_detail.html
<p>{{object.name}}</p>
<p>{{object.code}}</p>

# templates/model/category_form.html
{% load crispy_forms_tags %}

<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{form|crispy}}
    <button type="submit" class="btn btn-primary pull-right">Save</button>
    <div class="clearfix"></div>
</form>


# templates/model/category_list.html

{% for object in object_list %}
<tr>
    <td><a href="{{object.get_absolute_url}}">{{object.name}}</a></td>
    <td class="td-actions">
        <a href="{{object.get_absolute_url}}" rel="tooltip" class="btn btn-info btn-round">
            <i class="material-icons">open_in_new</i>
        </a>
        <a href="{{object.get_update_url}}" rel="tooltip" class="btn btn-success btn-round">
            <i class="material-icons">edit</i>
        </a>
        <a href="{{object.get_delete_url}}" rel="tooltip" class="btn btn-danger btn-round">
            <i class="material-icons">close</i>
        </a>
    </td>
</tr>
{% endfor %}

# templates/model/confirm_delete.html

<form method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ object }}"?</p>
    <button type="submit" class="mb-4 btn btn-primary">Confirm</button>
</form>

```
