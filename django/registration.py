pip install django-registration-redux==1.7

#settings. installed apps
'registration',

#set login url after AUTHENTICATION_BACKENDS  
LOGIN_URL = '/app/accounts/login/'
LOGOUT_URL = '/app/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

#urls.py
url(r'^app/accounts/', include('registration.backends.default.urls')),
url(r'^app/users/', include('users.urls', namespace="users")),

#as form.action or a.href
{% url 'auth_password_change' %}	#Change Password
{% url 'auth_logout' %}				#Logout
{% url 'auth_login' %}				#Login
{% url 'auth_password_reset' %}		#Reset Password