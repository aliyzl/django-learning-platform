from django import template

register = template.Library()


@register.filter
def get_translated(obj, lang):
    """
    Get the translated field value for an object based on language.

    Usage: {{ obj|get_translated:lang }}

    Returns:
    - obj.title_fa or obj.title_en based on language
    - obj.description_fa or obj.description_en based on language
    - obj.content_fa or obj.content_en based on language
    - obj.exercise_fa or obj.exercise_en based on language
    """
    if not obj:
        return ""

    if lang == 'fa':
        # Try to get the Farsi version first
        for attr in ['title_fa', 'description_fa', 'content_fa', 'exercise_fa']:
            if hasattr(obj, attr):
                return getattr(obj, attr, "")
    else:
        # Default to English version
        for attr in ['title_en', 'description_en', 'content_en', 'exercise_en']:
            if hasattr(obj, attr):
                return getattr(obj, attr, "")

    return ""


@register.filter
def get_field(obj, field_name):
    """
    Get a specific field's translated value based on current language.

    Usage: {{ obj|get_field:'title' }} (will use title_fa or title_en)
    """
    if not obj or not field_name:
        return ""

    lang = getattr(obj, '_template_lang', 'en')

    field_key = f"{field_name}_fa" if lang == 'fa' else f"{field_name}_en"
    return getattr(obj, field_key, "")
