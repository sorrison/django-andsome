from django import template
from django.utils.safestring import mark_safe
from django_common.util.filterspecs import get_query_string

register = template.Library()

DOT = '.'

def paginator_number(page, i, qs):

    qs['p'] = i
    
    if i == DOT:
        return u'... '
    elif i == page.number:
        return mark_safe(u'<span class="this-page">%d</span> ' % (i))
    else:
        return mark_safe(u'<a href="%s"%s>%d</a> ' % ((get_query_string(qs)), (i == page.paginator.num_pages and ' class="end"' or ''), i))
paginator_number = register.simple_tag(paginator_number)

def pagination(page, request):
    
    tqs = request.META['QUERY_STRING']
    qs = {}
    tqs = tqs.split('&')
    for q in tqs:
        k, v = q.split('=')
        qs[k] = v
    pagination_required = False
    if page.paginator.num_pages > 1:
        pagination_required = True

    return {
        'page': page,
        'pagination_required': pagination_required,
        'qs': qs,
    }
pagination = register.inclusion_tag('pagination.html')(pagination)
