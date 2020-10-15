from django import template
from django.templatetags import static

register = template.Library()

@register.simple_tag
def static_symbol(symbol_name):
    return static.static('images/symbols/svg/symbol-%s.svg' % symbol_name)
