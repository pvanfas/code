### Django Registration Redux

Install package

    pip install django-registration-redux

Add to installed apps

    INSTALLED_APPS = (
        ...
        'registration',
    )

Set login url after AUTHENTICATION_BACKENDS  

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

Setting up URLs

    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('registration.backends.simple.urls')),

Templates
[Default Templates](https://github.com/macropin/django-registration/tree/master/registration/templates/registration)

Auth Ref Links

        {% url 'auth_password_change' %}	        # Change Password
        {% url 'auth_logout' %}			# Logout
        {% url 'auth_login' %}			# Login
        {% url 'auth_password_reset' %}		# Reset Password
        {% url 'registration_register' %}           # Register

### Versatile Image Field

Install versatile image field package

    pip install django-versatileimagefield

Add to installed apps

    INSTALLED_APPS = (
        ...
        'versatileimagefield',
    )

Add versatile settings to settings.py

    VERSATILEIMAGEFIELD_SETTINGS = {
    	'cache_length': 2592000,
    	'cache_name': 'versatileimagefield_cache',
    	'jpeg_resize_quality': 70,
    	'sized_directory_name': '__sized__',
    	'filtered_directory_name': '__filtered__',
    	'placeholder_directory_name': '__placeholder__',
    	'create_images_on_demand': True,
    	'image_key_post_processor': None,
    	'progressive_jpeg': False
    }

Import plugin and Change ImageField into versatileimagefield

    from versatileimagefield.fields import VersatileImageField


    photo = VersatileImageField('Photo',blank=True,null=True,upload_to="customers/")

Run Migrations

    python3 manage.py makemigrations
    python3 manage.py migrate

Change image src

    src="{{instance.photo.crop.200x200}}"
    src="{{instance.photo.thumbnail.600x600}}"

### Django Import Export

Install package

    pip install django-import-export

Add to installed apps

    INSTALLED_APPS = (
        ...
        'import_export',
    )

Integrate to admin

    # As Admin Action
    from import_export.admin import ImportExportActionModelAdmin


    @admin.register(Designation)
    class DesignationAdmin(ImportExportActionModelAdmin):
        pass


    # As Button
    from import_export import fields, resources


    class RegistrationResource(resources.ModelResource):

        class Meta:
            model = models.Registration

    		#  Use the exclude option to blacklist fields:
    		exclude = ('imported', )

    		# Use the fields option to whitelist fields:
    		fields = ('id', 'name', 'author', 'price',)

    		# You can optionally set which fields are used as the id when importing
    		import_id_fields = ('isbn',)

    		# When defining ModelResource fields it is possible to follow model relationships
    		fields = ('author__name',)

    		# An explicit order for exporting fields can be set using the export_order option
            export_order = ('id', 'price', 'author__name')


    class RegistrationAdmin(ImportExportModelAdmin):
        resource_class = RegistrationResource
