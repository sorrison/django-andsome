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
Module for abstract graph generation base classes.
"""


class GraphGenerator(object):

    def sparkline(self):
        raise NotImplementedError

    def bar_chart(self, data, labels, x_labels, max_y):
        raise NotImplementedError

    def pie_chart(self, data_dict):
        raise NotImplementedError
