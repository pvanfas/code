# install DRF
pip install djangorestframework
pip install markdown
pip install django-filter

#Add 'rest_framework' to  INSTALLED_APPS setting.

INSTALLED_APPS = [
    ...
    'rest_framework',
]

#Add the following to root urls.py file.
urlpatterns = [
    ...
    url(r'^api-auth/', include('rest_framework.urls')),
]

#Create folder project/api/v1/customers
Add __init__.py to each of them to make it a python directory
create urls.py and views.py in v1/customers

mkdir api && cd api && touch __init__.py && mkdir v1 && cd v1 && touch __init__.py && mkdir customers && cd customers && touch __init__.py views.py urls.py

(urls.py)
import views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', views.customers, name='customers'),

]

(views.py)
from api.v1.customers.serializers import CustomerSerializer
from customers.models import Customer
from rest_framework import status
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def customers(request):
    instances = Customer.objects.filter(is_deleted = False)
    serialized = CustomerSerializer(instances,many=True)
    
    response_data = {
        "statusCode" : 6000,
        'data' : serialized.data
    }
    
    return Response(response_data, status=status.HTTP_200_OK)

# include urls.py in root url

urlpatterns = [
    ...
    url(r'^api/v1/customers/', include('api.v1.customers.urls',namespace="api_v1_customers")),

]
# create a new file serializers.py inside /customers
touch api/v1/customers/serializers.py

(serializers.py)
from customers.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ['id','name', 'email', 'phone', 'address', 'photo']


# Accessing single customer data
(urls.py)
urlpatterns = [
    ...
    url(r'^view/(?P<pk>.*)/$', views.customer, name='customer'),

]
(views.py)    
@api_view(['GET'])
@permission_classes((AllowAny,))
@renderer_classes((JSONRenderer,))
def customer(request,pk):
    instance = None
    if Customer.objects.filter(is_deleted = False, pk=pk).exists():
        instance = Customer.objects.get(is_deleted = False, pk=pk)
    
    if instance:
        serialized = CustomerSerializer(instance,context={"request":request})
    
        response_data = {
            "statusCode" : 6000,
            'data' : serialized.data
        }
    else:
        response_data = {
            "statusCode" : 6001,
            'message' : "Customer not found"
        }
    return Response(response_data, status=status.HTTP_200_OK)
    
# Add new api
    1. Define url in root urls
    2. Create directory sales in v1
    3. Make it python directory
    4. Add views, urls and serializers
    5. Change fields according to model
    6. Edit views, urls and serializers

# Modifying APIU response (serializers.py)
class SaleSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Sale
        fields = ['id','customer','customer_name','date','subtotal','discount','total']
    
    def get_customer_name(self,instance):
        if instance.customer:
            return instance.customer.name
        else:
            return ""
            