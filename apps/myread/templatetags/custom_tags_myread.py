from django import template
from apps.core.constance import BOOK_CATEGORY, BOOK_FORMAT

register = template.Library()

@register.filter
def semi_colon_seperator(value):
    return value.replace(', ','; ')

@register.filter
def extract_values(value):
    return ', '.join(str(tag) for tag in value.all())

@register.filter
def extract_constance(value):
    if value in BOOK_CATEGORY:
        value = BOOK_CATEGORY.get(value)
    elif value in BOOK_FORMAT:
        value = BOOK_FORMAT.get(value)
    return value
