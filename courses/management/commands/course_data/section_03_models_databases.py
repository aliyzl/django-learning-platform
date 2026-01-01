"""
Section 3: Models and Databases
Comprehensive coverage of Django models, fields, relationships, queries, and migrations
"""

SECTION_DATA = {
    'slug': 'models-databases',
    'title_en': 'Models and Databases',
    'title_fa': 'مدل‌ها و پایگاه‌های داده',
    'description_en': 'Master Django models, database relationships, queries, and migrations',
    'description_fa': 'تسلط بر مدل‌های جنگو، روابط پایگاه داده، کوئری‌ها و migrations',
    'lessons': [
        {
            'slug': 'model-fields',
            'title_en': 'Model Fields and Types',
            'title_fa': 'فیلدهای مدل و انواع',
            'content_en': '''Django provides many field types for different data types. Understanding field types is crucial for proper database design.

Common Field Types:
- CharField: Short text (max_length required)
- TextField: Long text (no max_length)
- IntegerField: Integer numbers
- FloatField: Floating point numbers
- DecimalField: Fixed-precision decimal numbers
- BooleanField: True/False values
- DateField: Date only
- DateTimeField: Date and time
- TimeField: Time only
- EmailField: Email address (validates email format)
- URLField: URL (validates URL format)
- FileField: File upload
- ImageField: Image upload (requires Pillow)
- AutoField: Auto-incrementing integer (primary key)

Field Options:
- null: Allow NULL in database (default: False)
- blank: Allow empty in forms (default: False)
- default: Default value
- unique: Unique constraint
- db_index: Create database index
- choices: Limit choices to specific values
- verbose_name: Human-readable name
- help_text: Help text for forms

Example:
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
```''',
            'content_fa': '''جنگو انواع فیلدهای زیادی برای انواع داده مختلف ارائه می‌دهد. درک انواع فیلد برای طراحی صحیح پایگاه داده ضروری است.

انواع فیلد رایج:
- CharField: متن کوتاه (نیاز به max_length دارد)
- TextField: متن طولانی (بدون max_length)
- IntegerField: اعداد صحیح
- FloatField: اعداد اعشاری
- DecimalField: اعداد اعشاری با دقت ثابت
- BooleanField: مقادیر True/False
- DateField: فقط تاریخ
- DateTimeField: تاریخ و زمان
- TimeField: فقط زمان
- EmailField: آدرس ایمیل (فرمت ایمیل را اعتبارسنجی می‌کند)
- URLField: URL (فرمت URL را اعتبارسنجی می‌کند)
- FileField: آپلود فایل
- ImageField: آپلود تصویر (نیاز به Pillow دارد)
- AutoField: عدد صحیح خودافزاینده (کلید اصلی)

گزینه‌های فیلد:
- null: اجازه NULL در پایگاه داده (پیش‌فرض: False)
- blank: اجازه خالی در فرم‌ها (پیش‌فرض: False)
- default: مقدار پیش‌فرض
- unique: محدودیت یکتا
- db_index: ایجاد ایندکس پایگاه داده
- choices: محدود کردن انتخاب‌ها به مقادیر خاص
- verbose_name: نام قابل خواندن برای انسان
- help_text: متن راهنما برای فرم‌ها

مثال:
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
```''',
            'code_example': '''from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)''',
            'code_example_windows': '''# In models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'code_example_mac': '''# In models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'exercise_en': 'Create a Book model with title (CharField, max_length=200), author (CharField, max_length=100), isbn (CharField, max_length=13, unique=True), price (DecimalField), and published_date (DateField).',
            'exercise_fa': 'یک مدل Book با title (CharField، max_length=200)، author (CharField، max_length=100)، isbn (CharField، max_length=13، unique=True)، price (DecimalField)، و published_date (DateField) ایجاد کنید.',
            'exercise_solution': '''from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()
    
    def __str__(self):
        return self.title''',
            'order': 1
        },
        {
            'slug': 'model-relationships',
            'title_en': 'Model Relationships',
            'title_fa': 'روابط مدل',
            'content_en': '''Django supports three types of relationships between models:

1. ForeignKey (Many-to-One):
- One model references another
- Example: Many posts belong to one author
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

2. ManyToManyField (Many-to-Many):
- Many instances of one model relate to many instances of another
- Example: Posts can have many tags, tags can be on many posts
```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
```

3. OneToOneField (One-to-One):
- One instance relates to exactly one instance of another
- Example: User profile extends User
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

on_delete Options:
- CASCADE: Delete related objects
- PROTECT: Prevent deletion
- SET_NULL: Set to NULL (requires null=True)
- SET_DEFAULT: Set to default value
- DO_NOTHING: Do nothing''',
            'content_fa': '''جنگو از سه نوع رابطه بین مدل‌ها پشتیبانی می‌کند:

1. ForeignKey (چند به یک):
- یک مدل به مدل دیگر ارجاع می‌دهد
- مثال: چندین پست متعلق به یک نویسنده است
```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

2. ManyToManyField (چند به چند):
- بسیاری از نمونه‌های یک مدل به بسیاری از نمونه‌های دیگری مرتبط می‌شوند
- مثال: پست‌ها می‌توانند چندین تگ داشته باشند، تگ‌ها می‌توانند در چندین پست باشند
```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
```

3. OneToOneField (یک به یک):
- یک نمونه دقیقاً به یک نمونه دیگری مرتبط می‌شود
- مثال: پروفایل کاربر User را گسترش می‌دهد
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

گزینه‌های on_delete:
- CASCADE: حذف اشیاء مرتبط
- PROTECT: جلوگیری از حذف
- SET_NULL: تنظیم به NULL (نیاز به null=True دارد)
- SET_DEFAULT: تنظیم به مقدار پیش‌فرض
- DO_NOTHING: هیچ کاری نکنید''',
            'code_example': '''from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=50)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()''',
            'code_example_windows': '''# In models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'code_example_mac': '''# In models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'exercise_en': 'Create a Comment model with a ForeignKey to Post, and a Like model with ForeignKey to Post and OneToOneField to User.',
            'exercise_fa': 'یک مدل Comment با ForeignKey به Post، و یک مدل Like با ForeignKey به Post و OneToOneField به User ایجاد کنید.',
            'exercise_solution': '''from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)''',
            'order': 2
        },
        {
            'slug': 'migrations',
            'title_en': 'Database Migrations',
            'title_fa': 'Migrations پایگاه داده',
            'content_en': '''Migrations are Django's way of propagating changes to your models into your database schema. They're version control for your database.

Creating Migrations:
- Command: python manage.py makemigrations
- Creates migration files in migrations/ directory
- Migration files are Python files that describe changes

Applying Migrations:
- Command: python manage.py migrate
- Applies all pending migrations
- Updates database schema

Migration Files:
- Named with timestamp: 0001_initial.py, 0002_add_field.py
- Contain operations: CreateModel, AddField, AlterField, etc.

Migration Operations:
- CreateModel: Create new table
- AddField: Add field to model
- RemoveField: Remove field
- AlterField: Modify field
- RenameModel: Rename model
- DeleteModel: Delete model

Rolling Back:
- python manage.py migrate app_name migration_number
- Example: python manage.py migrate myapp 0001

Migration Best Practices:
- Always review migration files before applying
- Test migrations on development first
- Don't edit applied migrations
- Use --fake for complex migrations
- Keep migrations in version control''',
            'content_fa': '''Migrations روش جنگو برای انتشار تغییرات در مدل‌های شما به طرح پایگاه داده است. آنها کنترل نسخه برای پایگاه داده شما هستند.

ایجاد Migrations:
- دستور: python manage.py makemigrations
- فایل‌های migration را در دایرکتوری migrations/ ایجاد می‌کند
- فایل‌های migration فایل‌های پایتون هستند که تغییرات را توصیف می‌کنند

اعمال Migrations:
- دستور: python manage.py migrate
- تمام migrations معلق را اعمال می‌کند
- طرح پایگاه داده را به‌روزرسانی می‌کند

فایل‌های Migration:
- نام‌گذاری شده با timestamp: 0001_initial.py، 0002_add_field.py
- شامل عملیات: CreateModel، AddField، AlterField و غیره

عملیات Migration:
- CreateModel: ایجاد جدول جدید
- AddField: افزودن فیلد به مدل
- RemoveField: حذف فیلد
- AlterField: تغییر فیلد
- RenameModel: تغییر نام مدل
- DeleteModel: حذف مدل

بازگشت:
- python manage.py migrate app_name migration_number
- مثال: python manage.py migrate myapp 0001

بهترین روش‌های Migration:
- همیشه فایل‌های migration را قبل از اعمال بررسی کنید
- ابتدا migrations را در development تست کنید
- migrations اعمال شده را ویرایش نکنید
- از --fake برای migrations پیچیده استفاده کنید
- migrations را در کنترل نسخه نگه دارید''',
            'code_example': '''# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Rollback to specific migration
python manage.py migrate myapp 0001''',
            'code_example_windows': '''# After modifying models.py, create migrations
python manage.py makemigrations

# Review the migration file in migrations/ directory
# Then apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Rollback if needed
python manage.py migrate myapp 0001

# Create empty migration (for data migrations)
python manage.py makemigrations --empty myapp''',
            'code_example_mac': '''# After modifying models.py, create migrations
python manage.py makemigrations

# Review the migration file in migrations/ directory
# Then apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations

# Rollback if needed
python manage.py migrate myapp 0001

# Create empty migration (for data migrations)
python manage.py makemigrations --empty myapp''',
            'exercise_en': 'Create a new field in your Post model, generate migrations, review the migration file, and apply it.',
            'exercise_fa': 'یک فیلد جدید در مدل Post خود ایجاد کنید، migrations را تولید کنید، فایل migration را بررسی کنید و آن را اعمال کنید.',
            'exercise_solution': '''# Step 1: Add field to model
# In models.py, add:
# views_count = models.IntegerField(default=0)

# Step 2: Create migrations
python manage.py makemigrations

# Step 3: Review migration file
# Check migrations/0002_post_views_count.py

# Step 4: Apply migrations
python manage.py migrate''',
            'order': 3
        },
        {
            'slug': 'queryset-api',
            'title_en': 'QuerySet API',
            'title_fa': 'QuerySet API',
            'content_en': '''QuerySets are Django's way of querying the database. They're lazy - they don't execute until evaluated.

Basic Queries:
- all(): Get all objects
- get(): Get single object (raises exception if not found)
- filter(): Filter objects
- exclude(): Exclude objects
- first(): Get first object
- last(): Get last object
- count(): Count objects
- exists(): Check if any objects exist

Filtering:
```python
# Get all posts
Post.objects.all()

# Get published posts
Post.objects.filter(published=True)

# Get posts by author
Post.objects.filter(author=user)

# Exclude certain posts
Post.objects.exclude(published=False)

# Multiple filters (AND)
Post.objects.filter(author=user, published=True)

# Chaining filters
Post.objects.filter(author=user).filter(published=True)
```

Lookups:
- exact: Exact match
- iexact: Case-insensitive exact
- contains: Contains substring
- icontains: Case-insensitive contains
- startswith: Starts with
- istartswith: Case-insensitive starts with
- in: In list
- gt, gte, lt, lte: Greater than, etc.
- isnull: Is NULL
- range: In range

Examples:
```python
Post.objects.filter(title__contains='Django')
Post.objects.filter(created_at__year=2024)
Post.objects.filter(price__gte=100)
```''',
            'content_fa': '''QuerySetها روش جنگو برای پرس‌وجوی پایگاه داده هستند. آنها lazy هستند - تا زمانی که ارزیابی نشوند اجرا نمی‌شوند.

کوئری‌های پایه:
- all(): دریافت تمام اشیاء
- get(): دریافت یک شیء (اگر پیدا نشود استثنا می‌اندازد)
- filter(): فیلتر کردن اشیاء
- exclude(): حذف اشیاء
- first(): دریافت اولین شیء
- last(): دریافت آخرین شیء
- count(): شمارش اشیاء
- exists(): بررسی وجود هر شیء

فیلتر کردن:
```python
# دریافت تمام پست‌ها
Post.objects.all()

# دریافت پست‌های منتشر شده
Post.objects.filter(published=True)

# دریافت پست‌های نویسنده
Post.objects.filter(author=user)

# حذف پست‌های خاص
Post.objects.exclude(published=False)

# چندین فیلتر (AND)
Post.objects.filter(author=user, published=True)

# زنجیره کردن فیلترها
Post.objects.filter(author=user).filter(published=True)
```

Lookupها:
- exact: تطابق دقیق
- iexact: تطابق دقیق بدون حساسیت به حروف
- contains: شامل زیررشته
- icontains: شامل زیررشته بدون حساسیت به حروف
- startswith: شروع با
- istartswith: شروع با بدون حساسیت به حروف
- in: در لیست
- gt, gte, lt, lte: بزرگتر از و غیره
- isnull: NULL است
- range: در محدوده

مثال‌ها:
```python
Post.objects.filter(title__contains='Django')
Post.objects.filter(created_at__year=2024)
Post.objects.filter(price__gte=100)
```''',
            'code_example': '''from .models import Post

# Get all posts
posts = Post.objects.all()

# Filter posts
published_posts = Post.objects.filter(published=True)

# Get single post
post = Post.objects.get(id=1)

# Complex filtering
recent_posts = Post.objects.filter(
    created_at__year=2024,
    published=True
).exclude(title__startswith='Draft')

# Ordering
ordered_posts = Post.objects.all().order_by('-created_at')''',
            'code_example_windows': '''# In Python shell or views.py
python manage.py shell

from myapp.models import Post

# Get all posts
posts = Post.objects.all()

# Filter posts
published_posts = Post.objects.filter(published=True)

# Get single post
post = Post.objects.get(id=1)

# Complex filtering
recent_posts = Post.objects.filter(
    created_at__year=2024,
    published=True
).exclude(title__startswith='Draft')

# Ordering
ordered_posts = Post.objects.all().order_by('-created_at')''',
            'code_example_mac': '''# In Python shell or views.py
python manage.py shell

from myapp.models import Post

# Get all posts
posts = Post.objects.all()

# Filter posts
published_posts = Post.objects.filter(published=True)

# Get single post
post = Post.objects.get(id=1)

# Complex filtering
recent_posts = Post.objects.filter(
    created_at__year=2024,
    published=True
).exclude(title__startswith='Draft')

# Ordering
ordered_posts = Post.objects.all().order_by('-created_at')''',
            'exercise_en': 'Write a QuerySet that gets all posts published in 2024, ordered by created_at descending, excluding posts with "Draft" in the title.',
            'exercise_fa': 'یک QuerySet بنویسید که تمام پست‌های منتشر شده در سال 2024 را دریافت می‌کند، به ترتیب created_at نزولی، به جز پست‌هایی که "Draft" در عنوان دارند.',
            'exercise_solution': '''posts = Post.objects.filter(
    published=True,
    created_at__year=2024
).exclude(
    title__icontains='Draft'
).order_by('-created_at')''',
            'order': 4
        },
        {
            'slug': 'aggregations-annotations',
            'title_en': 'Aggregations and Annotations',
            'title_fa': 'تجمع‌ها و حاشیه‌نویسی‌ها',
            'content_en': '''Aggregations perform calculations on QuerySets. Annotations add computed fields to each object.

Aggregation Functions:
- Count: Count objects
- Sum: Sum values
- Avg: Average values
- Min: Minimum value
- Max: Maximum value

Examples:
```python
from django.db.models import Count, Sum, Avg

# Count total posts
Post.objects.count()

# Count posts by author
Post.objects.values('author').annotate(
    post_count=Count('id')
)

# Sum prices
Product.objects.aggregate(total=Sum('price'))

# Average price
Product.objects.aggregate(avg_price=Avg('price'))
```

Annotations:
- Add computed fields to each object
- Useful for adding counts, sums, etc. to queryset results

Example:
```python
from django.db.models import Count

# Add comment count to each post
posts = Post.objects.annotate(
    comment_count=Count('comments')
)

# Now each post has comment_count attribute
for post in posts:
    print(post.comment_count)
```

Grouping:
- Use values() to group by fields
- Combine with annotations for grouped calculations''',
            'content_fa': '''تجمع‌ها محاسبات را روی QuerySetها انجام می‌دهند. حاشیه‌نویسی‌ها فیلدهای محاسبه شده را به هر شیء اضافه می‌کنند.

توابع تجمع:
- Count: شمارش اشیاء
- Sum: جمع مقادیر
- Avg: میانگین مقادیر
- Min: حداقل مقدار
- Max: حداکثر مقدار

مثال‌ها:
```python
from django.db.models import Count, Sum, Avg

# شمارش کل پست‌ها
Post.objects.count()

# شمارش پست‌ها بر اساس نویسنده
Post.objects.values('author').annotate(
    post_count=Count('id')
)

# جمع قیمت‌ها
Product.objects.aggregate(total=Sum('price'))

# میانگین قیمت
Product.objects.aggregate(avg_price=Avg('price'))
```

حاشیه‌نویسی‌ها:
- فیلدهای محاسبه شده را به هر شیء اضافه می‌کنند
- مفید برای افزودن شمارش‌ها، جمع‌ها و غیره به نتایج queryset

مثال:
```python
from django.db.models import Count

# افزودن شمارش نظر به هر پست
posts = Post.objects.annotate(
    comment_count=Count('comments')
)

# حالا هر پست ویژگی comment_count دارد
for post in posts:
    print(post.comment_count)
```

گروه‌بندی:
- استفاده از values() برای گروه‌بندی بر اساس فیلدها
- ترکیب با حاشیه‌نویسی‌ها برای محاسبات گروه‌بندی شده''',
            'code_example': '''from django.db.models import Count, Sum, Avg, Max, Min

# Count
total_posts = Post.objects.count()

# Aggregate
stats = Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views_count')
)

# Annotate
posts_with_comments = Post.objects.annotate(
    comment_count=Count('comments')
)

# Group by
posts_by_author = Post.objects.values('author').annotate(
    post_count=Count('id')
)''',
            'code_example_windows': '''# In Python shell
python manage.py shell

from django.db.models import Count, Sum, Avg
from myapp.models import Post

# Count
total_posts = Post.objects.count()

# Aggregate
stats = Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views_count')
)

# Annotate
posts_with_comments = Post.objects.annotate(
    comment_count=Count('comments')
)

# Group by
posts_by_author = Post.objects.values('author').annotate(
    post_count=Count('id')
)''',
            'code_example_mac': '''# In Python shell
python manage.py shell

from django.db.models import Count, Sum, Avg
from myapp.models import Post

# Count
total_posts = Post.objects.count()

# Aggregate
stats = Post.objects.aggregate(
    total=Count('id'),
    avg_views=Avg('views_count')
)

# Annotate
posts_with_comments = Post.objects.annotate(
    comment_count=Count('comments')
)

# Group by
posts_by_author = Post.objects.values('author').annotate(
    post_count=Count('id')
)''',
            'exercise_en': 'Write a QuerySet that annotates each Post with the count of its comments and orders them by comment count descending.',
            'exercise_fa': 'یک QuerySet بنویسید که هر Post را با شمارش نظراتش حاشیه‌نویسی می‌کند و آنها را به ترتیب شمارش نظر نزولی مرتب می‌کند.',
            'exercise_solution': '''from django.db.models import Count

posts = Post.objects.annotate(
    comment_count=Count('comments')
).order_by('-comment_count')''',
            'order': 5
        },
        {
            'slug': 'custom-managers',
            'title_en': 'Custom Managers and QuerySets',
            'title_fa': 'Managerها و QuerySetهای سفارشی',
            'content_en': '''Managers are the interface through which database query operations are provided to Django models. You can create custom managers for reusable query logic.

Default Manager:
- objects: Default manager for all models
- Can be overridden with custom manager

Custom Manager:
```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    
    objects = models.Manager()  # Default manager
    published_objects = PublishedManager()  # Custom manager
```

Custom QuerySet:
```python
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def recent(self):
        return self.filter(created_at__gte=timezone.now() - timedelta(days=7))

class Post(models.Model):
    objects = PostQuerySet.as_manager()
```

Benefits:
- Reusable query logic
- Cleaner code
- Better organization
- Chainable methods''',
            'content_fa': '''Managerها رابطی هستند که از طریق آن عملیات پرس‌وجوی پایگاه داده به مدل‌های جنگو ارائه می‌شوند. می‌توانید managerهای سفارشی برای منطق کوئری قابل استفاده مجدد ایجاد کنید.

Manager پیش‌فرض:
- objects: Manager پیش‌فرض برای تمام مدل‌ها
- می‌تواند با manager سفارشی جایگزین شود

Manager سفارشی:
```python
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    
    objects = models.Manager()  # Manager پیش‌فرض
    published_objects = PublishedManager()  # Manager سفارشی
```

QuerySet سفارشی:
```python
class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def recent(self):
        return self.filter(created_at__gte=timezone.now() - timedelta(days=7))

class Post(models.Model):
    objects = PostQuerySet.as_manager()
```

مزایا:
- منطق کوئری قابل استفاده مجدد
- کد تمیزتر
- سازماندهی بهتر
- متدهای قابل زنجیره‌سازی''',
            'code_example': '''from django.db import models
from django.utils import timezone
from datetime import timedelta

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def recent(self):
        return self.filter(
            created_at__gte=timezone.now() - timedelta(days=7)
        )

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PostQuerySet.as_manager()
    
    def __str__(self):
        return self.title

# Usage:
# Post.objects.published()
# Post.objects.recent()
# Post.objects.published().recent()''',
            'code_example_windows': '''# In models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def recent(self):
        return self.filter(
            created_at__gte=timezone.now() - timedelta(days=7)
        )

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PostQuerySet.as_manager()
    
    def __str__(self):
        return self.title

# Usage in views or shell:
# Post.objects.published()
# Post.objects.recent()
# Post.objects.published().recent()''',
            'code_example_mac': '''# In models.py
from django.db import models
from django.utils import timezone
from datetime import timedelta

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def recent(self):
        return self.filter(
            created_at__gte=timezone.now() - timedelta(days=7)
        )

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = PostQuerySet.as_manager()
    
    def __str__(self):
        return self.title

# Usage in views or shell:
# Post.objects.published()
# Post.objects.recent()
# Post.objects.published().recent()''',
            'exercise_en': 'Create a custom QuerySet for the Post model with methods: published() to filter published posts, and popular() to filter posts with views_count > 100.',
            'exercise_fa': 'یک QuerySet سفارشی برای مدل Post با متدهای زیر ایجاد کنید: published() برای فیلتر کردن پست‌های منتشر شده، و popular() برای فیلتر کردن پست‌هایی با views_count > 100.',
            'exercise_solution': '''from django.db import models

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)
    
    def popular(self):
        return self.filter(views_count__gt=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    
    objects = PostQuerySet.as_manager()''',
            'order': 6
        },
        {
            'slug': 'model-inheritance',
            'title_en': 'Model Inheritance',
            'title_fa': 'وراثت مدل',
            'content_en': '''Django supports three types of model inheritance:

1. Abstract Base Classes:
- Base class is not a database table
- Fields are inherited by child classes
- Useful for common fields

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
```

2. Multi-table Inheritance:
- Each model has its own database table
- Child table has OneToOne link to parent
- Useful when you need separate tables

```python
class Place(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
```

3. Proxy Models:
- Same database table as parent
- Different Python behavior
- Useful for different admin interfaces or methods

```python
class Person(models.Model):
    name = models.CharField(max_length=50)

class MyPerson(Person):
    class Meta:
        proxy = True
    
    def do_something(self):
        # Custom method
        pass
```''',
            'content_fa': '''جنگو از سه نوع وراثت مدل پشتیبانی می‌کند:

1. کلاس‌های پایه انتزاعی:
- کلاس پایه یک جدول پایگاه داده نیست
- فیلدها توسط کلاس‌های فرزند به ارث برده می‌شوند
- مفید برای فیلدهای مشترک

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
```

2. وراثت چند جدولی:
- هر مدل جدول پایگاه داده خود را دارد
- جدول فرزند لینک OneToOne به والد دارد
- مفید وقتی نیاز به جداول جداگانه دارید

```python
class Place(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
```

3. مدل‌های Proxy:
- همان جدول پایگاه داده با والد
- رفتار پایتون متفاوت
- مفید برای رابط‌های admin یا متدهای متفاوت

```python
class Person(models.Model):
    name = models.CharField(max_length=50)

class MyPerson(Person):
    class Meta:
        proxy = True
    
    def do_something(self):
        # متد سفارشی
        pass
```''',
            'code_example': '''from django.db import models

# Abstract base class
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# Proxy model
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

class MyPerson(Person):
    class Meta:
        proxy = True
    
    def is_adult(self):
        return self.age >= 18''',
            'code_example_windows': '''# In models.py
from django.db import models

# Abstract base class
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'code_example_mac': '''# In models.py
from django.db import models

# Abstract base class
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

# Multi-table inheritance
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

# Create and apply migrations
python manage.py makemigrations
python manage.py migrate''',
            'exercise_en': 'Create an abstract base class called BaseModel with created_at and updated_at fields, then create a Product model that inherits from it.',
            'exercise_fa': 'یک کلاس پایه انتزاعی با نام BaseModel با فیلدهای created_at و updated_at ایجاد کنید، سپس یک مدل Product ایجاد کنید که از آن به ارث می‌برد.',
            'exercise_solution': '''from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)''',
            'order': 7
        }
    ]
}

