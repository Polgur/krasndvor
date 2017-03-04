import re
from django import template
from..forms import MainCalc, PrjCalc, FundCalc, PhoneForm
from django.utils.encoding import force_text

register = template.Library()

@register.assignment_tag
def get_calc_form():
    return MainCalc()

@register.assignment_tag
def get_prjc_form():
    return PrjCalc()

@register.assignment_tag
def get_fundc_form():
    return FundCalc()

@register.assignment_tag
def get_phone_form():
    return PhoneForm()

@register.filter('intspace')
def intspace(value):
    orig = force_text(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1> \g<2>', orig)
    if orig == new:
        return new
    else:
        return intspace(new)