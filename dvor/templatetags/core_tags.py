from django import template
from..forms import MainCalc

register = template.Library()

@register.assignment_tag
def get_calc_form():
    return MainCalc()