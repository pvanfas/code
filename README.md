DJANGO CLEANUP

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -name '.DS_Store' -type f -delete
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py migrate
python manage.py createsuperuser
```
```
python manage.py shell

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
```
