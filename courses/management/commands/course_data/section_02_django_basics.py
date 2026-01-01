"""
Section 2: Django Basics
Fundamental Django concepts: apps, models, views, URLs, templates, admin
"""

SECTION_DATA = {
    'slug': 'django-basics',
    'title_en': 'Django Basics',
    'title_fa': 'مبانی جنگو',
    'description_en': 'Learn the fundamentals of Django: projects, apps, models, views, URLs, templates, and admin',
    'description_fa': 'اصول جنگو را بیاموزید: پروژه‌ها، برنامه‌ها، مدل‌ها، viewها، URLها، قالب‌ها و admin',
    'lessons': [
        {
            'slug': 'django-apps',
            'title_en': 'Understanding Django Apps',
            'title_fa': 'درک برنامه‌های جنگو',
            'content_en': '''A Django app is a Python package that contains related functionality. A project can contain multiple apps, and each app can be reused in other projects.

Key Concepts:
- App: A web application that does something specific (blog, polls, e-commerce)
- Project: A collection of configuration and apps for a particular website
- A project can contain multiple apps
- An app can be in multiple projects
- Apps should be focused on a single purpose

Creating an App:
- Command: python manage.py startapp appname
- This creates a directory with:
  * models.py: Database models
  * views.py: View functions/classes
  * admin.py: Admin configuration
  * apps.py: App configuration
  * tests.py: Test cases
  * urls.py: URL routing (created manually)

App Structure:
- Each app is self-contained
- Apps can have their own models, views, templates, static files
- Apps should be reusable and focused

Registering Apps:
- Add app name to INSTALLED_APPS in settings.py
- Format: 'appname' or 'appname.apps.AppnameConfig'

Best Practices:
- Use descriptive app names
- Keep apps focused on single responsibility
- Make apps reusable
- Organize related functionality together''',
            'content_fa': '''یک برنامه جنگو یک بسته پایتون است که شامل عملکردهای مرتبط است. یک پروژه می‌تواند شامل چندین برنامه باشد و هر برنامه می‌تواند در پروژه‌های دیگر استفاده مجدد شود.

مفاهیم کلیدی:
- برنامه: یک برنامه وب که کاری خاص انجام می‌دهد (وبلاگ، نظرسنجی، تجارت الکترونیک)
- پروژه: مجموعه‌ای از پیکربندی و برنامه‌ها برای یک وب‌سایت خاص
- یک پروژه می‌تواند شامل چندین برنامه باشد
- یک برنامه می‌تواند در چندین پروژه باشد
- برنامه‌ها باید روی یک هدف واحد متمرکز باشند

ایجاد یک برنامه:
- دستور: python manage.py startapp appname
- این یک دایرکتوری با موارد زیر ایجاد می‌کند:
  * models.py: مدل‌های پایگاه داده
  * views.py: توابع/کلاس‌های view
  * admin.py: پیکربندی admin
  * apps.py: پیکربندی برنامه
  * tests.py: موارد تست
  * urls.py: مسیریابی URL (به صورت دستی ایجاد می‌شود)

ساختار برنامه:
- هر برنامه خودکفا است
- برنامه‌ها می‌توانند مدل‌ها، viewها، قالب‌ها، فایل‌های static خود را داشته باشند
- برنامه‌ها باید قابل استفاده مجدد و متمرکز باشند

ثبت برنامه‌ها:
- نام برنامه را به INSTALLED_APPS در settings.py اضافه کنید
- فرمت: 'appname' یا 'appname.apps.AppnameConfig'

بهترین روش‌ها:
- از نام‌های توصیفی برای برنامه استفاده کنید
- برنامه‌ها را روی مسئولیت واحد متمرکز نگه دارید
- برنامه‌ها را قابل استفاده مجدد کنید
- عملکردهای مرتبط را با هم سازماندهی کنید''',
            'code_example': 'python manage.py startapp myapp',
            'code_example_windows': '''# Create app
python manage.py startapp myapp

# View app structure
dir myapp

# Don't forget to add it to INSTALLED_APPS in settings.py:
# INSTALLED_APPS = [
#     ...
#     'myapp',
# ]''',
            'code_example_mac': '''# Create app
python manage.py startapp myapp

# View app structure
ls -la myapp

# Don't forget to add it to INSTALLED_APPS in settings.py:
# INSTALLED_APPS = [
#     ...
#     'myapp',
# ]''',
            'exercise_en': 'Create an app named "posts" in your Django project and register it in INSTALLED_APPS.',
            'exercise_fa': 'یک برنامه با نام "posts" در پروژه جنگو خود ایجاد کنید و آن را در INSTALLED_APPS ثبت کنید.',
            'exercise_solution': '''# Step 1: Create app
python manage.py startapp posts

# Step 2: Add to settings.py INSTALLED_APPS:
# 'posts',''',
            'order': 1
        },
        {
            'slug': 'models-introduction',
            'title_en': 'Introduction to Models',
            'title_fa': 'معرفی مدل‌ها',
            'content_en': '''Models are Python classes that define the structure of your database. Django uses an ORM (Object-Relational Mapping) to interact with databases.

Key Concepts:
- Model: A Python class that represents a database table
- Field: An attribute of a model that represents a database column
- Instance: A specific row in the database table
- ORM: Maps Python objects to database tables

Model Benefits:
- Write Python code instead of SQL
- Database-agnostic (works with PostgreSQL, MySQL, SQLite, etc.)
- Automatic migrations
- Built-in validation
- Admin interface integration

Basic Model Example:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Model Fields:
- CharField: Short text (requires max_length)
- TextField: Long text
- IntegerField: Integer numbers
- BooleanField: True/False
- DateTimeField: Date and time
- EmailField: Email address
- URLField: URL
- ForeignKey: Relationship to another model
- ManyToManyField: Many-to-many relationship

After creating models:
1. Create migrations: python manage.py makemigrations
2. Apply migrations: python manage.py migrate''',
            'content_fa': '''مدل‌ها کلاس‌های پایتون هستند که ساختار پایگاه داده شما را تعریف می‌کنند. جنگو از ORM (Object-Relational Mapping) برای تعامل با پایگاه‌های داده استفاده می‌کند.

مفاهیم کلیدی:
- مدل: یک کلاس پایتون که یک جدول پایگاه داده را نشان می‌دهد
- فیلد: یک ویژگی از یک مدل که یک ستون پایگاه داده را نشان می‌دهد
- نمونه: یک ردیف خاص در جدول پایگاه داده
- ORM: اشیاء پایتون را به جداول پایگاه داده نگاشت می‌کند

مزایای مدل:
- نوشتن کد پایتون به جای SQL
- مستقل از پایگاه داده (با PostgreSQL، MySQL، SQLite و غیره کار می‌کند)
- migrations خودکار
- اعتبارسنجی داخلی
- یکپارچه‌سازی رابط admin

مثال مدل پایه:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

فیلدهای مدل:
- CharField: متن کوتاه (نیاز به max_length دارد)
- TextField: متن طولانی
- IntegerField: اعداد صحیح
- BooleanField: True/False
- DateTimeField: تاریخ و زمان
- EmailField: آدرس ایمیل
- URLField: URL
- ForeignKey: رابطه با مدل دیگر
- ManyToManyField: رابطه چند به چند

پس از ایجاد مدل‌ها:
1. ایجاد migrations: python manage.py makemigrations
2. اعمال migrations: python manage.py migrate''',
            'code_example': '''from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title''',
            'code_example_windows': '''# In your app's models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Then create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'code_example_mac': '''# In your app's models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Then create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'exercise_en': 'Create a Book model with fields: title (CharField), author (CharField), published_date (DateField), and isbn (CharField with max_length=13).',
            'exercise_fa': 'یک مدل Book با فیلدهای زیر ایجاد کنید: title (CharField)، author (CharField)، published_date (DateField)، و isbn (CharField با max_length=13).',
            'exercise_solution': '''from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    
    def __str__(self):
        return self.title''',
            'order': 2
        },
        {
            'slug': 'views-introduction',
            'title_en': 'Introduction to Views',
            'title_fa': 'معرفی Viewها',
            'content_en': '''Views are Python functions or classes that receive web requests and return web responses. They contain the logic that processes requests and returns appropriate responses.

Types of Views:
1. Function-Based Views (FBV): Simple Python functions
2. Class-Based Views (CBV): Python classes with methods

Function-Based View Example:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

View Responsibilities:
- Process HTTP requests
- Interact with models to get data
- Render templates with data
- Return HTTP responses

Request Object:
- Contains information about the request
- request.method: HTTP method (GET, POST, etc.)
- request.GET: GET parameters
- request.POST: POST parameters
- request.user: Current user

Response Types:
- HttpResponse: Basic response
- JsonResponse: JSON response
- HttpResponseRedirect: Redirect response
- render(): Render template with context

View Decorators:
- @login_required: Require authentication
- @csrf_exempt: Disable CSRF protection
- @require_http_methods: Restrict HTTP methods''',
            'content_fa': '''Viewها توابع یا کلاس‌های پایتون هستند که درخواست‌های وب را دریافت می‌کنند و پاسخ‌های وب را برمی‌گردانند. آنها شامل منطقی هستند که درخواست‌ها را پردازش می‌کند و پاسخ‌های مناسب را برمی‌گرداند.

انواع Viewها:
1. Function-Based Views (FBV): توابع ساده پایتون
2. Class-Based Views (CBV): کلاس‌های پایتون با متدها

مثال Function-Based View:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

مسئولیت‌های View:
- پردازش درخواست‌های HTTP
- تعامل با مدل‌ها برای دریافت داده
- رندر کردن قالب‌ها با داده
- برگرداندن پاسخ‌های HTTP

شیء Request:
- شامل اطلاعاتی درباره درخواست است
- request.method: متد HTTP (GET، POST و غیره)
- request.GET: پارامترهای GET
- request.POST: پارامترهای POST
- request.user: کاربر فعلی

انواع Response:
- HttpResponse: پاسخ پایه
- JsonResponse: پاسخ JSON
- HttpResponseRedirect: پاسخ redirect
- render(): رندر کردن قالب با context

دکوراتورهای View:
- @login_required: نیاز به احراز هویت
- @csrf_exempt: غیرفعال کردن محافظت CSRF
- @require_http_methods: محدود کردن متدهای HTTP''',
            'code_example': '''from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, World!")

def home(request):
    context = {'message': 'Welcome to Django!'}
    return render(request, 'home.html', context)''',
            'code_example_windows': '''# In your app's views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, World!")

def home(request):
    context = {'message': 'Welcome to Django!'}
    return render(request, 'home.html', context)''',
            'code_example_mac': '''# In your app's views.py
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, World!")

def home(request):
    context = {'message': 'Welcome to Django!'}
    return render(request, 'home.html', context)''',
            'exercise_en': 'Create a view function called "about" that returns an HttpResponse with the text "About Us".',
            'exercise_fa': 'یک تابع view با نام "about" ایجاد کنید که یک HttpResponse با متن "About Us" برمی‌گرداند.',
            'exercise_solution': '''from django.http import HttpResponse

def about(request):
    return HttpResponse("About Us")''',
            'order': 3
        },
        {
            'slug': 'url-configuration',
            'title_en': 'URL Configuration',
            'title_fa': 'پیکربندی URL',
            'content_en': '''URL configuration maps URLs to views. Django uses URL patterns to route requests to the appropriate view functions.

URL Configuration Files:
- Root urls.py: Main URL configuration (in project directory)
- App urls.py: App-specific URLs (create manually in each app)

Basic URL Pattern:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

URL Patterns:
- path(route, view, name): Simple URL pattern
- route: URL pattern (string)
- view: View function or class
- name: URL name for reverse lookup

URL Parameters:
- Capture values from URL: path('post/<int:id>/', views.post_detail)
- Types: str, int, slug, uuid, path

Including Other URL Configs:
- Use include() to include app URLs:
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

URL Names:
- Give URLs names for reverse lookup
- Use in templates: {% url 'name' %}
- Use in views: reverse('name')
- Use in redirects: redirect('name')''',
            'content_fa': '''پیکربندی URL، URLها را به viewها نگاشت می‌کند. جنگو از الگوهای URL برای مسیریابی درخواست‌ها به توابع view مناسب استفاده می‌کند.

فایل‌های پیکربندی URL:
- urls.py ریشه: پیکربندی URL اصلی (در دایرکتوری پروژه)
- urls.py برنامه: URLهای خاص برنامه (به صورت دستی در هر برنامه ایجاد کنید)

الگوی URL پایه:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

الگوهای URL:
- path(route, view, name): الگوی URL ساده
- route: الگوی URL (رشته)
- view: تابع یا کلاس view
- name: نام URL برای جستجوی معکوس

پارامترهای URL:
- گرفتن مقادیر از URL: path('post/<int:id>/', views.post_detail)
- انواع: str، int، slug، uuid، path

شامل کردن پیکربندی‌های URL دیگر:
- استفاده از include() برای شامل کردن URLهای برنامه:
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

نام‌های URL:
- به URLها نام بدهید برای جستجوی معکوس
- استفاده در قالب‌ها: {% url 'name' %}
- استفاده در viewها: reverse('name')
- استفاده در redirectها: redirect('name')''',
            'code_example': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]''',
            'code_example_windows': '''# In your app's urls.py (create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]

# In project's urls.py, include app URLs:
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]''',
            'code_example_mac': '''# In your app's urls.py (create this file)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
]

