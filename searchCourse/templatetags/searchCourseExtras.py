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

#Set color of the criterion card background and font based on the cards
#score. This may be misuse of Bootstraps color palette.
@register.simple_tag()
def set_color(score):
    textBSColor = "text-light"
    if not score:
        textBSColor = "text-dark"
        return textBSColor+" bg-light"
    score = Decimal(score)
    if score <= 1.7:
        return textBSColor+" bg-danger"
    elif score <= 3.3:
        return textBSColor+" bg-warning"
    else:
        return textBSColor+" bg-success"
        

