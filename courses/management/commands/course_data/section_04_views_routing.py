"""
Section 4: Views and URL Routing
Function-based views, class-based views, URL patterns, and routing
"""

SECTION_DATA = {
    'slug': 'views-routing',
    'title_en': 'Views and URL Routing',
    'title_fa': 'Viewها و مسیریابی URL',
    'description_en': 'Master Django views, URL routing, and request/response handling',
    'description_fa': 'تسلط بر viewهای جنگو، مسیریابی URL و مدیریت درخواست/پاسخ',
    'lessons': [
        {
            'slug': 'function-based-views',
            'title_en': 'Function-Based Views',
            'title_fa': 'Viewهای مبتنی بر تابع',
            'content_en': '''Function-Based Views (FBVs) are simple Python functions that handle HTTP requests and return HTTP responses.

Basic FBV:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

Request Object:
- request.method: HTTP method (GET, POST, etc.)
- request.GET: GET parameters (query string)
- request.POST: POST parameters (form data)
- request.FILES: Uploaded files
- request.user: Current user
- request.path: Request path
- request.META: HTTP headers

Response Types:
- HttpResponse: Basic response
- JsonResponse: JSON response
- HttpResponseRedirect: Redirect
- render(): Render template
- redirect(): Shortcut for redirect

Example:
```python
from django.shortcuts import render, redirect
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def api_data(request):
    data = {'message': 'Hello'}
    return JsonResponse(data)
```''',
            'content_fa': '''Viewهای مبتنی بر تابع (FBV) توابع ساده پایتون هستند که درخواست‌های HTTP را مدیریت می‌کنند و پاسخ‌های HTTP را برمی‌گردانند.

FBV پایه:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")
```

شیء Request:
- request.method: متد HTTP (GET، POST و غیره)
- request.GET: پارامترهای GET (query string)
- request.POST: پارامترهای POST (داده فرم)
- request.FILES: فایل‌های آپلود شده
- request.user: کاربر فعلی
- request.path: مسیر درخواست
- request.META: هدرهای HTTP

انواع Response:
- HttpResponse: پاسخ پایه
- JsonResponse: پاسخ JSON
- HttpResponseRedirect: Redirect
- render(): رندر کردن قالب
- redirect(): میانبر برای redirect

مثال:
```python
from django.shortcuts import render, redirect
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def api_data(request):
    data = {'message': 'Hello'}
    return JsonResponse(data)
```''',
            'code_example': '''from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

def index(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})''',
            'code_example_windows': '''# In views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

def index(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})''',
            'code_example_mac': '''# In views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post

def index(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})''',
            'exercise_en': 'Create a function-based view called "about" that renders an "about.html" template with a context variable "company_name" set to "Django Corp".',
            'exercise_fa': 'یک view مبتنی بر تابع با نام "about" ایجاد کنید که یک قالب "about.html" را با متغیر context "company_name" تنظیم شده به "Django Corp" رندر می‌کند.',
            'exercise_solution': '''from django.shortcuts import render

def about(request):
    context = {'company_name': 'Django Corp'}
    return render(request, 'about.html', context)''',
            'order': 1
        },
        {
            'slug': 'class-based-views',
            'title_en': 'Class-Based Views',
            'title_fa': 'Viewهای مبتنی بر کلاس',
            'content_en': '''Class-Based Views (CBVs) use Python classes instead of functions. They provide better code reuse and organization.

Basic CBV:
```python
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse("GET request")
    
    def post(self, request):
        return HttpResponse("POST request")
```

Generic Views:
- ListView: Display list of objects
- DetailView: Display single object
- CreateView: Create new object
- UpdateView: Update existing object
- DeleteView: Delete object
- FormView: Display and process form

ListView Example:
```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10
```

DetailView Example:
```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
```''',
            'content_fa': '''Viewهای مبتنی بر کلاس (CBV) از کلاس‌های پایتون به جای توابع استفاده می‌کنند. آنها استفاده مجدد و سازماندهی کد بهتری ارائه می‌دهند.

CBV پایه:
```python
from django.views import View

class MyView(View):
    def get(self, request):
        return HttpResponse("GET request")
    
    def post(self, request):
        return HttpResponse("POST request")
```

Viewهای Generic:
- ListView: نمایش لیست اشیاء
- DetailView: نمایش یک شیء
- CreateView: ایجاد شیء جدید
- UpdateView: به‌روزرسانی شیء موجود
- DeleteView: حذف شیء
- FormView: نمایش و پردازش فرم

مثال ListView:
```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10
```

مثال DetailView:
```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
```''',
            'code_example': '''from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('post_list')''',
            'code_example_windows': '''# In views.py
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('post_list')''',
            'code_example_mac': '''# In views.py
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('post_list')''',
            'exercise_en': 'Create a ListView for the Book model that displays books, paginated by 5 items per page.',
            'exercise_fa': 'یک ListView برای مدل Book ایجاد کنید که کتاب‌ها را نمایش می‌دهد، با صفحه‌بندی 5 مورد در هر صفحه.',
            'exercise_solution': '''from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    paginate_by = 5''',
            'order': 2
        },
        {
            'slug': 'url-patterns',
            'title_en': 'URL Patterns and Routing',
            'title_fa': 'الگوهای URL و مسیریابی',
            'content_en': '''URL patterns map URLs to views. Django uses path() and re_path() for routing.

Basic URL Pattern:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

URL Parameters:
- Capture values from URL
- Types: str, int, slug, uuid, path
- Example: path('post/<int:id>/', views.post_detail)

URL Names:
- Give URLs names for reverse lookup
- Use in templates: {% url 'name' %}
- Use in views: reverse('name')

Including URLs:
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

URL Namespaces:
```python
# blog/urls.py
app_name = 'blog'
urlpatterns = [...]

# Usage: 'blog:post_detail'
```''',
            'content_fa': '''الگوهای URL، URLها را به viewها نگاشت می‌کنند. جنگو از path() و re_path() برای مسیریابی استفاده می‌کند.

الگوی URL پایه:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
```

پارامترهای URL:
- گرفتن مقادیر از URL
- انواع: str، int، slug، uuid، path
- مثال: path('post/<int:id>/', views.post_detail)

نام‌های URL:
- به URLها نام بدهید برای جستجوی معکوس
- استفاده در قالب‌ها: {% url 'name' %}
- استفاده در viewها: reverse('name')

شامل کردن URLها:
```python
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls')),
]
```

Namespaceهای URL:
```python
# blog/urls.py
app_name = 'blog'
urlpatterns = [...]

# استفاده: 'blog:post_detail'
```''',
            'code_example': '''from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/', include('blog.urls')),
]''',
            'code_example_windows': '''# In urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/', include('blog.urls')),
]

# In blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
]''',
            'code_example_mac': '''# In urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('blog/', include('blog.urls')),
]

# In blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
]''',
            'exercise_en': 'Create URL patterns for: home page ("/"), about page ("/about/"), and product detail page ("/products/<product_id>/") with appropriate names.',
            'exercise_fa': 'الگوهای URL برای: صفحه اصلی ("/")، صفحه درباره ("/about/")، و صفحه جزئیات محصول ("/products/<product_id>/") با نام‌های مناسب ایجاد کنید.',
            'exercise_solution': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]''',
            'order': 3
        },
        {
            'slug': 'view-decorators',
            'title_en': 'View Decorators',
            'title_fa': 'دکوراتورهای View',
            'content_en': '''Decorators modify view behavior. Django provides several built-in decorators.

Common Decorators:
- @login_required: Require user authentication
- @permission_required: Require specific permission
- @require_http_methods: Restrict HTTP methods
- @csrf_exempt: Disable CSRF protection
- @cache_control: Set cache headers
- @never_cache: Disable caching

Usage:
```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
def my_view(request):
    return HttpResponse("Protected view")

@require_http_methods(["GET", "POST"])
def form_view(request):
    return HttpResponse("Form view")
```

Class-Based View Decorators:
```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class MyView(View):
    def get(self, request):
        return HttpResponse("Protected")
```''',
            'content_fa': '''دکوراتورها رفتار view را تغییر می‌دهند. جنگو چندین دکوراتور داخلی ارائه می‌دهد.

دکوراتورهای رایج:
- @login_required: نیاز به احراز هویت کاربر
- @permission_required: نیاز به مجوز خاص
- @require_http_methods: محدود کردن متدهای HTTP
- @csrf_exempt: غیرفعال کردن محافظت CSRF
- @cache_control: تنظیم هدرهای cache
- @never_cache: غیرفعال کردن cache

استفاده:
```python
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

@login_required
def my_view(request):
    return HttpResponse("Protected view")

@require_http_methods(["GET", "POST"])
def form_view(request):
    return HttpResponse("Form view")
```

دکوراتورهای View مبتنی بر کلاس:
```python
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class MyView(View):
    def get(self, request):
        return HttpResponse("Protected")
```''',
            'code_example': '''from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@login_required
def protected_view(request):
    return HttpResponse("This requires login")

@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request):
    return HttpResponse("This requires permission")

@require_http_methods(["GET", "POST"])
def form_view(request):
    return HttpResponse("Only GET and POST allowed")''',
            'code_example_windows': '''# In views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@login_required
def protected_view(request):
    return HttpResponse("This requires login")

@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request):
    return HttpResponse("This requires permission")

@require_http_methods(["GET", "POST"])
def form_view(request):
    return HttpResponse("Only GET and POST allowed")''',
            'code_example_mac': '''# In views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@login_required
def protected_view(request):
    return HttpResponse("This requires login")

@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request):
    return HttpResponse("This requires permission")

@require_http_methods(["GET", "POST"])
def form_view(request):
    return HttpResponse("Only GET and POST allowed")''',
            'exercise_en': 'Create a view that requires user login and only accepts GET and POST methods.',
            'exercise_fa': 'یک view ایجاد کنید که نیاز به ورود کاربر دارد و فقط متدهای GET و POST را می‌پذیرد.',
            'exercise_solution': '''from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

@login_required
@require_http_methods(["GET", "POST"])
def my_view(request):
    return HttpResponse("Protected view")''',
            'order': 4
        }
    ]
}

