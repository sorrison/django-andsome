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


from django.conf import settings
import datetime

module = __import__(settings.GRAPH_LIB, {}, {}, [''])

grapher = module.GraphGenerator()


def gen_sparkline():
    return grapher.sparkline()

def line_chart(*args, **kwargs):
    return grapher.line_chart(*args, **kwargs)

def bar_chart(data, labels, x_labels, max_y):
    return grapher.bar_chart(data, labels, x_labels, max_y)

def pie_chart(data_dict):
    return grapher.pie_chart(data_dict)
