from django.core.management.base import BaseCommand
from courses.models import Course, Section, Lesson

# Import all section data files
from .course_data.section_01_getting_started import SECTION_DATA as SECTION_01
from .course_data.section_02_django_basics import SECTION_DATA as SECTION_02
from .course_data.section_03_models_databases import SECTION_DATA as SECTION_03
from .course_data.section_04_views_routing import SECTION_DATA as SECTION_04
from .course_data.section_05_templates import SECTION_DATA as SECTION_05
from .course_data.section_06_forms import SECTION_DATA as SECTION_06
from .course_data.section_07_authentication import SECTION_DATA as SECTION_07
from .course_data.section_08_admin import SECTION_DATA as SECTION_08
from .course_data.section_09_testing import SECTION_DATA as SECTION_09
from .course_data.section_10_security import SECTION_DATA as SECTION_10
from .course_data.section_11_performance import SECTION_DATA as SECTION_11
from .course_data.section_12_rest_apis import SECTION_DATA as SECTION_12
from .course_data.section_13_deployment import SECTION_DATA as SECTION_13
from .course_data.section_14_advanced import SECTION_DATA as SECTION_14


class Command(BaseCommand):
    help = 'Create comprehensive Django course content'

    def handle(self, *args, **options):
        self.stdout.write('Creating Django course content...')
        
        # Create main course
        course, created = Course.objects.get_or_create(
            slug='django-master',
            defaults={
                'title_en': 'Django Master: From Zero to Master',
                'title_fa': 'جنگو مستر: از صفر تا استادی',
                'description_en': 'Complete Django course covering everything from installation to advanced topics. Learn Django for both Windows and Mac platforms.',
                'description_fa': 'دوره کامل جنگو که همه چیز را از نصب تا موضوعات پیشرفته پوشش می‌دهد. جنگو را برای پلتفرم‌های ویندوز و مک بیاموزید.',
                'order': 1,
                'is_active': True,
                'platform': 'all'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created course: {course.title_en}'))
        else:
            self.stdout.write(f'Course already exists: {course.title_en}')
        
        # Collect all section data
        sections_data = [
            SECTION_01, SECTION_02, SECTION_03, SECTION_04, SECTION_05,
            SECTION_06, SECTION_07, SECTION_08, SECTION_09, SECTION_10,
            SECTION_11, SECTION_12, SECTION_13, SECTION_14
        ]
        
        # Create sections and lessons
        for section_data in sections_data:
            section, created = Section.objects.get_or_create(
                course=course,
                slug=section_data['slug'],
                defaults={
                    'title_en': section_data['title_en'],
                    'title_fa': section_data['title_fa'],
                    'description_en': section_data['description_en'],
                    'description_fa': section_data['description_fa'],
                    'order': sections_data.index(section_data) + 1
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created section: {section.title_en}'))
            else:
                self.stdout.write(f'Section already exists: {section.title_en}')
            
            # Create lessons for this section
            for lesson_data in section_data['lessons']:
                lesson, created = Lesson.objects.get_or_create(
                    section=section,
                    slug=lesson_data['slug'],
                    defaults={
                        'title_en': lesson_data['title_en'],
                        'title_fa': lesson_data['title_fa'],
                        'content_en': lesson_data['content_en'],
                        'content_fa': lesson_data['content_fa'],
                        'code_example': lesson_data.get('code_example', ''),
                        'code_example_windows': lesson_data.get('code_example_windows', ''),
                        'code_example_mac': lesson_data.get('code_example_mac', ''),
                        'exercise_en': lesson_data.get('exercise_en', ''),
                        'exercise_fa': lesson_data.get('exercise_fa', ''),
                        'exercise_solution': lesson_data.get('exercise_solution', ''),
                        'order': lesson_data['order']
                    }
                )
                
                if created:
                    self.stdout.write(f'  Created lesson: {lesson.title_en}')
        
        self.stdout.write(self.style.SUCCESS('Course content created successfully!'))
        self.stdout.write(f'Total sections: {len(sections_data)}')
        total_lessons = sum(len(s['lessons']) for s in sections_data)
        self.stdout.write(f'Total lessons: {total_lessons}')
