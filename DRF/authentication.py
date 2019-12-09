# API Authentication using jwt
(Detailed documenation at [https://github.com/pvanfas/code/blob/master/DRF/simplejwt.rst])

pip install djangorestframework_simplejwt

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
from django.conf.urls import url,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

# Views.py (python3)
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

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

# Ckecking authentication
http://localhost:8000/api/v1/auth/token/
http://localhost:8000/api/v1/auth/refresh/
https://jwt.io/         ALGORITHM: HS512



