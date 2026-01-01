"""
Section 8: Admin Interface
Django admin customization and configuration
"""

SECTION_DATA = {
    'slug': 'admin',
    'title_en': 'Admin Interface',
    'title_fa': 'رابط Admin',
    'description_en': 'Customize and extend Django admin interface',
    'description_fa': 'سفارشی‌سازی و گسترش رابط admin جنگو',
    'lessons': [
        {
            'slug': 'admin-customization',
            'title_en': 'Admin Customization',
            'title_fa': 'سفارشی‌سازی Admin',
            'content_en': '''Customize the Django admin interface for better usability.

Basic Registration:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Custom Admin Class:
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
```

Admin Options:
- list_display: Fields to display in list
- list_filter: Filters in sidebar
- search_fields: Searchable fields
- ordering: Default ordering
- list_per_page: Items per page
- date_hierarchy: Date-based navigation''',
            'content_fa': '''رابط admin جنگو را برای قابلیت استفاده بهتر سفارشی کنید.

ثبت پایه:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

کلاس Admin سفارشی:
```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
```

گزینه‌های Admin:
- list_display: فیلدهای نمایش در لیست
- list_filter: فیلترها در sidebar
- search_fields: فیلدهای قابل جستجو
- ordering: مرتب‌سازی پیش‌فرض
- list_per_page: آیتم‌ها در هر صفحه
- date_hierarchy: ناوبری مبتنی بر تاریخ''',
            'code_example': '''from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'published']
    list_filter = ['created_at', 'author', 'published']
    search_fields = ['title', 'content']
    ordering = ['-created_at']
    list_per_page = 25
    date_hierarchy = 'created_at' ''',
            'code_example_windows': '''# In admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']''',
            'code_example_mac': '''# In admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']''',
            'exercise_en': 'Customize the admin for your Post model with list_display, list_filter, and search_fields.',
            'exercise_fa': 'admin را برای مدل Post خود با list_display، list_filter و search_fields سفارشی کنید.',
            'exercise_solution': '''from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['title', 'content']''',
            'order': 1
        },
        {
            'slug': 'admin-actions',
            'title_en': 'Admin Actions',
            'title_fa': 'اقدامات Admin',
            'content_en': '''Create custom admin actions for bulk operations.

Example:
```python
@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]
```''',
            'content_fa': '''ایجاد اقدامات admin سفارشی برای عملیات دسته‌ای.

مثال:
```python
@admin.action(description='علامت‌گذاری پست‌های انتخاب شده به عنوان منتشر شده')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]
```''',
            'code_example': '''from django.contrib import admin
from .models import Post

@admin.action(description='Mark selected as published')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]''',
            'code_example_windows': '''# In admin.py
from django.contrib import admin
from .models import Post

@admin.action(description='Mark as published')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]''',
            'code_example_mac': '''# In admin.py
from django.contrib import admin
from .models import Post

@admin.action(description='Mark as published')
def make_published(modeladmin, request, queryset):
    queryset.update(published=True)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [make_published]''',
            'exercise_en': 'Create an admin action that deletes all selected posts.',
            'exercise_fa': 'یک اقدام admin ایجاد کنید که تمام پست‌های انتخاب شده را حذف می‌کند.',
            'exercise_solution': '''from django.contrib import admin

@admin.action(description='Delete selected posts')
def delete_selected(modeladmin, request, queryset):
    queryset.delete()

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    actions = [delete_selected]''',
            'order': 2
        }
    ]
}

