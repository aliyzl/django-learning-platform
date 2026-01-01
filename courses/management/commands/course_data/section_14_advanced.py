"""
Section 14: Advanced Topics
Advanced Django features and techniques
"""

SECTION_DATA = {
    'slug': 'advanced',
    'title_en': 'Advanced Topics',
    'title_fa': 'موضوعات پیشرفته',
    'description_en': 'Advanced Django features: middleware, signals, custom commands',
    'description_fa': 'ویژگی‌های پیشرفته جنگو: middleware، signals، دستورات سفارشی',
    'lessons': [
        {
            'slug': 'custom-middleware',
            'title_en': 'Custom Middleware',
            'title_fa': 'Middleware سفارشی',
            'content_en': '''Middleware is a framework of hooks into Django's request/response processing.

Creating Middleware:
```python
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Code executed before view
        response = self.get_response(request)
        # Code executed after view
        return response
```

Registering Middleware:
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'myapp.middleware.CustomMiddleware',
    ...
]
```

Middleware Methods:
- process_request(request): Called before view
- process_response(request, response): Called after view
- process_exception(request, exception): Called on exception''',
            'content_fa': '''Middleware یک فریمورک از hooks در پردازش درخواست/پاسخ جنگو است.

ایجاد Middleware:
```python
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # کد اجرا شده قبل از view
        response = self.get_response(request)
        # کد اجرا شده بعد از view
        return response
```

ثبت Middleware:
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'myapp.middleware.CustomMiddleware',
    ...
]
```

متدهای Middleware:
- process_request(request): قبل از view فراخوانی می‌شود
- process_response(request, response): بعد از view فراخوانی می‌شود
- process_exception(request, exception): در صورت استثنا فراخوانی می‌شود''',
            'code_example': '''# middleware.py
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Before view
        print(f"Request: {request.path}")
        response = self.get_response(request)
        # After view
        return response

# settings.py
MIDDLEWARE = [
    'myapp.middleware.CustomMiddleware',
]''',
            'code_example_windows': '''# Create middleware.py
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print(f"Request: {request.path}")
        response = self.get_response(request)
        return response

# Add to settings.py MIDDLEWARE list''',
            'code_example_mac': '''# Create middleware.py
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print(f"Request: {request.path}")
        response = self.get_response(request)
        return response

# Add to settings.py MIDDLEWARE list''',
            'exercise_en': 'Create a custom middleware that logs the request path to the console.',
            'exercise_fa': 'یک middleware سفارشی ایجاد کنید که مسیر درخواست را در کنسول لاگ می‌کند.',
            'exercise_solution': '''# middleware.py
class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print(f"Request path: {request.path}")
        response = self.get_response(request)
        return response

# Add to MIDDLEWARE in settings.py''',
            'order': 1
        },
        {
            'slug': 'signals',
            'title_en': 'Signals',
            'title_fa': 'Signals',
            'content_en': '''Signals allow decoupled applications to get notified when certain actions occur.

Common Signals:
- pre_save, post_save: Before/after model save
- pre_delete, post_delete: Before/after model delete
- request_started, request_finished: Request lifecycle

Example:
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")
    else:
        print(f"Post updated: {instance.title}")
```''',
            'content_fa': '''Signals به برنامه‌های جدا شده امکان می‌دهند هنگام رخ دادن اقدامات خاص مطلع شوند.

Signals رایج:
- pre_save، post_save: قبل/بعد از ذخیره مدل
- pre_delete، post_delete: قبل/بعد از حذف مدل
- request_started، request_finished: چرخه زندگی درخواست

مثال:
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"پست جدید ایجاد شد: {instance.title}")
    else:
        print(f"پست به‌روزرسانی شد: {instance.title}")
```''',
            'code_example': '''from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New post: {instance.title}")''',
            'code_example_windows': '''# In signals.py or models.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")''',
            'code_example_mac': '''# In signals.py or models.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")''',
            'exercise_en': 'Create a signal that prints a message when a new Post is created.',
            'exercise_fa': 'یک signal ایجاد کنید که هنگام ایجاد یک Post جدید پیامی چاپ می‌کند.',
            'exercise_solution': '''from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def post_created(sender, instance, created, **kwargs):
    if created:
        print(f"New post created: {instance.title}")''',
            'order': 2
        },
        {
            'slug': 'custom-commands',
            'title_en': 'Custom Management Commands',
            'title_fa': 'دستورات مدیریتی سفارشی',
            'content_en': '''Create custom management commands for your Django app.

Structure:
```
myapp/
    management/
        __init__.py
        commands/
            __init__.py
            mycommand.py
```

Command Example:
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Description of command'
    
    def add_arguments(self, parser):
        parser.add_argument('--option', type=str)
    
    def handle(self, *args, **options):
        self.stdout.write('Command executed')
```

Usage:
```bash
python manage.py mycommand
python manage.py mycommand --option value
```''',
            'content_fa': '''ایجاد دستورات مدیریتی سفارشی برای برنامه جنگو شما.

ساختار:
```
myapp/
    management/
        __init__.py
        commands/
            __init__.py
            mycommand.py
```

مثال دستور:
```python
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'توضیحات دستور'
    
    def add_arguments(self, parser):
        parser.add_argument('--option', type=str)
    
    def handle(self, *args, **options):
        self.stdout.write('دستور اجرا شد')
```

استفاده:
```bash
python manage.py mycommand
python manage.py mycommand --option value
```''',
            'code_example': '''# management/commands/mycommand.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'My custom command'
    
    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='Name argument')
    
    def handle(self, *args, **options):
        name = options['name']
        self.stdout.write(f'Hello, {name}!')''',
            'code_example_windows': '''# Create directory structure:
# myapp/management/commands/mycommand.py

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Custom command'
    
    def handle(self, *args, **options):
        self.stdout.write('Command executed')

# Run: python manage.py mycommand''',
            'code_example_mac': '''# Create directory structure:
# myapp/management/commands/mycommand.py

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Custom command'
    
    def handle(self, *args, **options):
        self.stdout.write('Command executed')

# Run: python manage.py mycommand''',
            'exercise_en': 'Create a custom management command that prints "Hello, Django!" when executed.',
            'exercise_fa': 'یک دستور مدیریتی سفارشی ایجاد کنید که هنگام اجرا "Hello, Django!" را چاپ می‌کند.',
            'exercise_solution': '''# management/commands/hello.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints hello message'
    
    def handle(self, *args, **options):
        self.stdout.write('Hello, Django!')''',
            'order': 3
        }
    ]
}

