from django.utils import translation
from django.conf import settings


class LanguageMiddleware:
    """Middleware to handle language switching via session or request parameter"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check for language parameter in request
        lang_code = request.GET.get('lang') or request.session.get('language', settings.LANGUAGE_CODE)
        
        # Validate language code
        if lang_code in dict(settings.LANGUAGES):
            request.session['language'] = lang_code
            translation.activate(lang_code)
        else:
            translation.activate(settings.LANGUAGE_CODE)
        
        response = self.get_response(request)
        
        # Deactivate translation after response
        translation.deactivate()
        
        return response




