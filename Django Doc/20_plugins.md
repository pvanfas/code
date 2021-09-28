### Versatile Image Field

Install versatile image field package

    pip install django-versatileimagefield

Add to installed apps

    'versatileimagefield',

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
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Change image src

    src="{{instance.photo.crop.200x200}}"
    src="{{instance.photo.thumbnail.600x600}}"


### Django Import Export
Install package

```
pip install django-import-export
```
Add to installed apps
```
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```
Integrate to admin
```
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
```
