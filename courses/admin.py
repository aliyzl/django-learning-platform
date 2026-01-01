from django.contrib import admin
from .models import Course, Section, Lesson, UserProgress


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_fa', 'platform', 'order', 'is_active', 'created_at']
    list_filter = ['platform', 'is_active', 'created_at']
    search_fields = ['title_en', 'title_fa', 'description_en', 'description_fa']
    prepopulated_fields = {'slug': ('title_en',)}


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_fa', 'course', 'order', 'created_at']
    list_filter = ['course', 'created_at']
    search_fields = ['title_en', 'title_fa']
    prepopulated_fields = {'slug': ('title_en',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_fa', 'section', 'order', 'content_type', 'created_at']
    list_filter = ['section__course', 'content_type', 'created_at']
    search_fields = ['title_en', 'title_fa', 'content_en', 'content_fa']
    prepopulated_fields = {'slug': ('title_en',)}


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'completed', 'completed_at', 'last_accessed']
    list_filter = ['completed', 'completed_at']
    search_fields = ['user__username', 'lesson__title_en', 'lesson__title_fa']
