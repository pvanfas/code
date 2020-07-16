DJANGO SETUP

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
DJANGO COMMANDS

```
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
