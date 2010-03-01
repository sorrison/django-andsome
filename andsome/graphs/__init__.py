from django.conf import settings
import datetime

module = __import__(settings.GRAPH_LIB, {}, {}, [''])

grapher = module.GraphGenerator()


def gen_sparkline():
    return grapher.sparkline()

def bar_chart(data, labels, x_labels, max_y):
    return grapher.bar_chart(data, labels, x_labels, max_y)

def pie_chart(data_dict):
    return grapher.pie_chart(data_dict)
