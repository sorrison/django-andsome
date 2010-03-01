# Copyright 2010 VPAC
#
# This file is part of django-andsom.
#
# django-andsome is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-andsome is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-andsome  If not, see <http://www.gnu.org/licenses/>.


from django import template
from django.utils.safestring import mark_safe
from django.core.paginator import QuerySetPaginator
from django_common.util.filterspecs import get_query_string

register = template.Library()

DOT = '.'

def paginator_number(page, i, qs):

    qs['page'] = i
    
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
    try:
        tqs = tqs.split('&')
        for q in tqs:
            k, v = q.split('=')
            qs[k] = v
    except:
        pass
    pagination_required = False
    if page.paginator.num_pages > 1:
        pagination_required = True
        
    if page.paginator.count == 1:
        object_name = 'object'
    else:
        object_name = 'objects'

    if isinstance(page.paginator, QuerySetPaginator):
        if page.paginator.count == 1:
            object_name = page.paginator.object_list.model._meta.verbose_name
        else:
            object_name = page.paginator.object_list.model._meta.verbose_name_plural
            

    return {
        'page': page,
        'pagination_required': pagination_required,
        'object_name': object_name,
        'qs': qs,
    }
pagination = register.inclusion_tag('pagination.html')(pagination)
