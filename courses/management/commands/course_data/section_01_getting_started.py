"""
Section 1: Getting Started
Expanded content for Django installation and setup
"""

SECTION_DATA = {
    'slug': 'getting-started',
    'title_en': 'Getting Started',
    'title_fa': 'شروع کار',
    'description_en': 'Install Django and set up your development environment',
    'description_fa': 'جنگو را نصب کنید و محیط توسعه خود را راه‌اندازی کنید',
    'lessons': [
        {
            'slug': 'introduction',
            'title_en': 'Introduction to Django',
            'title_fa': 'معرفی جنگو',
            'content_en': '''Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

Key Features:
- Fast development: Django was designed to help developers take applications from concept to completion as quickly as possible
- Secure by default: Django takes security seriously and helps developers avoid many common security mistakes
- Scalable: Some of the busiest sites on the web leverage Django's ability to quickly and flexibly scale
- Versatile: Companies, organizations, and governments have used Django to build all sorts of things
- Well-documented: Django has extensive documentation and a thriving community

Django follows the MVT (Model-View-Template) architecture pattern, which is similar to MVC but adapted for Django's philosophy:
- Model: The data access layer, handles data structure and database
- View: The business logic layer, processes requests and returns responses
- Template: The presentation layer, handles user interface and display

Django was created in 2003 and has been under active development since 2005. It's used by major companies like Instagram, Pinterest, Spotify, and NASA.''',
            'content_fa': '''جنگو یک فریمورک وب پایتون سطح بالا است که توسعه سریع و طراحی تمیز و عملی را تشویق می‌کند. ساخته شده توسط توسعه‌دهندگان با تجربه، بسیاری از مشکلات توسعه وب را برطرف می‌کند، بنابراین می‌توانید روی نوشتن برنامه خود تمرکز کنید.

ویژگی‌های کلیدی:
- توسعه سریع: جنگو برای کمک به توسعه‌دهندگان در تبدیل ایده‌ها به برنامه‌های کامل در سریع‌ترین زمان ممکن طراحی شده است
- امن به صورت پیش‌فرض: جنگو امنیت را جدی می‌گیرد و به توسعه‌دهندگان کمک می‌کند از بسیاری از اشتباهات امنیتی رایج اجتناب کنند
- مقیاس‌پذیر: برخی از شلوغ‌ترین سایت‌های وب از توانایی جنگو برای مقیاس‌پذیری سریع و انعطاف‌پذیر استفاده می‌کنند
- همه‌کاره: شرکت‌ها، سازمان‌ها و دولت‌ها از جنگو برای ساخت انواع چیزها استفاده کرده‌اند
- مستندات خوب: جنگو مستندات گسترده و جامعه‌ای پررونق دارد

جنگو از الگوی معماری MVT (Model-View-Template) پیروی می‌کند که شبیه به MVC است اما برای فلسفه جنگو تطبیق یافته است:
- Model: لایه دسترسی به داده، ساختار داده و پایگاه داده را مدیریت می‌کند
- View: لایه منطق کسب‌وکار، درخواست‌ها را پردازش می‌کند و پاسخ‌ها را برمی‌گرداند
- Template: لایه ارائه، رابط کاربری و نمایش را مدیریت می‌کند

جنگو در سال 2003 ایجاد شد و از سال 2005 تحت توسعه فعال قرار دارد. توسط شرکت‌های بزرگی مانند اینستاگرام، پینترست، اسپاتیفای و ناسا استفاده می‌شود.''',
            'code_example': '',
            'code_example_windows': '',
            'code_example_mac': '',
            'exercise_en': 'Research and list 5 major websites or applications that use Django.',
            'exercise_fa': 'تحقیق کنید و 5 وب‌سایت یا برنامه اصلی که از جنگو استفاده می‌کنند را فهرست کنید.',
            'exercise_solution': '''Some major Django users:
1. Instagram
2. Pinterest
3. Spotify
4. NASA
5. The Washington Post''',
            'order': 1
        },
        {
            'slug': 'installation-windows',
            'title_en': 'Installing Django on Windows',
            'title_fa': 'نصب جنگو در ویندوز',
            'content_en': '''To install Django on Windows, you'll need Python installed first. Here's a comprehensive guide to set up Django on Windows:

Step 1: Install Python
- Download Python from python.org (recommended: Python 3.8 or higher)
- During installation, make sure to check "Add Python to PATH"
- Verify installation by opening Command Prompt and typing: python --version
- You should see something like: Python 3.11.0

Step 2: Create a Virtual Environment
Virtual environments help isolate project dependencies. This is a best practice.
- Open Command Prompt in your project directory
- Run: python -m venv venv
- This creates a virtual environment in a folder named "venv"
- Activate it: venv\\Scripts\\activate
- You'll see (venv) at the start of your command prompt when activated

Step 3: Install Django
- With virtual environment activated, run: pip install django
- This installs the latest stable version of Django
- Verify installation: python -m django --version
- You should see something like: 5.1

Step 4: Upgrade pip (Optional but Recommended)
- Run: python -m pip install --upgrade pip
- This ensures you have the latest version of pip

Troubleshooting:
- If "python" command doesn't work, try "py" instead
- If pip is not found, install it: python -m ensurepip --upgrade
- Always activate your virtual environment before working on Django projects''',
            'content_fa': '''برای نصب جنگو در ویندوز، ابتدا باید پایتون را نصب کنید. در اینجا راهنمای جامعی برای راه‌اندازی جنگو در ویندوز آمده است:

مرحله 1: نصب پایتون
- پایتون را از python.org دانلود کنید (توصیه می‌شود: Python 3.8 یا بالاتر)
- در حین نصب، حتماً "Add Python to PATH" را بررسی کنید
- با باز کردن Command Prompt و تایپ کردن تأیید کنید: python --version
- باید چیزی شبیه به این ببینید: Python 3.11.0

مرحله 2: ایجاد محیط مجازی
محیط‌های مجازی به جداسازی وابستگی‌های پروژه کمک می‌کنند. این یک روش خوب است.
- Command Prompt را در دایرکتوری پروژه خود باز کنید
- اجرا کنید: python -m venv venv
- این یک محیط مجازی در پوشه‌ای به نام "venv" ایجاد می‌کند
- فعال کنید: venv\\Scripts\\activate
- وقتی فعال شد، (venv) را در ابتدای خط فرمان خود خواهید دید

مرحله 3: نصب جنگو
- با محیط مجازی فعال شده، اجرا کنید: pip install django
- این آخرین نسخه پایدار جنگو را نصب می‌کند
- تأیید نصب: python -m django --version
- باید چیزی شبیه به این ببینید: 5.1

مرحله 4: ارتقای pip (اختیاری اما توصیه می‌شود)
- اجرا کنید: python -m pip install --upgrade pip
- این اطمینان می‌دهد که آخرین نسخه pip را دارید

عیب‌یابی:
- اگر دستور "python" کار نمی‌کند، به جای آن "py" را امتحان کنید
- اگر pip پیدا نشد، آن را نصب کنید: python -m ensurepip --upgrade
- همیشه قبل از کار روی پروژه‌های جنگو، محیط مجازی خود را فعال کنید''',
            'code_example': '',
            'code_example_windows': '''# Open Command Prompt (cmd) or PowerShell

# Step 1: Check Python version
python --version

# Step 2: Create virtual environment
python -m venv venv

# Step 3: Activate virtual environment
venv\\Scripts\\activate

# Step 4: Upgrade pip (recommended)
python -m pip install --upgrade pip

# Step 5: Install Django
pip install django

# Step 6: Verify installation
python -m django --version

# Step 7: Install specific Django version (optional)
# pip install django==5.1

# To deactivate virtual environment later:
# deactivate''',
            'code_example_mac': '',
            'exercise_en': 'Create a virtual environment named "myproject" and install Django version 5.1 in it. Verify the installation.',
            'exercise_fa': 'یک محیط مجازی با نام "myproject" ایجاد کنید و جنگو نسخه 5.1 را در آن نصب کنید. نصب را تأیید کنید.',
            'exercise_solution': '''python -m venv myproject
myproject\\Scripts\\activate
pip install django==5.1
python -m django --version''',
            'order': 2
        },
        {
            'slug': 'installation-mac',
            'title_en': 'Installing Django on Mac',
            'title_fa': 'نصب جنگو در مک',
            'content_en': '''Installing Django on macOS is straightforward. Here's a comprehensive step-by-step process:

Step 1: Install Python (if not already installed)
- macOS comes with Python, but it's often an older version
- Recommended: Use Homebrew to install the latest Python
- Install Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- Install Python: brew install python
- Verify: python3 --version

Step 2: Create a Virtual Environment
- Open Terminal
- Navigate to your project directory: cd ~/Projects (or wherever you keep projects)
- Run: python3 -m venv venv
- This creates a virtual environment in a folder named "venv"
- Activate: source venv/bin/activate
- You'll see (venv) at the start of your terminal prompt when activated

Step 3: Install Django
- With virtual environment activated: pip install django
- Verify: python -m django --version
- You should see something like: 5.1

Step 4: Upgrade pip (Optional but Recommended)
- Run: pip install --upgrade pip

Alternative: Using pyenv (Advanced)
If you need to manage multiple Python versions:
- Install pyenv: brew install pyenv
- Install Python: pyenv install 3.11.0
- Set local version: pyenv local 3.11.0

Troubleshooting:
- Use python3 instead of python if python3 is not aliased
- If you get permission errors, don't use sudo with pip
- Always activate your virtual environment before working on Django projects''',
            'content_fa': '''نصب جنگو در macOS ساده است. در اینجا فرآیند گام به گام جامعی آمده است:

مرحله 1: نصب پایتون (اگر قبلاً نصب نشده است)
- macOS با پایتون همراه است، اما اغلب نسخه قدیمی‌تری است
- توصیه می‌شود: از Homebrew برای نصب آخرین نسخه پایتون استفاده کنید
- نصب Homebrew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- نصب پایتون: brew install python
- تأیید: python3 --version

مرحله 2: ایجاد محیط مجازی
- Terminal را باز کنید
- به دایرکتوری پروژه خود بروید: cd ~/Projects (یا هر جایی که پروژه‌ها را نگه می‌دارید)
- اجرا کنید: python3 -m venv venv
- این یک محیط مجازی در پوشه‌ای به نام "venv" ایجاد می‌کند
- فعال کنید: source venv/bin/activate
- وقتی فعال شد، (venv) را در ابتدای خط فرمان ترمینال خود خواهید دید

مرحله 3: نصب جنگو
- با محیط مجازی فعال شده: pip install django
- تأیید: python -m django --version
- باید چیزی شبیه به این ببینید: 5.1

مرحله 4: ارتقای pip (اختیاری اما توصیه می‌شود)
- اجرا کنید: pip install --upgrade pip

جایگزین: استفاده از pyenv (پیشرفته)
اگر نیاز به مدیریت چندین نسخه پایتون دارید:
- نصب pyenv: brew install pyenv
- نصب پایتون: pyenv install 3.11.0
- تنظیم نسخه محلی: pyenv local 3.11.0

عیب‌یابی:
- اگر python3 به python متصل نشده است، از python3 به جای python استفاده کنید
- اگر خطاهای مجوز دریافت کردید، از sudo با pip استفاده نکنید
- همیشه قبل از کار روی پروژه‌های جنگو، محیط مجازی خود را فعال کنید''',
            'code_example': '',
            'code_example_windows': '',
            'code_example_mac': '''# Open Terminal

# Step 1: Check Python version
python3 --version

# Step 2: Create virtual environment
python3 -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate

# Step 4: Upgrade pip (recommended)
pip install --upgrade pip

# Step 5: Install Django
pip install django

# Step 6: Verify installation
python -m django --version

# Step 7: Install specific Django version (optional)
# pip install django==5.1

# To deactivate virtual environment later:
# deactivate''',
            'exercise_en': 'Create a virtual environment and install Django 5.1 on your Mac. Verify the installation works correctly.',
            'exercise_fa': 'یک محیط مجازی ایجاد کنید و جنگو 5.1 را در مک خود نصب کنید. تأیید کنید که نصب به درستی کار می‌کند.',
            'exercise_solution': '''python3 -m venv venv
source venv/bin/activate
pip install django==5.1
python -m django --version''',
            'order': 3
        },
        {
            'slug': 'creating-project',
            'title_en': 'Creating Your First Django Project',
            'title_fa': 'ایجاد اولین پروژه جنگو',
            'content_en': '''A Django project is a collection of settings and configurations for a Django application. Let's create your first project:

After installing Django, you can create a new project using the django-admin command. This will create a directory structure with all necessary files.

The project structure includes:
- manage.py: A command-line utility for administrative tasks
- settings.py: Configuration for your Django project (database, installed apps, middleware, etc.)
- urls.py: URL routing configuration (maps URLs to views)
- wsgi.py: WSGI configuration for deployment (Web Server Gateway Interface)
- asgi.py: ASGI configuration for async deployment (Asynchronous Server Gateway Interface)

Project vs App:
- A project is a collection of configuration and apps for a particular website
- An app is a web application that does something (e.g., a blog, a poll app)
- A project can contain multiple apps
- An app can be in multiple projects

Best Practices:
- Use descriptive project names
- Keep projects organized in a dedicated directory
- Use virtual environments for each project
- Don't commit virtual environments to version control''',
            'content_fa': '''یک پروژه جنگو مجموعه‌ای از تنظیمات و پیکربندی‌ها برای یک برنامه جنگو است. بیایید اولین پروژه خود را ایجاد کنیم:

پس از نصب جنگو، می‌توانید یک پروژه جدید با استفاده از دستور django-admin ایجاد کنید. این یک ساختار دایرکتوری با تمام فایل‌های لازم ایجاد می‌کند.

ساختار پروژه شامل:
- manage.py: یک ابزار خط فرمان برای کارهای مدیریتی
- settings.py: پیکربندی برای پروژه جنگو شما (پایگاه داده، برنامه‌های نصب شده، میدل‌ور و غیره)
- urls.py: پیکربندی مسیریابی URL (نقشه‌برداری URL‌ها به viewها)
- wsgi.py: پیکربندی WSGI برای استقرار (Web Server Gateway Interface)
- asgi.py: پیکربندی ASGI برای استقرار ناهمزمان (Asynchronous Server Gateway Interface)

پروژه در مقابل برنامه:
- یک پروژه مجموعه‌ای از پیکربندی و برنامه‌ها برای یک وب‌سایت خاص است
- یک برنامه یک برنامه وب است که کاری انجام می‌دهد (مثلاً یک وبلاگ، یک برنامه نظرسنجی)
- یک پروژه می‌تواند شامل چندین برنامه باشد
- یک برنامه می‌تواند در چندین پروژه باشد

بهترین روش‌ها:
- از نام‌های توصیفی برای پروژه استفاده کنید
- پروژه‌ها را در یک دایرکتوری اختصاصی سازماندهی کنید
- از محیط‌های مجازی برای هر پروژه استفاده کنید
- محیط‌های مجازی را به کنترل نسخه commit نکنید''',
            'code_example': 'django-admin startproject myproject',
            'code_example_windows': '''# In Command Prompt or PowerShell
# Navigate to your desired directory
cd C:\\Users\\YourName\\Projects

# Create Django project
django-admin startproject myproject

# Navigate into project
cd myproject

# View project structure
dir

# Run development server
python manage.py runserver

# Access at http://127.0.0.1:8000/''',
            'code_example_mac': '''# In Terminal
# Navigate to your desired directory
cd ~/Projects

# Create Django project
django-admin startproject myproject

# Navigate into project
cd myproject

# View project structure
ls -la

# Run development server
python manage.py runserver

# Access at http://127.0.0.1:8000/''',
            'exercise_en': 'Create a Django project named "blog" and start the development server. Access it in your browser.',
            'exercise_fa': 'یک پروژه جنگو با نام "blog" ایجاد کنید و سرور توسعه را راه‌اندازی کنید. در مرورگر خود به آن دسترسی پیدا کنید.',
            'exercise_solution': '''django-admin startproject blog
cd blog
python manage.py runserver
# Then open http://127.0.0.1:8000/ in your browser''',
            'order': 4
        },
        {
            'slug': 'project-structure',
            'title_en': 'Understanding Project Structure',
            'title_fa': 'درک ساختار پروژه',
            'content_en': '''Let's explore the Django project structure in detail:

Root Project Directory:
- manage.py: Command-line utility for Django administrative tasks
  * Run migrations: python manage.py migrate
  * Create superuser: python manage.py createsuperuser
  * Start development server: python manage.py runserver
  * Create apps: python manage.py startapp appname

Project Configuration Directory (same name as project):
- __init__.py: Makes the directory a Python package
- settings.py: All project settings
  * DEBUG: Set to False in production
  * ALLOWED_HOSTS: List of host/domain names
  * INSTALLED_APPS: List of applications enabled
  * DATABASES: Database configuration
  * STATIC_URL, MEDIA_URL: Static and media file settings
- urls.py: Root URL configuration
- wsgi.py: WSGI config for production deployment
- asgi.py: ASGI config for async deployment

Key Settings to Know:
- SECRET_KEY: Used for cryptographic signing (keep secret!)
- DEBUG: Shows detailed error pages (False in production)
- ALLOWED_HOSTS: Hosts that can serve this Django site
- INSTALLED_APPS: Apps that Django will use
- MIDDLEWARE: Components that process requests/responses
- ROOT_URLCONF: Points to your root URL configuration
- DATABASES: Database connection settings
- LANGUAGE_CODE: Default language
- TIME_ZONE: Default timezone''',
            'content_fa': '''بیایید ساختار پروژه جنگو را به تفصیل بررسی کنیم:

دایرکتوری ریشه پروژه:
- manage.py: ابزار خط فرمان برای کارهای مدیریتی جنگو
  * اجرای migrations: python manage.py migrate
  * ایجاد superuser: python manage.py createsuperuser
  * راه‌اندازی سرور توسعه: python manage.py runserver
  * ایجاد برنامه‌ها: python manage.py startapp appname

دایرکتوری پیکربندی پروژه (همان نام پروژه):
- __init__.py: دایرکتوری را به یک بسته پایتون تبدیل می‌کند
- settings.py: تمام تنظیمات پروژه
  * DEBUG: در production روی False تنظیم کنید
  * ALLOWED_HOSTS: لیست نام‌های host/domain
  * INSTALLED_APPS: لیست برنامه‌های فعال شده
  * DATABASES: پیکربندی پایگاه داده
  * STATIC_URL, MEDIA_URL: تنظیمات فایل‌های static و media
- urls.py: پیکربندی URL ریشه
- wsgi.py: پیکربندی WSGI برای استقرار production
- asgi.py: پیکربندی ASGI برای استقرار ناهمزمان

تنظیمات کلیدی برای دانستن:
- SECRET_KEY: برای امضای رمزنگاری استفاده می‌شود (مخفی نگه دارید!)
- DEBUG: صفحات خطای تفصیلی را نشان می‌دهد (در production False)
- ALLOWED_HOSTS: میزبان‌هایی که می‌توانند این سایت جنگو را سرو کنند
- INSTALLED_APPS: برنامه‌هایی که جنگو استفاده خواهد کرد
- MIDDLEWARE: کامپوننت‌هایی که درخواست/پاسخ را پردازش می‌کنند
- ROOT_URLCONF: به پیکربندی URL ریشه شما اشاره می‌کند
- DATABASES: تنظیمات اتصال پایگاه داده
- LANGUAGE_CODE: زبان پیش‌فرض
- TIME_ZONE: منطقه زمانی پیش‌فرض''',
            'code_example': '''# Example settings.py structure
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]''',
            'code_example_windows': '''# Navigate to project directory
cd myproject

# View settings.py
type myproject\\settings.py

# Or open in editor
notepad myproject\\settings.py''',
            'code_example_mac': '''# Navigate to project directory
cd myproject

# View settings.py
cat myproject/settings.py

# Or open in editor
open myproject/settings.py''',
            'exercise_en': 'Explore your Django project structure. Open settings.py and identify the key configuration options.',
            'exercise_fa': 'ساختار پروژه جنگو خود را بررسی کنید. settings.py را باز کنید و گزینه‌های پیکربندی کلیدی را شناسایی کنید.',
            'exercise_solution': '''# Key settings to identify:
# - SECRET_KEY
# - DEBUG
# - ALLOWED_HOSTS
# - INSTALLED_APPS
# - DATABASES
# - LANGUAGE_CODE
# - TIME_ZONE''',
            'order': 5
        },
        {
            'slug': 'development-server',
            'title_en': 'Running the Development Server',
            'title_fa': 'اجرای سرور توسعه',
            'content_en': '''Django comes with a lightweight development server that you can use during development:

Starting the Server:
- Command: python manage.py runserver
- Default address: http://127.0.0.1:8000/
- The server automatically reloads when you make code changes
- Press Ctrl+C to stop the server

Custom Port:
- Run on different port: python manage.py runserver 8080
- Access at: http://127.0.0.1:8080/

Custom IP and Port:
- python manage.py runserver 0.0.0.0:8000
- This makes the server accessible from other devices on your network

Important Notes:
- The development server is NOT suitable for production
- It's single-threaded and not optimized for performance
- Use it only for development and testing
- For production, use proper WSGI/ASGI servers like Gunicorn or uWSGI

Server Features:
- Automatic reloading on code changes
- Detailed error pages (when DEBUG=True)
- Static file serving (when DEBUG=True)
- Database migrations are applied automatically

Troubleshooting:
- Port already in use: Use a different port
- Address already in use: Stop other Django servers or use different IP
- Module not found: Check your Python path and virtual environment''',
            'content_fa': '''جنگو با یک سرور توسعه سبک همراه است که می‌توانید در طول توسعه از آن استفاده کنید:

راه‌اندازی سرور:
- دستور: python manage.py runserver
- آدرس پیش‌فرض: http://127.0.0.1:8000/
- سرور به طور خودکار هنگام تغییر کد، reload می‌شود
- برای توقف سرور Ctrl+C را فشار دهید

پورت سفارشی:
- اجرا روی پورت متفاوت: python manage.py runserver 8080
- دسترسی در: http://127.0.0.1:8080/

IP و پورت سفارشی:
- python manage.py runserver 0.0.0.0:8000
- این سرور را از دستگاه‌های دیگر در شبکه شما قابل دسترسی می‌کند

نکات مهم:
- سرور توسعه برای production مناسب نیست
- تک‌ریسمانه است و برای عملکرد بهینه نشده است
- فقط برای توسعه و تست از آن استفاده کنید
- برای production، از سرورهای WSGI/ASGI مناسب مانند Gunicorn یا uWSGI استفاده کنید

ویژگی‌های سرور:
- بارگذاری مجدد خودکار هنگام تغییر کد
- صفحات خطای تفصیلی (وقتی DEBUG=True)
- سرو کردن فایل‌های static (وقتی DEBUG=True)
- migrations پایگاه داده به طور خودکار اعمال می‌شوند

عیب‌یابی:
- پورت قبلاً استفاده شده: از پورت متفاوتی استفاده کنید
- آدرس قبلاً استفاده شده: سرورهای جنگو دیگر را متوقف کنید یا از IP متفاوتی استفاده کنید
- ماژول پیدا نشد: مسیر پایتون و محیط مجازی خود را بررسی کنید''',
            'code_example': 'python manage.py runserver',
            'code_example_windows': '''# Start development server (default port 8000)
python manage.py runserver

# Start on custom port
python manage.py runserver 8080

# Start on custom IP and port
python manage.py runserver 0.0.0.0:8000

# Stop server: Press Ctrl+C''',
            'code_example_mac': '''# Start development server (default port 8000)
python manage.py runserver

# Start on custom port
python manage.py runserver 8080

# Start on custom IP and port
python manage.py runserver 0.0.0.0:8000

# Stop server: Press Ctrl+C''',
            'exercise_en': 'Start the Django development server on port 9000 and access it in your browser.',
            'exercise_fa': 'سرور توسعه جنگو را روی پورت 9000 راه‌اندازی کنید و در مرورگر خود به آن دسترسی پیدا کنید.',
            'exercise_solution': '''python manage.py runserver 9000
# Then open http://127.0.0.1:9000/ in your browser''',
            'order': 6
        }
    ]
}

