"""
Section 7: User Authentication and Authorization
User authentication, login, logout, registration, permissions
"""

SECTION_DATA = {
    'slug': 'authentication',
    'title_en': 'User Authentication and Authorization',
    'title_fa': 'احراز هویت و مجوز کاربر',
    'description_en': 'Master Django authentication: login, logout, registration, and permissions',
    'description_fa': 'تسلط بر احراز هویت جنگو: ورود، خروج، ثبت‌نام و مجوزها',
    'lessons': [
        {
            'slug': 'user-model',
            'title_en': 'User Model',
            'title_fa': 'مدل User',
            'content_en': '''Django provides a built-in User model for authentication.

User Model Fields:
- username: Unique username
- email: Email address
- password: Hashed password
- first_name, last_name: Name fields
- is_active: Active status
- is_staff: Staff status
- is_superuser: Superuser status
- date_joined: Join date
- last_login: Last login time

Creating Users:
```python
from django.contrib.auth.models import User

# Create user
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret123'
)

# Create superuser
superuser = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)
```

Checking Authentication:
```python
if request.user.is_authenticated:
    # User is logged in
    pass
```''',
            'content_fa': '''جنگو یک مدل User داخلی برای احراز هویت ارائه می‌دهد.

فیلدهای مدل User:
- username: نام کاربری یکتا
- email: آدرس ایمیل
- password: رمز عبور هش شده
- first_name، last_name: فیلدهای نام
- is_active: وضعیت فعال
- is_staff: وضعیت کارمند
- is_superuser: وضعیت superuser
- date_joined: تاریخ عضویت
- last_login: زمان آخرین ورود

ایجاد کاربران:
```python
from django.contrib.auth.models import User

# ایجاد کاربر
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret123'
)

# ایجاد superuser
superuser = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)
```

بررسی احراز هویت:
```python
if request.user.is_authenticated:
    # کاربر وارد شده است
    pass
```''',
            'code_example': '''from django.contrib.auth.models import User

# Create regular user
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret123'
)

# Create superuser
admin = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

# Check authentication
if request.user.is_authenticated:
    username = request.user.username
    email = request.user.email''',
            'code_example_windows': '''# In Python shell
python manage.py shell

from django.contrib.auth.models import User

# Create user
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret123'
)

# Or use management command
python manage.py createsuperuser

# In views.py
if request.user.is_authenticated:
    username = request.user.username''',
            'code_example_mac': '''# In Python shell
python manage.py shell

from django.contrib.auth.models import User

# Create user
user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret123'
)

# Or use management command
python manage.py createsuperuser

# In views.py
if request.user.is_authenticated:
    username = request.user.username''',
            'exercise_en': 'Create a view that checks if the user is authenticated and displays their username if they are logged in.',
            'exercise_fa': 'یک view ایجاد کنید که بررسی می‌کند کاربر احراز هویت شده است یا نه و نام کاربری آنها را اگر وارد شده باشند نمایش می‌دهد.',
            'exercise_solution': '''from django.shortcuts import render

def profile_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'profile.html', {'username': username})
    else:
        return redirect('login')''',
            'order': 1
        },
        {
            'slug': 'login-logout',
            'title_en': 'Login and Logout',
            'title_fa': 'ورود و خروج',
            'content_en': '''Django provides built-in views for login and logout.

Using Built-in Views:
```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

Custom Login View:
```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
```

Logout:
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

Login Required Decorator:
```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return HttpResponse("Protected content")
```''',
            'content_fa': '''جنگو viewهای داخلی برای ورود و خروج ارائه می‌دهد.

استفاده از Viewهای داخلی:
```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

View ورود سفارشی:
```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'اعتبارنامه نامعتبر'})
    return render(request, 'login.html')
```

خروج:
```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
```

دکوراتور Login Required:
```python
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return HttpResponse("محتوای محافظت شده")
```''',
            'code_example': '''from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def protected_view(request):
    return render(request, 'protected.html')''',
            'code_example_windows': '''# In views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# In urls.py
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]''',
            'code_example_mac': '''# In views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

# In urls.py
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]''',
            'exercise_en': 'Create a custom login view that authenticates users and redirects them to the home page on success.',
            'exercise_fa': 'یک view ورود سفارشی ایجاد کنید که کاربران را احراز هویت می‌کند و در صورت موفقیت آنها را به صفحه اصلی redirect می‌کند.',
            'exercise_solution': '''from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')''',
            'order': 2
        },
        {
            'slug': 'user-registration',
            'title_en': 'User Registration',
            'title_fa': 'ثبت‌نام کاربر',
            'content_en': '''Create custom registration views for new users.

Registration Form:
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

Registration View:
```python
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
```

Manual Registration:
```python
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')
```''',
            'content_fa': '''ایجاد viewهای ثبت‌نام سفارشی برای کاربران جدید.

فرم ثبت‌نام:
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

View ثبت‌نام:
```python
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
```

ثبت‌نام دستی:
```python
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')
```''',
            'code_example': '''from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})''',
            'code_example_windows': '''# In forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# In views.py
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})''',
            'code_example_mac': '''# In forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# In views.py
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})''',
            'exercise_en': 'Create a user registration form and view that allows users to register with username, email, and password.',
            'exercise_fa': 'یک فرم و view ثبت‌نام کاربر ایجاد کنید که به کاربران امکان ثبت‌نام با username، email و password را می‌دهد.',
            'exercise_solution': '''from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})''',
            'order': 3
        },
        {
            'slug': 'permissions',
            'title_en': 'Permissions and Groups',
            'title_fa': 'مجوزها و گروه‌ها',
            'content_en': '''Django provides a permission system for access control.

Checking Permissions:
```python
# Check if user has permission
if request.user.has_perm('app.add_post'):
    # User can add posts
    pass

# Check multiple permissions
if request.user.has_perms(['app.add_post', 'app.change_post']):
    pass
```

Permission Decorator:
```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')
```

Groups:
```python
from django.contrib.auth.models import Group, Permission

# Create group
editors = Group.objects.create(name='Editors')

# Add permissions
post_permission = Permission.objects.get(codename='add_post')
editors.permissions.add(post_permission)

# Add user to group
user.groups.add(editors)
```

Model Permissions:
- Django automatically creates: add, change, delete, view
- Custom permissions can be defined in Meta class''',
            'content_fa': '''جنگو یک سیستم مجوز برای کنترل دسترسی ارائه می‌دهد.

بررسی مجوزها:
```python
# بررسی اینکه کاربر مجوز دارد
if request.user.has_perm('app.add_post'):
    # کاربر می‌تواند پست اضافه کند
    pass

# بررسی چندین مجوز
if request.user.has_perms(['app.add_post', 'app.change_post']):
    pass
```

دکوراتور مجوز:
```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')
```

گروه‌ها:
```python
from django.contrib.auth.models import Group, Permission

# ایجاد گروه
editors = Group.objects.create(name='Editors')

# افزودن مجوزها
post_permission = Permission.objects.get(codename='add_post')
editors.permissions.add(post_permission)

# افزودن کاربر به گروه
user.groups.add(editors)
```

مجوزهای مدل:
- جنگو به طور خودکار ایجاد می‌کند: add، change، delete، view
- مجوزهای سفارشی می‌توانند در کلاس Meta تعریف شوند''',
            'code_example': '''from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group, Permission

# Check permission
if request.user.has_perm('myapp.add_post'):
    # User can add posts
    pass

# Permission decorator
@permission_required('myapp.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')

# Create group with permissions
editors = Group.objects.create(name='Editors')
post_add = Permission.objects.get(codename='add_post')
editors.permissions.add(post_add)''',
            'code_example_windows': '''# In views.py
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')

# In Python shell
python manage.py shell

from django.contrib.auth.models import Group, Permission
editors = Group.objects.create(name='Editors')
post_add = Permission.objects.get(codename='add_post')
editors.permissions.add(post_add)''',
            'code_example_mac': '''# In views.py
from django.contrib.auth.decorators import permission_required

@permission_required('myapp.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')

# In Python shell
python manage.py shell

from django.contrib.auth.models import Group, Permission
editors = Group.objects.create(name='Editors')
post_add = Permission.objects.get(codename='add_post')
editors.permissions.add(post_add)''',
            'exercise_en': 'Create a view that requires the "add_post" permission and check if the current user has this permission.',
            'exercise_fa': 'یک view ایجاد کنید که نیاز به مجوز "add_post" دارد و بررسی کنید که کاربر فعلی این مجوز را دارد یا نه.',
            'exercise_solution': '''from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('myapp.add_post', raise_exception=True)
def create_post(request):
    return render(request, 'create_post.html')

# Or check manually
def create_post(request):
    if request.user.has_perm('myapp.add_post'):
        return render(request, 'create_post.html')
    else:
        return HttpResponse("Permission denied", status=403)''',
            'order': 4
        }
    ]
}

