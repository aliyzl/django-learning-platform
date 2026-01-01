import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Section, Lesson

def verify_data():
    course = Course.objects.first()
    if not course:
        print("No courses found. Creating a test course...")
        course = Course.objects.create(
            title_en="Test Course",
            title_fa="Test Course FA",
            description_en="A test course description",
            description_fa="A test course description FA",
            slug="test-course",
            platform="all"
        )
    
    section = Section.objects.filter(course=course).first()
    if not section:
        print("No sections found. Creating a test section...")
        section = Section.objects.create(
            course=course,
            title_en="Test Section",
            title_fa="Test Section FA",
            slug="test-section",
            order=1
        )
        
    lesson = Lesson.objects.filter(section=section).first()
    if not lesson:
        print("No lessons found. Creating a test lesson...")
        lesson = Lesson.objects.create(
            section=section,
            title_en="Test Lesson",
            title_fa="Test Lesson FA",
            content_en="This is test lesson content.",
            content_fa="This is test lesson content FA.",
            slug="test-lesson",
            order=1,
            code_example="print('Hello World')"
        )
        
    print(f"Course Slug: {course.slug}")
    print(f"Section Slug: {section.slug}")
    print(f"Lesson Slug: {lesson.slug}")
    print(f"Lesson URL: {lesson.get_absolute_url()}")

if __name__ == "__main__":
    verify_data()
