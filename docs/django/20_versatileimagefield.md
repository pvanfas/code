
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
