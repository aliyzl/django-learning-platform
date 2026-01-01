"""
Section 9: Testing
Writing and running tests in Django
"""

SECTION_DATA = {
    'slug': 'testing',
    'title_en': 'Testing',
    'title_fa': 'تست',
    'description_en': 'Write and run tests for Django applications',
    'description_fa': 'نوشتن و اجرای تست‌ها برای برنامه‌های جنگو',
    'lessons': [
        {
            'slug': 'writing-tests',
            'title_en': 'Writing Tests',
            'title_fa': 'نوشتن تست‌ها',
            'content_en': '''Django uses Python's unittest framework for testing.

Basic Test:
```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test content'
        )
        self.assertEqual(post.title, 'Test Post')
```

Test Methods:
- setUp(): Run before each test
- tearDown(): Run after each test
- Test methods must start with 'test_'

Running Tests:
- python manage.py test
- python manage.py test app_name
- python manage.py test app_name.TestClass
- python manage.py test app_name.TestClass.test_method''',
            'content_fa': '''جنگو از فریمورک unittest پایتون برای تست استفاده می‌کند.

تست پایه:
```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test content'
        )
        self.assertEqual(post.title, 'Test Post')
```

متدهای تست:
- setUp(): قبل از هر تست اجرا می‌شود
- tearDown(): بعد از هر تست اجرا می‌شود
- متدهای تست باید با 'test_' شروع شوند

اجرای تست‌ها:
- python manage.py test
- python manage.py test app_name
- python manage.py test app_name.TestClass
- python manage.py test app_name.TestClass.test_method''',
            'code_example': '''from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            content='Test content'
        )
    
    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')
    
    def test_post_str(self):
        self.assertEqual(str(self.post), 'Test Post')''',
            'code_example_windows': '''# In tests.py
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title='Test',
            content='Content'
        )
        self.assertEqual(post.title, 'Test')

# Run tests
python manage.py test''',
            'code_example_mac': '''# In tests.py
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title='Test',
            content='Content'
        )
        self.assertEqual(post.title, 'Test')

# Run tests
python manage.py test''',
            'exercise_en': 'Write a test that creates a Post and verifies its title is correct.',
            'exercise_fa': 'یک تست بنویسید که یک Post ایجاد می‌کند و عنوان آن را تأیید می‌کند.',
            'exercise_solution': '''from django.test import TestCase
from .models import Post

class PostTest(TestCase):
    def test_post_title(self):
        post = Post.objects.create(title='Test', content='Content')
        self.assertEqual(post.title, 'Test')''',
            'order': 1
        },
        {
            'slug': 'test-client',
            'title_en': 'Test Client',
            'title_fa': 'Test Client',
            'content_en': '''Use Django's test client to test views.

Example:
```python
from django.test import TestCase, Client

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_post_list_view(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_create(self):
        response = self.client.post('/posts/create/', {
            'title': 'New Post',
            'content': 'Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
```''',
            'content_fa': '''از test client جنگو برای تست viewها استفاده کنید.

مثال:
```python
from django.test import TestCase, Client

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_post_list_view(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
    
    def test_post_create(self):
        response = self.client.post('/posts/create/', {
            'title': 'New Post',
            'content': 'Content'
        })
        self.assertEqual(response.status_code, 302)  # Redirect
```''',
            'code_example': '''from django.test import TestCase, Client
from django.contrib.auth.models import User

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@test.com', 'pass')
    
    def test_post_list(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)''',
            'code_example_windows': '''# In tests.py
from django.test import TestCase, Client

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)''',
            'code_example_mac': '''# In tests.py
from django.test import TestCase, Client

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)''',
            'exercise_en': 'Write a test that uses the test client to check if a view returns status code 200.',
            'exercise_fa': 'یک تست بنویسید که از test client استفاده می‌کند تا بررسی کند یک view کد وضعیت 200 را برمی‌گرداند.',
            'exercise_solution': '''from django.test import TestCase, Client

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)''',
            'order': 2
        }
    ]
}

