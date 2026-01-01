try:
    import google.genai as genai
except ImportError:
    import google.generativeai as genai

from django.conf import settings
from courses.models import Lesson
import json
import logging

logger = logging.getLogger(__name__)


def get_gemini_client():
    """
    Initialize and return Gemini client with automatic fallback to multiple API keys.
    Tries each key in order until one succeeds.
    """
    api_keys = getattr(settings, 'GEMINI_API_KEYS', [])
    
    if not api_keys:
        # Fallback to single key for backward compatibility
        single_key = getattr(settings, 'GEMINI_API_KEY', '')
        if not single_key:
            raise ValueError("No GEMINI_API_KEY or GEMINI_API_KEYS configured in settings")
        api_keys = [single_key]
    
    last_error = None

    # Try each API key in order
    for index, api_key in enumerate(api_keys, 1):
        try:
            # Try new API first
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.0-flash-exp')
            logger.info(f"Successfully initialized Gemini client with API key {index}")
            return model
        except (ImportError, AttributeError) as e:
            # Configuration or API structure errors - these won't be fixed by trying another key
            logger.error(f"Fatal error initializing Gemini client: {str(e)}")
            raise ValueError(f"Gemini API configuration error: {str(e)}")
        except Exception as e:
            # API key specific errors - try next key
            last_error = e
            logger.warning(f"Failed to initialize Gemini client with API key {index}: {str(e)}")
            continue

    # If all keys failed, raise the last error
    raise ValueError(f"All API keys failed. Last error: {str(last_error)}")


def get_lesson_context(lesson_id):
    """Extract context from a lesson for AI assistant"""
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        context = {
            'title': lesson.title_en,
            'content': lesson.content_en,
            'code_example': lesson.code_example,
            'exercise': lesson.exercise_en,
            'section': lesson.section.title_en,
            'course': lesson.section.course.title_en,
        }
        return context
    except Lesson.DoesNotExist:
        return None


def generate_ai_response(user_question, lesson_id=None, chat_history=None):
    """
    Generate AI response using Gemini Flash 2.5 with automatic key fallback
    
    Args:
        user_question: The user's question
        lesson_id: Optional lesson ID for context-aware responses
        chat_history: Optional list of previous messages
    
    Returns:
        str: AI response
    """
    try:
        model = get_gemini_client()
        
        # Build context-aware prompt
        system_prompt = """You are a helpful Django learning assistant. You help students learn Django framework from zero to master level. 
        Provide clear, concise, and educational answers. If the user asks about a specific lesson, use the lesson context provided.
        Always be encouraging and provide practical examples when relevant."""
        
        # Add lesson context if available
        context_prompt = ""
        if lesson_id:
            lesson_context = get_lesson_context(lesson_id)
            if lesson_context:
                context_prompt = f"""
Current Lesson Context:
- Course: {lesson_context['course']}
- Section: {lesson_context['section']}
- Lesson: {lesson_context['title']}
- Content: {lesson_context['content'][:500]}...
- Code Example: {lesson_context['code_example'][:300] if lesson_context['code_example'] else 'None'}...
- Exercise: {lesson_context['exercise'][:300] if lesson_context['exercise'] else 'None'}...

Please answer the user's question in the context of this lesson. If the question is not related to this lesson, you can still answer it but mention that you're providing general Django knowledge.
"""
        
        # Build conversation history
        conversation = []
        if chat_history:
            for msg in chat_history[-5:]:  # Last 5 messages for context
                conversation.append({
                    'role': msg.get('role', 'user'),
                    'parts': [msg.get('content', '')]
                })
        
        # Add current question
        full_prompt = f"{system_prompt}\n\n{context_prompt}\n\nUser Question: {user_question}"
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        return response.text
        
    except ValueError as e:
        # API key configuration error
        logger.error(f"API key configuration error: {str(e)}")
        return "I apologize, but the AI service is not properly configured. Please contact the administrator."
    except (ConnectionError, TimeoutError) as e:
        # Network errors
        logger.error(f"Network error generating AI response: {str(e)}")
        return "I apologize, but I'm having trouble connecting to the AI service. Please check your internet connection and try again."
    except Exception as e:
        # Unexpected errors - log with traceback for debugging
        logger.exception(f"Unexpected error generating AI response: {str(e)}")
        return "I apologize, but I encountered an unexpected error. The issue has been logged and will be investigated."


def format_chat_message(role, content):
    """Format a chat message"""
    return {
        'role': role,
        'content': content,
        'timestamp': None  # Can add timestamp if needed
    }

