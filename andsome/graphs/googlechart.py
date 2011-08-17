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



"""
Graph generation using pygooglechart
"""

from django.conf import settings
from django.db import connection
from django.template.defaultfilters import dictsortreversed

from operator import itemgetter
from decimal import Decimal
import datetime
from pygooglechart import *

import base
from util import *

__author__ = 'Sam Morrison'


colours = [
    '3374cd',
    '992220',
    '469b57',
    'e4e144',
    'cd3333',
    '749920',
    'ab346f',
    '6682bf',
    'dcab5e',
    '9a66bf',
    'b76683',
    '66aabf',
    '1f4590',
    'd8a303',
    '743920',
    '8ebf66',
    ]



class GraphGenerator(base.GraphGenerator):

    def sparkline(self, data, line_colour='4D89F9', fill_colour='E6F2FA'):
        chart = SparkLineChart(600, 100)
        chart.add_data(data)
        chart.set_line_style(0, thickness=3)
        chart.set_colours([line_colour])
        chart.add_fill_simple(fill_colour)
        return chart


    def line_chart(self, data_dict, title='', x_labels=None, y_label='', x_label=''):
        if not data_dict:
            return None
        
        chart = SimpleLineChart(840, 200)
        labels = []
        min_y = None
        max_y = None
        for label, data in data_dict.items():
            chart.add_data(data)
            labels.append(label)
            if min_y is None or min(data) < min_y:
                min_y = min(data)
            if max_y is None or max(data) > max_y:
                max_y = max(data)
            print data
                
        if len(labels) > 1:
            chart.set_legend(labels)

        chart.set_title(title)
        chart.set_axis_range('y', min_y, max_y)
        chart.set_axis_labels('y', ['',y_label,''])
        if x_labels:
            chart.set_axis_labels('x', x_labels)
        chart.set_axis_labels('x', ['', x_label, ''])
        #chart.set_grid(10, 20)
        for c, i in enumerate(data_dict):
            chart.set_line_style(c, thickness=2)
        
        chart.set_colours(colours[:len(data)])
        
        return chart


    def bar_chart(self, data_dict, x_labels, max_y=None, bar_width=None):

        chart = GroupedVerticalBarChart(840, 300)
        labels = []
        max_y = None
        for label, data in data_dict.items():
            chart.add_data(data)
            labels.append(label)
            if max_y is None or max(data) > max_y:
                max_y = max(data)

        if not bar_width:
            bar_width = 35 / len(data)
        chart.set_bar_width(bar_width)
        
        if len(labels) > 1:
            chart.set_legend(labels)
        
        chart.set_axis_range('y', 0, float(max_y))
        chart.set_axis_labels('x', [''])
        chart.set_axis_labels('x', x_labels)
        
        chart.set_colours(colours[:len(data)])
        return chart


    def pie_chart(self, data_dict, title=None):
        
        chart = PieChart2D(500, 225)
    
        chart_data = []
        chart_labels = []
        for label, value in data_dict.items():
            if value > 0:
                chart_labels.append(str(label))
                chart_data.append(value)

        if title:
            chart.title = title

        chart.add_data(chart_data)
        chart.set_pie_labels(chart_labels)
        chart.set_colours(colours[:len(data_dict)])
        return chart
