from django import template
from django.contrib.staticfiles.templatetags import staticfiles

register = template.Library()

@register.simple_tag
def static_symbol(symbol_name):
    return staticfiles.static('images/symbols/svg/symbol-%s.svg' % symbol_name)