# In project's urls.py, include app URLs:
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]''',
            'exercise_en': 'Create a URL pattern that maps "/products/<product_id>/" to a view called "product_detail" with the name "product_detail".',
            'exercise_fa': 'یک الگوی URL ایجاد کنید که "/products/<product_id>/" را به یک view با نام "product_detail" با نام "product_detail" نگاشت می‌کند.',
            'exercise_solution': '''from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]''',
            'order': 4
        },
        {
            'slug': 'templates-basics',
            'title_en': 'Templates Basics',
            'title_fa': 'مبانی قالب‌ها',
            'content_en': '''Templates are HTML files with Django template syntax. They separate presentation from logic.

Template Location:
- Create a 'templates' directory in your app
- Django looks for templates in app directories and project-level templates

Basic Template:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

Template Syntax:
- {{ variable }}: Display variable value
- {% tag %}: Template tag (logic)
- {# comment #}: Template comment

Common Template Tags:
- {% if %}: Conditional logic
- {% for %}: Loop through items
- {% block %}: Define block for inheritance
- {% extends %}: Extend base template
- {% include %}: Include another template
- {% url %}: Generate URL from name
- {% load %}: Load template tags/filters

Rendering Templates:
```python
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Welcome',
        'content': 'Hello, World!'
    }
    return render(request, 'index.html', context)
```

Template Inheritance:
- Create base.html with common structure
- Use {% block %} to define replaceable sections
- Child templates extend base and fill blocks''',
            'content_fa': '''قالب‌ها فایل‌های HTML با سینتکس قالب جنگو هستند. آنها ارائه را از منطق جدا می‌کنند.

موقعیت قالب:
- یک دایرکتوری 'templates' در برنامه خود ایجاد کنید
- جنگو قالب‌ها را در دایرکتوری‌های برنامه و قالب‌های سطح پروژه جستجو می‌کند

قالب پایه:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

سینتکس قالب:
- {{ variable }}: نمایش مقدار متغیر
- {% tag %}: تگ قالب (منطق)
- {# comment #}: نظر قالب

تگ‌های قالب رایج:
- {% if %}: منطق شرطی
- {% for %}: حلقه از طریق آیتم‌ها
- {% block %}: تعریف بلوک برای وراثت
- {% extends %}: گسترش قالب پایه
- {% include %}: شامل کردن قالب دیگر
- {% url %}: تولید URL از نام
- {% load %}: بارگذاری تگ‌ها/فیلترهای قالب

رندر کردن قالب‌ها:
```python
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Welcome',
        'content': 'Hello, World!'
    }
    return render(request, 'index.html', context)
```

وراثت قالب:
- ایجاد base.html با ساختار مشترک
- استفاده از {% block %} برای تعریف بخش‌های قابل جایگزینی
- قالب‌های فرزند base را گسترش می‌دهند و بلوک‌ها را پر می‌کنند''',
            'code_example': '''<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>''',
            'code_example_windows': '''# Create templates directory in your app
# myapp/templates/index.html

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>

# In views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Welcome',
        'content': 'Hello, World!'
    }
    return render(request, 'index.html', context)''',
            'code_example_mac': '''# Create templates directory in your app
# myapp/templates/index.html

<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>

# In views.py
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'heading': 'Welcome',
        'content': 'Hello, World!'
    }
    return render(request, 'index.html', context)''',
            'exercise_en': 'Create a template called "about.html" that displays a title and description passed from the view.',
            'exercise_fa': 'یک قالب با نام "about.html" ایجاد کنید که عنوان و توضیحات ارسال شده از view را نمایش می‌دهد.',
            'exercise_solution': '''<!-- templates/about.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
