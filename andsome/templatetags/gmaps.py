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


