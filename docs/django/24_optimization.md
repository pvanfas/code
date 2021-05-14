
Database export and import
```
python manage.py dumpdata > database.json
python manage.py loaddata database.json
```
Delete migrations
```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
find . -path "*/migrations/*.pyc"  -delete
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
```
Run Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
Clean Django Admin Log Entries
```
python3 manage.py shell

from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
```
Setup production postgresql database
```
sudo su postgres
su - postgres (for servers)
```
```
createdb project_db
createuser project_dbuser -P
psql
grant all privileges on database project_db to project_dbuser;
\q
exit
```
GIT-IGNORE File

```
### Django ###
*.log
*.pot
*.pyc
migrations/*.py
__pycache__/
!__init__.py
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
*.zip
```
Re-Initiate Git
```
git checkout --orphan latest_branch
git add -A
git commit -am "commit message"
git branch -D master
git branch -m master
git push -f origin master
```