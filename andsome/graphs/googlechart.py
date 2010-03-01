
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


    def bar_chart(self, data_dict, x_labels, max_y):

        chart = GroupedVerticalBarChart(840, 200)
        labels = []

        for label, data in data_dict.items():
            chart.add_data(data)
            labels.append(label)
            
        bar_width = 35 / len(data)
        chart.set_bar_width(bar_width)   
        
        chart.set_legend(labels)
        
        chart.set_axis_range('y', 0, float(max_y))
        chart.set_axis_labels('x', [''])
        chart.set_axis_labels('x', x_labels)
        
        chart.set_colours(colours[:len(data)])
        return chart.get_url()


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
