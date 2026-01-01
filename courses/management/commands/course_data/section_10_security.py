"""
Section 10: Security
Security best practices in Django
"""

SECTION_DATA = {
    'slug': 'security',
    'title_en': 'Security',
    'title_fa': 'امنیت',
    'description_en': 'Security best practices and protection in Django',
    'description_fa': 'بهترین روش‌های امنیتی و محافظت در جنگو',
    'lessons': [
        {
            'slug': 'csrf-protection',
            'title_en': 'CSRF Protection',
            'title_fa': 'محافظت CSRF',
            'content_en': '''Django provides CSRF protection by default.

In Templates:
```html
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
```

In AJAX:
```javascript
// Get CSRF token
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Include in request
fetch('/api/endpoint/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrfToken
    }
});
```

Exempting Views:
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    # CSRF protection disabled
    pass
```''',
            'content_fa': '''جنگو به طور پیش‌فرض محافظت CSRF ارائه می‌دهد.

در قالب‌ها:
```html
<form method="post">
    {% csrf_token %}
    <!-- فیلدهای فرم -->
</form>
```

در AJAX:
```javascript
// دریافت توکن CSRF
const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// شامل در درخواست
fetch('/api/endpoint/', {
    method: 'POST',
    headers: {
        'X-CSRFToken': csrfToken
    }
});
```

معاف کردن Viewها:
```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    # محافظت CSRF غیرفعال شده
    pass
```''',
            'code_example': '''# In template
<form method="post">
    {% csrf_token %}
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>

# In views.py (if needed to exempt)
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_view(request):
    # Handle request
    pass''',
            'code_example_windows': '''# Always include CSRF token in forms
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

# For AJAX requests, get token from cookie or form''',
            'code_example_mac': '''# Always include CSRF token in forms
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

# For AJAX requests, get token from cookie or form''',
            'exercise_en': 'Create a form template that includes CSRF protection.',
            'exercise_fa': 'یک قالب فرم ایجاد کنید که شامل محافظت CSRF است.',
            'exercise_solution': '''<form method="post">
    {% csrf_token %}
    <input type="text" name="name">
    <button type="submit">Submit</button>
</form>''',
            'order': 1
        },
        {
            'slug': 'security-best-practices',
            'title_en': 'Security Best Practices',
            'title_fa': 'بهترین روش‌های امنیتی',
            'content_en': '''Key security practices for Django applications:

1. Keep SECRET_KEY secret
2. Set DEBUG=False in production
3. Use ALLOWED_HOSTS
4. Use HTTPS in production
5. Keep dependencies updated
6. Validate all user input
7. Use parameterized queries (Django ORM does this)
8. Hash passwords (Django does this automatically)
9. Use CSRF protection (enabled by default)
10. Set secure cookie flags in production''',
            'content_fa': '''روش‌های امنیتی کلیدی برای برنامه‌های جنگو:

1. SECRET_KEY را مخفی نگه دارید
2. DEBUG=False را در production تنظیم کنید
3. از ALLOWED_HOSTS استفاده کنید
4. از HTTPS در production استفاده کنید
5. وابستگی‌ها را به‌روز نگه دارید
6. تمام ورودی‌های کاربر را اعتبارسنجی کنید
7. از کوئری‌های پارامتری استفاده کنید (Django ORM این کار را می‌کند)
8. رمزهای عبور را hash کنید (جنگو این کار را به طور خودکار انجام می‌دهد)
9. از محافظت CSRF استفاده کنید (به طور پیش‌فرض فعال است)
10. پرچم‌های cookie امن را در production تنظیم کنید''',
            'code_example': '''# settings.py (production)
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True''',
            'code_example_windows': '''# settings.py for production
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')''',
            'code_example_mac': '''# settings.py for production
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')''',
            'exercise_en': 'Configure production security settings: set DEBUG=False and configure ALLOWED_HOSTS.',
            'exercise_fa': 'تنظیمات امنیتی production را پیکربندی کنید: DEBUG=False تنظیم کنید و ALLOWED_HOSTS را پیکربندی کنید.',
            'exercise_solution': '''# settings.py
import os

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')''',
            'order': 2
        }
    ]
}

