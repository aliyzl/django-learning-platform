from courses.models import Lesson


def extract_lesson_context(lesson_id, lang='en'):
    """
    Extract comprehensive context from a lesson for AI assistant
    
    Args:
        lesson_id: ID of the lesson
        lang: Language code ('en' or 'fa')
    
    Returns:
        dict: Context information
    """
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        return {
            'title': lesson.get_title(lang),
            'content': lesson.get_content(lang),
            'code_example': lesson.code_example,
            'code_example_windows': lesson.code_example_windows,
            'code_example_mac': lesson.code_example_mac,
            'exercise': lesson.get_exercise(lang),
            'exercise_solution': lesson.exercise_solution,
            'section_title': lesson.section.get_title(lang),
            'course_title': lesson.section.course.get_title(lang),
            'content_type': lesson.content_type,
        }
    except Lesson.DoesNotExist:
        return None


def build_context_prompt(lesson_context, user_question):
    """
    Build a context-aware prompt for the AI
    
    Args:
        lesson_context: Dictionary with lesson information
        user_question: User's question
    
    Returns:
        str: Formatted prompt
    """
    if not lesson_context:
        return f"User Question: {user_question}"
    
    prompt = f"""You are helping a student learn Django. They are currently studying:

Course: {lesson_context['course_title']}
Section: {lesson_context['section_title']}
Lesson: {lesson_context['title']}

Lesson Content Summary:
{lesson_context['content'][:800]}

"""
    
    if lesson_context['code_example']:
        prompt += f"Code Example:\n{lesson_context['code_example'][:500]}\n\n"
    
    if lesson_context['exercise']:
        prompt += f"Exercise:\n{lesson_context['exercise'][:500]}\n\n"
    
    prompt += f"User Question: {user_question}\n\n"
    prompt += "Please provide a helpful answer in the context of this lesson. If the question is general, you can still answer it."
    
    return prompt




