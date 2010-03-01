from django.template import Library
from django.conf import settings
from django import template

register = Library()


@register.inclusion_tag('gmaps/head.html')
def gmaps_head(longitude, latitude):
    api_key = settings.GMAP_KEY
    return locals()


@register.inclusion_tag('gmaps/body.html')
def gmaps_body(width=500, height=300):
    return locals()


