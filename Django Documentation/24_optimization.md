Database export and import

    python manage.py dumpdata > database.json
    python manage.py loaddata database.json

Delete migrations

    find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
    find . -path "*/migrations/*.pyc"  -delete
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

Run Migrations

    python3 manage.py makemigrations
    python3 manage.py migrate

Optimize Code

    pip install isort autoflake black flake8

    autoflake -i -r --expand-star-imports --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --recursive .
    
    isort .
    black .
    
    flake8  --exclude=backup --ignore=E501,W503,E722


Clean Django Admin Log Entries

    python3 manage.py shell

    from django.contrib.admin.models import LogEntry

    LogEntry.objects.all().delete()

Setup production postgresql database

    sudo su postgres
    su - postgres (for servers)

    createdb project_db
    createuser project_dbuser -P
    psql
    grant all privileges on database project_db to project_dbuser;
    \q
    exit

GIT-IGNORE File

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

Re-Initiate Git

    git checkout --orphan latest_branch
    git add -A
    git commit -am "commit message"
    git branch -D master
    git branch -m master
    git push -f origin master

Attach a README.md File

    Because no one can read your mind. Yet, Scientists and companies like Facebook and Neuralink (presumably) 
    are working on it. Perhaps in the future, you'll be able to attach a copy of your thoughts and/or 
    consciousness to your projects. In the meantime, please make READMEs.
