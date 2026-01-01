from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils import translation
import json
from .services import generate_ai_response
from .utils import extract_lesson_context, build_context_prompt


@login_required
@require_http_methods(["POST"])
def chat(request):
    """Handle AI chat requests"""
    try:
        data = json.loads(request.body)
        user_question = data.get('question', '').strip()
        lesson_id = data.get('lesson_id')
        chat_history = data.get('history', [])
        
        if not user_question:
            return JsonResponse({
                'success': False,
                'error': 'Question is required'
            }, status=400)
        
        # Get current language
        lang = request.session.get('language', translation.get_language())
        
        # Generate response
        response_text = generate_ai_response(
            user_question=user_question,
            lesson_id=lesson_id,
            chat_history=chat_history
        )
        
        return JsonResponse({
            'success': True,
            'response': response_text,
            'question': user_question
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@login_required
@require_http_methods(["GET"])
def get_lesson_context_api(request, lesson_id):
    """Get lesson context for AI assistant"""
    lang = request.session.get('language', translation.get_language())
    context = extract_lesson_context(lesson_id, lang)
    
    if not context:
        return JsonResponse({
            'success': False,
            'error': 'Lesson not found'
        }, status=404)
    
    return JsonResponse({
        'success': True,
        'context': context
    })
