pip install django-registration-redux

#settings. installed apps
'registration',

#set login url after AUTHENTICATION_BACKENDS  
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SEND_ACTIVATION_EMAIL = False
REGISTRATION_EMAIL_SUBJECT_PREFIX = ''

REGISTRATION_OPEN = True
LOGIN_URL = '/app/accounts/login/'
LOGOUT_URL = '/app/accounts/logout/'
LOGIN_REDIRECT_URL = '/admin/'

EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL= config('DEFAULT_FROM_EMAIL')
DEFAULT_BCC_EMAIL= config('DEFAULT_BCC_EMAIL')
DEFAULT_REPLY_TO_EMAIL = config('DEFAULT_REPLY_TO_EMAIL')
SERVER_EMAIL = config('SERVER_EMAIL')
ADMIN_EMAIL = config('ADMIN_EMAIL')

#urls.py
path('accounts/', include('registration.backends.default.urls')),

#as form.action or a.href
{% url 'auth_password_change' %}	#Change Password
{% url 'auth_logout' %}				#Logout
{% url 'auth_login' %}				#Login
{% url 'auth_password_reset' %}		#Reset Password
{% url 'registration_register' %} #register
