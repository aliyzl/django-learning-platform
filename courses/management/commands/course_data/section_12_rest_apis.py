"""
Section 12: REST APIs with Django REST Framework
Building RESTful APIs with DRF
"""

SECTION_DATA = {
    'slug': 'rest-apis',
    'title_en': 'REST APIs with Django REST Framework',
    'title_fa': 'REST APIها با Django REST Framework',
    'description_en': 'Build RESTful APIs using Django REST Framework',
    'description_fa': 'ساخت REST APIها با استفاده از Django REST Framework',
    'lessons': [
        {
            'slug': 'drf-introduction',
            'title_en': 'Introduction to DRF',
            'title_fa': 'معرفی DRF',
            'content_en': '''Django REST Framework (DRF) is a toolkit for building Web APIs.

Installation:
```bash
pip install djangorestframework
```

Add to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Basic Serializer:
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

Basic ViewSet:
```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

URL Configuration:
```python
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = router.urls
```''',
            'content_fa': '''Django REST Framework (DRF) یک ابزار برای ساخت Web APIها است.

نصب:
```bash
pip install djangorestframework
```

افزودن به INSTALLED_APPS:
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Serializer پایه:
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

ViewSet پایه:
```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

پیکربندی URL:
```python
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
urlpatterns = router.urls
```''',
            'code_example': '''# Install DRF
pip install djangorestframework

# In settings.py
INSTALLED_APPS = [
    'rest_framework',
]

# In serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# In views.py
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer''',
            'code_example_windows': '''# Install
pip install djangorestframework

# settings.py
INSTALLED_APPS = ['rest_framework']

# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' ''',
            'code_example_mac': '''# Install
pip install djangorestframework

# settings.py
INSTALLED_APPS = ['rest_framework']

# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' ''',
            'exercise_en': 'Install DRF, create a serializer for your Post model, and set up a basic ViewSet.',
            'exercise_fa': 'DRF را نصب کنید، یک serializer برای مدل Post خود ایجاد کنید و یک ViewSet پایه راه‌اندازی کنید.',
            'exercise_solution': '''# Install
pip install djangorestframework

# serializers.py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer''',
            'order': 1
        }
    ]
}




