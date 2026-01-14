### Create the project & virtualenv (why: isolation, reproducibility)
```bash
   mkdir alx_travel_app && cd alx_travel_app
   python -m venv .venv
   .venv\Scripts\Activate.ps1
```

### Create requirements.txt and install packages (why: repeatable installs)
```bash
    Django>=4.2
    djangorestframework
    django-cors-headers
    django-environ
    drf-yasg
    celery
    pika            # (for RabbitMQ python client directly; optional)
    mysqlclient     # or PyMySQL (mysqlclient is common)
```

### Install the libraries
```bash
   pip install -r requirements.txt
```

### Start the Django project & app
```bash
    django-admin startproject alx_travel_app .
    python manage.py startapp listings

### Configure settings.py — REST framework, CORS, MySQL via environment variables
```bash
   INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # third-party
    "rest_framework",
    "corsheaders",
    "drf_yasg",

    # local apps
    "listings",
] 
```
### Configure Celery
```bash
    python -m celery -A alx_travel_app worker --loglevel=info
```

### Migrate and runserver
```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser   # optional
    python manage.py runserver
```

> Note: 
```bash
    docker compose exec app python alx_travel_app/manage.py migrate
    docker compose down --remove-orphans # remove orphaned containers
    docker compose build --no-cache # If dockerfile is changed, rebuild without cache
```