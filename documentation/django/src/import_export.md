### Installation and configuration
```
pip install django-import-export
```
```
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```
```
python manage.py collectstatic
```
```
# admin.py

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class RegistrationResource(resources.ModelResource):

    class Meta:
        model = models.Registration


class RegistrationAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    search_fields = ('full_name',)
    list_filter = ('zone','gender')
    readonly_fields = ('phone_number','password',)
    list_display = ('full_name','phone_number','whatsapp_number','zone','gender')

```