</body>
</html>''',
            'order': 5
        },
        {
            'slug': 'django-admin',
            'title_en': 'The Django Admin',
            'title_fa': 'Django Admin',
            'content_en': '''Django provides a powerful admin interface for managing your application's data. It's automatically generated from your models.

Creating Admin User:
- Command: python manage.py createsuperuser
- Enter username, email, and password
- Access admin at: http://127.0.0.1:8000/admin/

Registering Models:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Admin Features:
- Automatic interface generation
- User authentication and permissions
- CRUD operations (Create, Read, Update, Delete)
- Search and filtering
- Customizable display

Customizing Admin:
- Customize list display
- Add filters
- Add search fields
- Customize forms
- Add actions

Admin Class Example:
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
```

Admin URLs:
- Admin interface: /admin/
- Login: /admin/login/
- Logout: /admin/logout/''',
            'content_fa': '''جنگو یک رابط admin قدرتمند برای مدیریت داده‌های برنامه شما ارائه می‌دهد. به طور خودکار از مدل‌های شما تولید می‌شود.

ایجاد کاربر Admin:
- دستور: python manage.py createsuperuser
- نام کاربری، ایمیل و رمز عبور را وارد کنید
- دسترسی به admin در: http://127.0.0.1:8000/admin/

ثبت مدل‌ها:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

ویژگی‌های Admin:
- تولید خودکار رابط
- احراز هویت و مجوزهای کاربر
- عملیات CRUD (ایجاد، خواندن، به‌روزرسانی، حذف)
- جستجو و فیلتر
- قابل تنظیم نمایش

سفارشی‌سازی Admin:
- سفارشی‌سازی نمایش لیست
- افزودن فیلترها
- افزودن فیلدهای جستجو
- سفارشی‌سازی فرم‌ها
- افزودن اقدامات

مثال کلاس Admin:
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['title', 'content']
```

URLهای Admin:
- رابط admin: /admin/
- ورود: /admin/login/
- خروج: /admin/logout/''',
            'code_example': '''from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['title', 'content']''',
            'code_example_windows': '''# Create superuser
python manage.py createsuperuser

# In admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

# Access admin at http://127.0.0.1:8000/admin/''',
            'code_example_mac': '''# Create superuser
python manage.py createsuperuser

# In admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

# Access admin at http://127.0.0.1:8000/admin/''',
            'exercise_en': 'Create a superuser, register your Post model in admin, and customize the admin to show title, created_at, and author in the list display.',
            'exercise_fa': 'یک superuser ایجاد کنید، مدل Post خود را در admin ثبت کنید و admin را سفارشی کنید تا title، created_at و author را در نمایش لیست نشان دهد.',
            'exercise_solution': '''# Step 1: Create superuser
python manage.py createsuperuser

# Step 2: In admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'author']''',
            'order': 6
        }
    ]
}

