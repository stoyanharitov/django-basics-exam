from django import template
from reg_exam_main.utils import get_active_user

register = template.Library()

@register.simple_tag
def get_user():
    return get_active_user()