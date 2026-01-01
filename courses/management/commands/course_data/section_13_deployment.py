"""
Section 13: Deployment
Deploying Django applications to production
"""

SECTION_DATA = {
    'slug': 'deployment',
    'title_en': 'Deployment',
    'title_fa': 'استقرار',
    'description_en': 'Deploy Django applications to production',
    'description_fa': 'استقرار برنامه‌های جنگو در production',
    'lessons': [
        {
            'slug': 'production-settings',
            'title_en': 'Production Settings',
            'title_fa': 'تنظیمات Production',
            'content_en': '''Configure Django for production deployment.

Key Settings:
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Database (PostgreSQL recommended)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

Collect Static Files:
```bash
python manage.py collectstatic
```''',
            'content_fa': '''جنگو را برای استقرار production پیکربندی کنید.

تنظیمات کلیدی:
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# پایگاه داده (PostgreSQL توصیه می‌شود)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# فایل‌های static
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# امنیت
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

جمع‌آوری فایل‌های Static:
```bash
python manage.py collectstatic
```''',
            'code_example': '''# settings.py
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
    }
}

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Collect static files
# python manage.py collectstatic''',
            'code_example_windows': '''# settings.py
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Collect static
python manage.py collectstatic --noinput''',
            'code_example_mac': '''# settings.py
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Collect static
python manage.py collectstatic --noinput''',
            'exercise_en': 'Configure production settings: set DEBUG=False, configure ALLOWED_HOSTS, and set up environment variables for SECRET_KEY.',
            'exercise_fa': 'تنظیمات production را پیکربندی کنید: DEBUG=False تنظیم کنید، ALLOWED_HOSTS را پیکربندی کنید و متغیرهای محیطی برای SECRET_KEY تنظیم کنید.',
            'exercise_solution': '''# settings.py
import os

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Set environment variable
# export SECRET_KEY='your-secret-key-here' ''',
            'order': 1
        }
    ]
}

