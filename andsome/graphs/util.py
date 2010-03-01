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
from django.db import connection

import datetime

from decimal import Decimal


def smooth_data(rows, start, end):
    
    today = datetime.date.today()
    data = []
    colours = []
    period = (end - start).days
    
    if period >= 3000:
        while start <= end:
            start_e = start
            if start != today:
                total = 0
                
                end_e = start_e + datetime.timedelta(days=15)
                while start_e <= end_e:
                    try:
                        add = rows[start_e]
                    except:
                        add = 0
                    total = total + (add or 0)
                    start_e= start_e  + datetime.timedelta(days=1)

                total = total / 3600  
                data.append(total)
                colours.append(0x9AB8D7)
            start = start + datetime.timedelta(days=15)
    elif period >= 3000:
        while start <= end:
            start_e = start
            if start != today:
                total = 0
                
                end_e = start_e + datetime.timedelta(days=5)
                while start_e <= end_e:
                    try:
                        add = rows[start_e]
                    except:
                        add = 0
                    total = total + add
                    start_e= start_e  + datetime.timedelta(days=1)

                total = total / 3600
                total = float(total)
                data.append(total)
                colours.append(0x9AB8D7)
            start = start + datetime.timedelta(days=5)
    else:
        while start <= end:
            if start != today:
                try:
                    total = int(rows[start])
                except:
                    total = 0
                total = total# / 3600  
                data.append(total)
                colours.append(0x9AB8D7)
            start = start + datetime.timedelta(days=1)

    
    return data, colours

