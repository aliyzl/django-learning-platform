from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.db.models import Q
from .models import Course, Section, Lesson, UserProgress
import json


def get_current_language(request):
    """Get current language from session or default"""
    return request.session.get('language', translation.get_language())


def course_list(request):
    """Display list of all courses grouped by platform"""
    lang = get_current_language(request)
    all_courses = Course.objects.filter(is_active=True)
    
    # Group courses by platform
    mac_courses = all_courses.filter(platform='mac')
    windows_courses = all_courses.filter(platform='windows')
    all_platforms_courses = all_courses.filter(platform='all')
    
    # Calculate total count
    total_courses = all_courses.count()
    
    context = {
        'mac_courses': mac_courses,
        'windows_courses': windows_courses,
        'all_platforms_courses': all_platforms_courses,
        'total_courses': total_courses,
        'lang': lang,
    }
    return render(request, 'courses/course_list.html', context)


def course_detail(request, course_slug):
    """Display course detail with sections"""
    lang = get_current_language(request)
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    # Use prefetch_related to avoid N+1 queries when accessing lessons
    sections = course.sections.prefetch_related('lessons').all()
    
    context = {
        'course': course,
        'sections': sections,
        'lang': lang,
    }
    return render(request, 'courses/course_detail.html', context)


def lesson_detail(request, course_slug, section_slug, lesson_slug):
    """Display individual lesson"""
    lang = get_current_language(request)

    # Use select_related to fetch related course and section in a single query
    course = get_object_or_404(Course, slug=course_slug, is_active=True)
    section = get_object_or_404(
        Section.objects.select_related('course'),
        course=course,
        slug=section_slug
    )
    lesson = get_object_or_404(
        Lesson.objects.select_related('section', 'section__course'),
        section=section,
        slug=lesson_slug
    )

    # Get previous and next lessons efficiently using database queries
    # instead of loading all lessons into memory
    prev_lesson = (
        Lesson.objects
        .filter(section=section, order__lt=lesson.order)
        .order_by('-order')
        .only('id', 'slug', 'title_en', 'title_fa', 'order')
        .first()
    )

    next_lesson = (
        Lesson.objects
        .filter(section=section, order__gt=lesson.order)
        .order_by('order')
        .only('id', 'slug', 'title_en', 'title_fa', 'order')
        .first()
    )
    
    # Get user progress if authenticated
    user_progress = None
    if request.user.is_authenticated:
        user_progress, _ = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson
        )
    
    # Detect platform from user agent
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    platform = 'mac' if 'mac' in user_agent else 'windows' if 'windows' in user_agent else 'default'
    
    context = {
        'course': course,
        'section': section,
        'lesson': lesson,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'user_progress': user_progress,
        'platform': platform,
        'lang': lang,
    }
    return render(request, 'courses/lesson_detail.html', context)


@login_required
@require_http_methods(["POST"])
def update_progress(request, lesson_id):
    """Update user progress for a lesson"""
    try:
        lesson = get_object_or_404(Lesson, id=lesson_id)

        # Parse JSON with proper error handling
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON format'
            }, status=400)

        completed = data.get('completed', False)

        # Validate completed is a boolean
        if not isinstance(completed, bool):
            return JsonResponse({
                'success': False,
                'error': 'completed must be a boolean value'
            }, status=400)

        # Use update_or_create to avoid race condition
        from django.utils import timezone
        defaults = {'completed': completed}
        if completed:
            defaults['completed_at'] = timezone.now()

        user_progress, created = UserProgress.objects.update_or_create(
            user=request.user,
            lesson=lesson,
            defaults=defaults
        )

        return JsonResponse({
            'success': True,
            'completed': user_progress.completed
        })

    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error updating progress for lesson {lesson_id}: {str(e)}")
        return JsonResponse({
            'success': False,
            'error': 'An error occurred while updating progress'
        }, status=500)


@require_http_methods(["GET"])
def api_lesson_content(request, lesson_id):
    """API endpoint to get lesson content for AI context"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    lang = get_current_language(request)
    
    return JsonResponse({
        'title': lesson.get_title(lang),
        'content': lesson.get_content(lang),
        'code_example': lesson.code_example,
        'exercise': lesson.get_exercise(lang),
        'section_title': lesson.section.get_title(lang),
        'course_title': lesson.section.course.get_title(lang),
    })
