"""
Section 11: Performance and Optimization
Database optimization, caching, and performance tuning
"""

SECTION_DATA = {
    'slug': 'performance',
    'title_en': 'Performance and Optimization',
    'title_fa': 'عملکرد و بهینه‌سازی',
    'description_en': 'Optimize Django applications for better performance',
    'description_fa': 'بهینه‌سازی برنامه‌های جنگو برای عملکرد بهتر',
    'lessons': [
        {
            'slug': 'database-optimization',
            'title_en': 'Database Optimization',
            'title_fa': 'بهینه‌سازی پایگاه داده',
            'content_en': '''Optimize database queries to reduce queries.

select_related():
- For ForeignKey relationships
- Performs SQL JOIN
```python
posts = Post.objects.select_related('author').all()
```

prefetch_related():
- For ManyToMany and reverse ForeignKey
- Performs separate queries
```python
posts = Post.objects.prefetch_related('tags').all()
```

only() and defer():
- Limit fields fetched
```python
posts = Post.objects.only('title', 'content')
posts = Post.objects.defer('content')
```

Avoid N+1 Queries:
```python
# Bad: N+1 queries
for post in Post.objects.all():
    print(post.author.name)  # Query for each post

# Good: Single query
for post in Post.objects.select_related('author').all():
    print(post.author.name)  # No additional queries
```''',
            'content_fa': '''کوئری‌های پایگاه داده را برای کاهش کوئری‌ها بهینه کنید.

select_related():
- برای روابط ForeignKey
- SQL JOIN انجام می‌دهد
```python
posts = Post.objects.select_related('author').all()
```

prefetch_related():
- برای ManyToMany و ForeignKey معکوس
- کوئری‌های جداگانه انجام می‌دهد
```python
posts = Post.objects.prefetch_related('tags').all()
```

only() و defer():
- محدود کردن فیلدهای واکشی شده
```python
posts = Post.objects.only('title', 'content')
posts = Post.objects.defer('content')
```

اجتناب از کوئری‌های N+1:
```python
# بد: کوئری‌های N+1
for post in Post.objects.all():
    print(post.author.name)  # کوئری برای هر پست

# خوب: یک کوئری
for post in Post.objects.select_related('author').all():
    print(post.author.name)  # بدون کوئری اضافی
```''',
            'code_example': '''# Optimize ForeignKey queries
posts = Post.objects.select_related('author').all()

# Optimize ManyToMany queries
posts = Post.objects.prefetch_related('tags').all()

# Combine both
posts = Post.objects.select_related('author').prefetch_related('tags').all()

# Limit fields
posts = Post.objects.only('title', 'created_at')''',
            'code_example_windows': '''# In views.py
from .models import Post

# Bad: Multiple queries
def post_list_bad(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# Good: Optimized
def post_list_good(request):
    posts = Post.objects.select_related('author').prefetch_related('tags').all()
    return render(request, 'posts.html', {'posts': posts})''',
            'code_example_mac': '''# In views.py
from .models import Post

# Bad: Multiple queries
def post_list_bad(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# Good: Optimized
def post_list_good(request):
    posts = Post.objects.select_related('author').prefetch_related('tags').all()
    return render(request, 'posts.html', {'posts': posts})''',
            'exercise_en': 'Optimize a QuerySet that accesses related author and tags to avoid N+1 queries.',
            'exercise_fa': 'یک QuerySet که به author و tags مرتبط دسترسی دارد را بهینه کنید تا از کوئری‌های N+1 اجتناب کنید.',
            'exercise_solution': '''posts = Post.objects.select_related('author').prefetch_related('tags').all()''',
            'order': 1
        }
    ]
}

