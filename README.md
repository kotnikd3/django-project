## django-project
Full stack project in Django for learning purposes.

### Create Python virtual environment and activate it
```bash
cd django-project
python3 -m venv .
source bin/activate
```

### Install dependencies
```bash
pip install --upgrade pip
pip install django django-crispy-forms Pillow
```

### Create and run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Run
```bash
python manage.py runserver
```