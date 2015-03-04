# -*- coding: utf-8 -*-
from django.template import Library, TemplateSyntaxError

register = Library()


@register.filter
def rupluralize(count, arg):
    """
    {{ count }} пользовател{% count|rupluralize:"ь,я,ей" %}
    """
    forms = arg.split(',')
    try:
        if len(forms) < 3:
            raise TemplateSyntaxError('Not enough word forms')
        value = int(count) % 100
        form = 2 if (10 <= value <= 20) or value % 10 >= 5 or value % 10 == 0 else (0 if value % 10 == 1 else 1)
        return forms[form]
    except:
        return forms[0]
