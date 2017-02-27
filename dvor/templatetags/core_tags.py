from django import template
from..forms import MainCalc, PrjCalc, FundCalc, PhoneForm

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