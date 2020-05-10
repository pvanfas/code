pip install django-registration-redux

#settings. installed apps
'registration',

#set login url after AUTHENTICATION_BACKENDS  
LOGIN_URL = '/app/accounts/login/'
LOGOUT_URL = '/app/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

#urls.py
path('app/accounts', include('registration.backends.default.urls')),
path('app/users', include('users.urls', namespace="users")),

#as form.action or a.href
{% url 'auth_password_change' %}	#Change Password
{% url 'auth_logout' %}				#Logout
{% url 'auth_login' %}				#Login
{% url 'auth_password_reset' %}		#Reset Password