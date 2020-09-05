DJANGO CLEANUP

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -name '.DS_Store' -type f -delete
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
```
python manage.py shell

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
```
```
git checkout --orphan latest_branch
git add -A
git commit -am "commit message"
git branch -D master
git branch -m master
git push -f origin master
```
```
git remote add origin https://gedexo@bitbucket.org/gedexo/project.git
git push -u origin master
```
