from django import template

register = template.Library()

@register.filter
def first_three_words(value):
    words = value.split()

    if len(words) <= 3:
        return value
    return ' '.join(words[:3])