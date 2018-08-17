#https://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables

from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.simple_tag()
def get_attribute(context, arg):
    return getattr(context, arg)
