from django.shortcuts import render
from django.utils import translation
from courses.models import Course, Lesson, Section


def get_current_language(request):
    """Get current language from session or default"""
    return request.session.get('language', translation.get_language())


def landing_page(request):
    """Display Django framework landing page"""
    lang = get_current_language(request)
    
    # Get statistics for the landing page
    total_courses = Course.objects.filter(is_active=True).count()
    total_sections = Section.objects.count()
    total_lessons = Lesson.objects.count()
    
    context = {
        'lang': lang,
        'total_courses': total_courses,
        'total_sections': total_sections,
        'total_lessons': total_lessons,
    }
    return render(request, 'landing.html', context)
