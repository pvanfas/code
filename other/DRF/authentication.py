# API Authentication using jwt
# Detailed documenation at [https://github.com/pvanfas/code/blob/master/DRF/simplejwt.rst]

# pip install djangorestframework_simplejwt

# Add to setting.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

create folder /authentication in v1 and add __init__.py, urls.py, serializers.py, views.py

# Define url in root url
url(r'^api/v1/auth/', include('api.v1.authentication.urls',namespace="api_v1_authentication")),

# Views.py (python3)
from django.conf.urls import include, url
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

# Views.py (python3)
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Custom token lifetime
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# getting authentication tokens
http://localhost:8000/api/v1/auth/token/
# Refreshing access tokens
http://localhost:8000/api/v1/auth/refresh/
# Token validation
https://jwt.io/         ALGORITHM: HS512

# Response on authentication
change decorator @permission_classes((AllowAny,)) to @permission_classes((IsAuthenticated,))

# Accessing auth protected data
postman: Authentication --> Bearer token --> paste token

# Overwriting default authentication class and add new datas 
(authentication/serializers.py)
from django.utils.six import text_type
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token
        
    def validate(cls, attrs):
        data = super(UserTokenObtainPairSerializer, cls).validate(attrs)
        
        refresh = cls.get_token(cls.usr)
        
        data['refresh'] = text_type(refresh)
        data["access"] = text_type(refresh.access_token)
        
        if cls.user.is_superuser:
            data["role"] = "superuser"
        else:
            data["role"] = "user"
            
        return data
        
(authentication/views.py)
from api.v1.IsAuthentication.serializers import UserTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer

(authentication/urls.py)
from django.conf.urls import include, url
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]

