#https://stackoverflow.com/questions/2047622/how-to-paginate-django-with-other-get-variables

from django import template
from urllib.parse import urlencode
from decimal import Decimal

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

#Get attribute of an object, and normalize the attribute if it's a float
@register.simple_tag()
def get_attribute(context, arg):
    attribute = getattr(context, arg)
    if isinstance(attribute,float):
        attribute = Decimal(attribute).normalize()
    return attribute
