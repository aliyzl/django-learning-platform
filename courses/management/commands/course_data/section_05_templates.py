"""
Section 5: Templates
Template syntax, inheritance, tags, filters, and best practices
"""

SECTION_DATA = {
    'slug': 'templates',
    'title_en': 'Templates',
    'title_fa': 'قالب‌ها',
    'description_en': 'Master Django template system: syntax, inheritance, tags, and filters',
    'description_fa': 'تسلط بر سیستم قالب جنگو: سینتکس، وراثت، تگ‌ها و فیلترها',
    'lessons': [
        {
            'slug': 'template-syntax',
            'title_en': 'Template Syntax',
            'title_fa': 'سینتکس قالب',
            'content_en': '''Django templates use a special syntax to insert dynamic content into HTML.

Variables:
- {{ variable }}: Display variable value
- {{ object.attribute }}: Access object attributes
- {{ object.method }}: Call methods (no arguments)

Filters:
- {{ variable|filter }}: Apply filter to variable
- {{ variable|filter:"arg" }}: Filter with argument
- Common filters: upper, lower, length, date, truncatewords

Tags:
- {% tag %}: Template tag for logic
- {% if %}: Conditional statements
- {% for %}: Loops
- {% block %}: Define blocks
- {% extends %}: Template inheritance

Comments:
- {# comment #}: Template comments (not in HTML)

Example:
```html
<h1>{{ post.title|upper }}</h1>
<p>{{ post.content|truncatewords:30 }}</p>
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% endif %}
```''',
            'content_fa': '''قالب‌های جنگو از سینتکس خاصی برای درج محتوای پویا در HTML استفاده می‌کنند.

متغیرها:
- {{ variable }}: نمایش مقدار متغیر
- {{ object.attribute }}: دسترسی به ویژگی‌های شیء
- {{ object.method }}: فراخوانی متدها (بدون آرگومان)

فیلترها:
- {{ variable|filter }}: اعمال فیلتر به متغیر
- {{ variable|filter:"arg" }}: فیلتر با آرگومان
- فیلترهای رایج: upper، lower، length، date، truncatewords

تگ‌ها:
- {% tag %}: تگ قالب برای منطق
- {% if %}: دستورات شرطی
- {% for %}: حلقه‌ها
- {% block %}: تعریف بلوک‌ها
- {% extends %}: وراثت قالب

نظرات:
- {# comment #}: نظرات قالب (در HTML نیست)

مثال:
```html
<h1>{{ post.title|upper }}</h1>
<p>{{ post.content|truncatewords:30 }}</p>
{% if user.is_authenticated %}
    <p>خوش آمدید، {{ user.username }}!</p>
{% endif %}
```''',
            'code_example': '''<!-- templates/post_detail.html -->
<h1>{{ post.title|upper }}</h1>
<p>Published: {{ post.created_at|date:"F d, Y" }}</p>
<p>{{ post.content|truncatewords:30 }}</p>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please <a href="/login/">login</a></p>
{% endif %}''',
            'code_example_windows': '''# Create templates/post_detail.html
<h1>{{ post.title|upper }}</h1>
<p>Published: {{ post.created_at|date:"F d, Y" }}</p>
<p>{{ post.content|truncatewords:30 }}</p>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please <a href="/login/">login</a></p>
{% endif %}

# In views.py
from django.shortcuts import render
from .models import Post

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})''',
            'code_example_mac': '''# Create templates/post_detail.html
<h1>{{ post.title|upper }}</h1>
<p>Published: {{ post.created_at|date:"F d, Y" }}</p>
<p>{{ post.content|truncatewords:30 }}</p>

{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please <a href="/login/">login</a></p>
{% endif %}

# In views.py
from django.shortcuts import render
from .models import Post

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})''',
            'exercise_en': 'Create a template that displays a product name in uppercase, price formatted to 2 decimal places, and shows "In Stock" if in_stock is True.',
            'exercise_fa': 'یک قالب ایجاد کنید که نام محصول را با حروف بزرگ نمایش می‌دهد، قیمت را با 2 رقم اعشار فرمت می‌کند و "موجود" را اگر in_stock True باشد نشان می‌دهد.',
            'exercise_solution': '''<h1>{{ product.name|upper }}</h1>
<p>Price: ${{ product.price|floatformat:2 }}</p>
{% if product.in_stock %}
    <p>In Stock</p>
{% endif %}''',
            'order': 1
        },
        {
            'slug': 'template-inheritance',
            'title_en': 'Template Inheritance',
            'title_fa': 'وراثت قالب',
            'content_en': '''Template inheritance allows you to create a base template and extend it in child templates.

Base Template (base.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>{% block header %}{% endblock %}</header>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% block footer %}{% endblock %}</footer>
</body>
</html>
```

Child Template:
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome</h1>
<p>This is the home page.</p>
{% endblock %}
```

Benefits:
- DRY (Don't Repeat Yourself)
- Consistent layout
- Easy maintenance
- Reusable components

Block Names:
- Can use any name
- Can have multiple blocks
- Blocks can have default content
- Child templates override parent blocks''',
            'content_fa': '''وراثت قالب به شما امکان می‌دهد یک قالب پایه ایجاد کنید و آن را در قالب‌های فرزند گسترش دهید.

قالب پایه (base.html):
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}سایت من{% endblock %}</title>
</head>
<body>
    <header>{% block header %}{% endblock %}</header>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% block footer %}{% endblock %}</footer>
</body>
</html>
```

قالب فرزند:
```html
{% extends "base.html" %}

{% block title %}صفحه اصلی{% endblock %}

{% block content %}
<h1>خوش آمدید</h1>
<p>این صفحه اصلی است.</p>
{% endblock %}
```

مزایا:
- DRY (خود را تکرار نکنید)
- چیدمان یکنواخت
- نگهداری آسان
- کامپوننت‌های قابل استفاده مجدد

نام‌های بلوک:
- می‌توانید از هر نامی استفاده کنید
- می‌توانید چندین بلوک داشته باشید
- بلوک‌ها می‌توانند محتوای پیش‌فرض داشته باشند
- قالب‌های فرزند بلوک‌های والد را override می‌کنند''',
            'code_example': '''<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <nav>{% block nav %}{% endblock %}</nav>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% block footer %}{% endblock %}</footer>
    {% block extra_js %}{% endblock %}
</body>
</html>

<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
<h1>Welcome</h1>
<p>This is the home page.</p>
{% endblock %}''',
            'code_example_windows': '''# Create templates/base.html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>{% block nav %}{% endblock %}</nav>
    <main>{% block content %}{% endblock %}</main>
</body>
</html>

# Create templates/home.html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Welcome</h1>
{% endblock %}''',
            'code_example_mac': '''# Create templates/base.html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <nav>{% block nav %}{% endblock %}</nav>
    <main>{% block content %}{% endblock %}</main>
</body>
</html>

# Create templates/home.html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
<h1>Welcome</h1>
{% endblock %}''',
            'exercise_en': 'Create a base template with header, content, and footer blocks. Then create a child template that extends it and fills the content block.',
            'exercise_fa': 'یک قالب پایه با بلوک‌های header، content و footer ایجاد کنید. سپس یک قالب فرزند ایجاد کنید که آن را گسترش می‌دهد و بلوک content را پر می‌کند.',
            'exercise_solution': '''<!-- base.html -->
<!DOCTYPE html>
<html>
<body>
    <header>{% block header %}{% endblock %}</header>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% block footer %}{% endblock %}</footer>
</body>
</html>

<!-- page.html -->
{% extends "base.html" %}
{% block content %}
<h1>Page Content</h1>
{% endblock %}''',
            'order': 2
        },
        {
            'slug': 'template-tags-filters',
            'title_en': 'Template Tags and Filters',
            'title_fa': 'تگ‌ها و فیلترهای قالب',
            'content_en': '''Django provides many built-in template tags and filters.

Common Tags:
- {% if %}: Conditional logic
- {% for %}: Loop through items
- {% with %}: Create temporary variable
- {% url %}: Generate URL from name
- {% load %}: Load template tags/filters
- {% include %}: Include another template
- {% static %}: Generate static file URL
- {% csrf_token %}: CSRF token

Common Filters:
- upper, lower: Case conversion
- length: Get length
- default: Default value if empty
- date: Format date
- time: Format time
- truncatewords: Truncate text
- slice: Slice list/string
- join: Join list items
- add: Add numbers
- cut: Remove substring

Examples:
```html
{% for post in posts %}
    <h2>{{ post.title|upper }}</h2>
    <p>{{ post.content|truncatewords:20 }}</p>
{% empty %}
    <p>No posts available.</p>
{% endfor %}

{% url 'post_detail' post.id as post_url %}
<a href="{{ post_url }}">View Post</a>
```''',
            'content_fa': '''جنگو تگ‌ها و فیلترهای قالب داخلی زیادی ارائه می‌دهد.

تگ‌های رایج:
- {% if %}: منطق شرطی
- {% for %}: حلقه از طریق آیتم‌ها
- {% with %}: ایجاد متغیر موقت
- {% url %}: تولید URL از نام
- {% load %}: بارگذاری تگ‌ها/فیلترهای قالب
- {% include %}: شامل کردن قالب دیگر
- {% static %}: تولید URL فایل static
- {% csrf_token %}: توکن CSRF

فیلترهای رایج:
- upper، lower: تبدیل حروف
- length: دریافت طول
- default: مقدار پیش‌فرض اگر خالی باشد
- date: فرمت تاریخ
- time: فرمت زمان
- truncatewords: کوتاه کردن متن
- slice: برش لیست/رشته
- join: اتصال آیتم‌های لیست
- add: جمع اعداد
- cut: حذف زیررشته

مثال‌ها:
```html
{% for post in posts %}
    <h2>{{ post.title|upper }}</h2>
    <p>{{ post.content|truncatewords:20 }}</p>
{% empty %}
    <p>هیچ پستی در دسترس نیست.</p>
{% endfor %}

{% url 'post_detail' post.id as post_url %}
<a href="{{ post_url }}">مشاهده پست</a>
```''',
            'code_example': '''{% load static %}

{% for post in posts %}
    <article>
        <h2>{{ post.title|upper }}</h2>
        <p>{{ post.content|truncatewords:30|default:"No content" }}</p>
        <p>Published: {{ post.created_at|date:"F d, Y" }}</p>
        <a href="{% url 'post_detail' post.id %}">Read more</a>
    </article>
{% empty %}
    <p>No posts available.</p>
{% endfor %}

<img src="{% static 'images/logo.png' %}" alt="Logo">''',
            'code_example_windows': '''# In template
{% load static %}

{% for post in posts %}
    <article>
        <h2>{{ post.title|upper }}</h2>
        <p>{{ post.content|truncatewords:30 }}</p>
        <a href="{% url 'post_detail' post.id %}">Read more</a>
    </article>
{% empty %}
    <p>No posts available.</p>
{% endfor %}

# Make sure to load static in settings.py
# STATIC_URL = '/static/' ''',
            'code_example_mac': '''# In template
{% load static %}

{% for post in posts %}
    <article>
        <h2>{{ post.title|upper }}</h2>
        <p>{{ post.content|truncatewords:30 }}</p>
        <a href="{% url 'post_detail' post.id %}">Read more</a>
    </article>
{% empty %}
    <p>No posts available.</p>
{% endfor %}

# Make sure to load static in settings.py
# STATIC_URL = '/static/' ''',
            'exercise_en': 'Create a template that loops through a list of products, displays each product name in uppercase, and shows "Out of Stock" if in_stock is False.',
            'exercise_fa': 'یک قالب ایجاد کنید که از لیست محصولات حلقه می‌زند، نام هر محصول را با حروف بزرگ نمایش می‌دهد و "ناموجود" را اگر in_stock False باشد نشان می‌دهد.',
            'exercise_solution': '''{% for product in products %}
    <div>
        <h3>{{ product.name|upper }}</h3>
        {% if not product.in_stock %}
            <p>Out of Stock</p>
        {% endif %}
    </div>
{% endfor %}''',
            'order': 3
        },
        {
            'slug': 'custom-template-tags',
            'title_en': 'Custom Template Tags',
            'title_fa': 'تگ‌های قالب سفارشی',
            'content_en': '''You can create custom template tags for reusable functionality.

Steps:
1. Create templatetags directory in your app
2. Create __init__.py file
3. Create your_tags.py file
4. Register tags using @register decorator

Simple Tag Example:
```python
# myapp/templatetags/my_tags.py
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
```

Usage:
```html
{% load my_tags %}
{% current_time "%Y-%m-%d" %}
```

Inclusion Tag Example:
```python
@register.inclusion_tag('tags/product_card.html')
def product_card(product):
    return {'product': product}
```

Usage:
```html
{% product_card product %}
```''',
            'content_fa': '''می‌توانید تگ‌های قالب سفارشی برای عملکرد قابل استفاده مجدد ایجاد کنید.

مراحل:
1. ایجاد دایرکتوری templatetags در برنامه شما
2. ایجاد فایل __init__.py
3. ایجاد فایل your_tags.py
4. ثبت تگ‌ها با استفاده از دکوراتور @register

مثال تگ ساده:
```python
# myapp/templatetags/my_tags.py
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
```

استفاده:
```html
{% load my_tags %}
{% current_time "%Y-%m-%d" %}
```

مثال تگ Inclusion:
```python
@register.inclusion_tag('tags/product_card.html')
def product_card(product):
    return {'product': product}
```

استفاده:
```html
{% product_card product %}
```''',
            'code_example': '''# myapp/templatetags/my_tags.py
from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

@register.inclusion_tag('tags/product_card.html')
def product_card(product):
    return {'product': product}

# Usage in template:
# {% load my_tags %}
# {% current_time "%Y-%m-%d" %}
# {% product_card product %}''',
            'code_example_windows': '''# Create directory structure:
# myapp/
#   templatetags/
#     __init__.py
#     my_tags.py

# myapp/templatetags/my_tags.py
from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

# In template:
# {% load my_tags %}
# {% current_time "%Y-%m-%d" %}''',
            'code_example_mac': '''# Create directory structure:
# myapp/
#   templatetags/
#     __init__.py
#     my_tags.py

# myapp/templatetags/my_tags.py
from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)

# In template:
# {% load my_tags %}
# {% current_time "%Y-%m-%d" %}''',
            'exercise_en': 'Create a custom template tag called "multiply" that takes two numbers and returns their product.',
            'exercise_fa': 'یک تگ قالب سفارشی با نام "multiply" ایجاد کنید که دو عدد می‌گیرد و حاصلضرب آنها را برمی‌گرداند.',
            'exercise_solution': '''# myapp/templatetags/my_tags.py
from django import template

register = template.Library()

@register.simple_tag
def multiply(a, b):
    return a * b

# Usage: {% multiply 5 3 %}''',
            'order': 4
        },
        {
            'slug': 'static-files',
            'title_en': 'Static Files',
            'title_fa': 'فایل‌های Static',
            'content_en': '''Static files are CSS, JavaScript, images, and other files that don't change dynamically.

Configuration:
```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

Collecting Static Files:
- Development: Django serves static files automatically
- Production: Run `python manage.py collectstatic`

Using Static Files:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/main.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

Static Files Finder:
- Django searches in STATICFILES_DIRS
- Then in each app's static/ directory
- Files are collected to STATIC_ROOT for production''',
            'content_fa': '''فایل‌های static فایل‌های CSS، JavaScript، تصاویر و سایر فایل‌هایی هستند که به صورت پویا تغییر نمی‌کنند.

پیکربندی:
```python
# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

جمع‌آوری فایل‌های Static:
- Development: جنگو به طور خودکار فایل‌های static را سرو می‌کند
- Production: اجرای `python manage.py collectstatic`

استفاده از فایل‌های Static:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/main.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

Static Files Finder:
- جنگو در STATICFILES_DIRS جستجو می‌کند
- سپس در دایرکتوری static/ هر برنامه
- فایل‌ها برای production به STATIC_ROOT جمع‌آوری می‌شوند''',
            'code_example': '''# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# In template
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>''',
            'code_example_windows': '''# Create directory structure:
# myproject/
#   static/
#     css/
#       style.css
#     js/
#       main.js
#     images/
#       logo.png

# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# In template
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">''',
            'code_example_mac': '''# Create directory structure:
# myproject/
#   static/
#     css/
#       style.css
#     js/
#       main.js
#     images/
#       logo.png

# settings.py
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# In template
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">''',
            'exercise_en': 'Configure static files in settings.py and create a template that loads a CSS file from the static directory.',
            'exercise_fa': 'فایل‌های static را در settings.py پیکربندی کنید و یک قالب ایجاد کنید که یک فایل CSS را از دایرکتوری static بارگذاری می‌کند.',
            'exercise_solution': '''# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# In template
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">''',
            'order': 5
        }
    ]
}

