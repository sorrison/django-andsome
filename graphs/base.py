
"""
Module for abstract graph generation base classes.
"""


class GraphGenerator(object):

    def sparkline(self):
        raise NotImplementedError

    def bar_chart(self, data, labels, x_labels, max_y):
        raise NotImplementedError

    def pie_chart(self, data_dict):
        raise NotImplementedError
