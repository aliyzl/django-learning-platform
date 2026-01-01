"""
Section 6: Forms
Django forms, validation, ModelForms, and form handling
"""

SECTION_DATA = {
    'slug': 'forms',
    'title_en': 'Forms',
    'title_fa': 'فرم‌ها',
    'description_en': 'Master Django forms: creation, validation, ModelForms, and form handling',
    'description_fa': 'تسلط بر فرم‌های جنگو: ایجاد، اعتبارسنجی، ModelForms و مدیریت فرم',
    'lessons': [
        {
            'slug': 'forms-basics',
            'title_en': 'Django Forms Basics',
            'title_fa': 'مبانی فرم‌های جنگو',
            'content_en': '''Django forms handle form rendering, validation, and data processing.

Creating a Form:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

Form Fields:
- CharField: Text input
- EmailField: Email validation
- IntegerField: Integer input
- BooleanField: Checkbox
- ChoiceField: Dropdown
- DateField: Date picker
- FileField: File upload

Rendering Forms:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

Processing Forms:
```python
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data
            name = form.cleaned_data['name']
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```''',
            'content_fa': '''فرم‌های جنگو رندر کردن فرم، اعتبارسنجی و پردازش داده را مدیریت می‌کنند.

ایجاد یک فرم:
```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

فیلدهای فرم:
- CharField: ورودی متن
- EmailField: اعتبارسنجی ایمیل
- IntegerField: ورودی عدد صحیح
- BooleanField: چک‌باکس
- ChoiceField: منوی کشویی
- DateField: انتخابگر تاریخ
- FileField: آپلود فایل

رندر کردن فرم‌ها:
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">ارسال</button>
</form>
```

پردازش فرم‌ها:
```python
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # پردازش داده فرم
            name = form.cleaned_data['name']
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
```''',
            'code_example': '''from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Message')

# In views.py
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Process data
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})''',
            'code_example_windows': '''# In forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# In views.py
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# In template contact.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>''',
            'code_example_mac': '''# In forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

# In views.py
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# In template contact.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>''',
            'exercise_en': 'Create a registration form with fields: username, email, password, and confirm_password. Add validation to ensure passwords match.',
            'exercise_fa': 'یک فرم ثبت‌نام با فیلدهای username، email، password و confirm_password ایجاد کنید. اعتبارسنجی اضافه کنید تا مطمئن شوید رمزهای عبور مطابقت دارند.',
            'exercise_solution': '''from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data''',
            'order': 1
        },
        {
            'slug': 'modelforms',
            'title_en': 'ModelForms',
            'title_fa': 'ModelForms',
            'content_en': '''ModelForms automatically generate forms from models.

Creating ModelForm:
```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
```

Benefits:
- Automatic field generation
- Validation based on model
- Save directly to database
- Less code

Excluding Fields:
```python
class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['created_at']
```

Customizing Fields:
```python
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10})
        }
```

Using ModelForm:
```python
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
```''',
            'content_fa': '''ModelForms به طور خودکار فرم‌ها را از مدل‌ها تولید می‌کنند.

ایجاد ModelForm:
```python
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
```

مزایا:
- تولید خودکار فیلدها
- اعتبارسنجی بر اساس مدل
- ذخیره مستقیم در پایگاه داده
- کد کمتر

حذف فیلدها:
```python
class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['created_at']
```

سفارشی‌سازی فیلدها:
```python
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10})
        }
```

استفاده از ModelForm:
```python
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
```''',
            'code_example': '''from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10})
        }

# In views.py
from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})''',
            'code_example_windows': '''# In forms.py
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# In views.py
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})''',
            'code_example_mac': '''# In forms.py
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# In views.py
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})''',
            'exercise_en': 'Create a ModelForm for the Book model with fields: title, author, and price. Use it in a view to create new books.',
            'exercise_fa': 'یک ModelForm برای مدل Book با فیلدهای title، author و price ایجاد کنید. از آن در یک view برای ایجاد کتاب‌های جدید استفاده کنید.',
            'exercise_solution': '''from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']

# In views.py
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'create_book.html', {'form': form})''',
            'order': 2
        },
        {
            'slug': 'form-validation',
            'title_en': 'Form Validation',
            'title_fa': 'اعتبارسنجی فرم',
            'content_en': '''Django provides multiple levels of form validation.

Field-Level Validation:
```python
class ContactForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if 'spam' in email:
            raise forms.ValidationError("Spam emails not allowed")
        return email
```

Form-Level Validation:
```python
def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm = cleaned_data.get('confirm_password')
    if password != confirm:
        raise forms.ValidationError("Passwords don't match")
    return cleaned_data
```

Validation Errors:
- Display in template: {{ form.errors }}
- Field-specific: {{ form.field_name.errors }}
- Non-field errors: {{ form.non_field_errors }}

Custom Validators:
```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('Must be even number')

class MyForm(forms.Form):
    number = forms.IntegerField(validators=[validate_even])
```''',
            'content_fa': '''جنگو سطوح متعددی از اعتبارسنجی فرم ارائه می‌دهد.

اعتبارسنجی سطح فیلد:
```python
class ContactForm(forms.Form):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if 'spam' in email:
            raise forms.ValidationError("ایمیل‌های اسپم مجاز نیستند")
        return email
```

اعتبارسنجی سطح فرم:
```python
def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm = cleaned_data.get('confirm_password')
    if password != confirm:
        raise forms.ValidationError("رمزهای عبور مطابقت ندارند")
    return cleaned_data
```

خطاهای اعتبارسنجی:
- نمایش در قالب: {{ form.errors }}
- خاص فیلد: {{ form.field_name.errors }}
- خطاهای غیر فیلد: {{ form.non_field_errors }}

اعتبارسنج‌های سفارشی:
```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError('باید عدد زوج باشد')

class MyForm(forms.Form):
    number = forms.IntegerField(validators=[validate_even])
```''',
            'code_example': '''from django import forms
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError('Must be positive')

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(validators=[validate_positive])
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name too short")
        return name

# In template
{% if form.errors %}
    <ul>
    {% for error in form.errors %}
        <li>{{ error }}</li>
    {% endfor %}
    </ul>
{% endif %}''',
            'code_example_windows': '''# In forms.py
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name too short")
        return name

# In template
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    {% if form.errors %}
        <div class="errors">{{ form.errors }}</div>
    {% endif %}
    <button type="submit">Submit</button>
</form>''',
            'code_example_mac': '''# In forms.py
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField()
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError("Name too short")
        return name

# In template
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    {% if form.errors %}
        <div class="errors">{{ form.errors }}</div>
    {% endif %}
    <button type="submit">Submit</button>
</form>''',
            'exercise_en': 'Create a form with a price field and add validation to ensure the price is greater than 0.',
            'exercise_fa': 'یک فرم با فیلد price ایجاد کنید و اعتبارسنجی اضافه کنید تا مطمئن شوید قیمت بیشتر از 0 است.',
            'exercise_solution': '''from django import forms
from django.core.exceptions import ValidationError

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField()
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price and price <= 0:
            raise forms.ValidationError("Price must be greater than 0")
        return price''',
            'order': 3
        },
        {
            'slug': 'file-uploads',
            'title_en': 'File Uploads',
            'title_fa': 'آپلود فایل',
            'content_en': '''Django handles file uploads through forms.

Form with File Upload:
```python
class DocumentForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
```

Model with FileField:
```python
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
```

Handling Uploads:
```python
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document()
            document.title = form.cleaned_data['title']
            document.file = request.FILES['file']
            document.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
```

Template:
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

Important:
- Use enctype="multipart/form-data" in form
- Access files via request.FILES
- Configure MEDIA_URL and MEDIA_ROOT in settings''',
            'content_fa': '''جنگو آپلود فایل‌ها را از طریق فرم‌ها مدیریت می‌کند.

فرم با آپلود فایل:
```python
class DocumentForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
```

مدل با FileField:
```python
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
```

مدیریت آپلودها:
```python
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document()
            document.title = form.cleaned_data['title']
            document.file = request.FILES['file']
            document.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})
```

قالب:
```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">آپلود</button>
</form>
```

مهم:
- استفاده از enctype="multipart/form-data" در فرم
- دسترسی به فایل‌ها از طریق request.FILES
- پیکربندی MEDIA_URL و MEDIA_ROOT در settings''',
            'code_example': '''# In models.py
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

# In forms.py
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

# In views.py
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

# In template
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>''',
            'code_example_windows': '''# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In models.py
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

# In forms.py
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

# In views.py
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})''',
            'code_example_mac': '''# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In models.py
class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

# In forms.py
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file']

# In views.py
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})''',
            'exercise_en': 'Create a form that allows users to upload an image file. Configure MEDIA settings and handle the file upload in the view.',
            'exercise_fa': 'یک فرم ایجاد کنید که به کاربران امکان آپلود فایل تصویر را می‌دهد. تنظیمات MEDIA را پیکربندی کنید و آپلود فایل را در view مدیریت کنید.',
            'exercise_solution': '''# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# In models.py
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

# In forms.py
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

# In views.py
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})''',
            'order': 4
        }
    ]
}

