from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Course(models.Model):
    """Main course model"""
    PLATFORM_CHOICES = [
        ('all', _('All Platforms')),
        ('mac', _('Mac')),
        ('windows', _('Windows')),
    ]
    
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))
    title_fa = models.CharField(max_length=200, verbose_name=_('Title (Persian)'))
    description_en = models.TextField(verbose_name=_('Description (English)'))
    description_fa = models.TextField(verbose_name=_('Description (Persian)'))
    slug = models.SlugField(unique=True)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='all', verbose_name=_('Platform'))
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        indexes = [
            models.Index(fields=['is_active', 'platform'], name='course_active_platform_idx'),
            models.Index(fields=['platform', 'order'], name='course_platform_order_idx'),
        ]

    def __str__(self):
        return self.title_en

    def get_title(self, lang='en'):
        """Get title based on language"""
        return self.title_fa if lang == 'fa' else self.title_en

    def get_description(self, lang='en'):
        """Get description based on language"""
        return self.description_fa if lang == 'fa' else self.description_en


class Section(models.Model):
    """Section within a course"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))
    title_fa = models.CharField(max_length=200, verbose_name=_('Title (Persian)'))
    description_en = models.TextField(blank=True, verbose_name=_('Description (English)'))
    description_fa = models.TextField(blank=True, verbose_name=_('Description (Persian)'))
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['course', 'slug']
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

    def __str__(self):
        return f"{self.course.title_en} - {self.title_en}"

    def get_title(self, lang='en'):
        """Get title based on language"""
        return self.title_fa if lang == 'fa' else self.title_en

    def get_description(self, lang='en'):
        """Get description based on language"""
        return self.description_fa if lang == 'fa' else self.description_en


class Lesson(models.Model):
    """Individual lesson within a section"""
    CONTENT_TYPE_CHOICES = [
        ('text', _('Text')),
        ('code', _('Code Example')),
        ('exercise', _('Exercise')),
    ]

    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='lessons')
    title_en = models.CharField(max_length=200, verbose_name=_('Title (English)'))
    title_fa = models.CharField(max_length=200, verbose_name=_('Title (Persian)'))
    content_en = models.TextField(verbose_name=_('Content (English)'))
    content_fa = models.TextField(verbose_name=_('Content (Persian)'))
    code_example = models.TextField(blank=True, verbose_name=_('Code Example'))
    code_example_windows = models.TextField(blank=True, verbose_name=_('Windows Code Example'))
    code_example_mac = models.TextField(blank=True, verbose_name=_('Mac Code Example'))
    exercise_en = models.TextField(blank=True, verbose_name=_('Exercise (English)'))
    exercise_fa = models.TextField(blank=True, verbose_name=_('Exercise (Persian)'))
    exercise_solution = models.TextField(blank=True, verbose_name=_('Exercise Solution'))
    slug = models.SlugField()
    order = models.IntegerField(default=0)
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='text')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['section', 'slug']
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')

    def __str__(self):
        return f"{self.section.title_en} - {self.title_en}"

    def get_title(self, lang='en'):
        """Get title based on language"""
        return self.title_fa if lang == 'fa' else self.title_en

    def get_content(self, lang='en'):
        """Get content based on language"""
        return self.content_fa if lang == 'fa' else self.content_en

    def get_exercise(self, lang='en'):
        """Get exercise based on language"""
        return self.exercise_fa if lang == 'fa' else self.exercise_en

    def get_code_example(self, platform='default'):
        """Get code example based on platform"""
        if platform == 'windows' and self.code_example_windows:
            return self.code_example_windows
        elif platform == 'mac' and self.code_example_mac:
            return self.code_example_mac
        return self.code_example

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={
            'course_slug': self.section.course.slug,
            'section_slug': self.section.slug,
            'lesson_slug': self.slug
        })


class UserProgress(models.Model):
    """Track user progress through lessons"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='user_progress')
    completed = models.BooleanField(default=False, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    last_accessed = models.DateTimeField(auto_now=True, db_index=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['user', 'lesson']
        verbose_name = _('User Progress')
        verbose_name_plural = _('User Progress')
        indexes = [
            models.Index(fields=['user', 'completed'], name='user_progress_user_completed_idx'),
            models.Index(fields=['last_accessed'], name='user_progress_accessed_idx'),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title_en}"
