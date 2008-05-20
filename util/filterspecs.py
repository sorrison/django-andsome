from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet
import datetime
from operator import itemgetter

def get_query_string(qs):
    return '?' + '&amp;'.join([u'%s=%s' % (k, v) for k, v in qs.items()]).replace(' ', '%20')

class Filter(object):
    multi = False

    def __init__(self, request, name, filters):

        if isinstance(filters, QuerySet):
            f = {}
            for i in filters:
                f[i.pk] = str(i)
            filters = f
        
        self.name = name
        self.filters = filters
        self.selected = None
        if request.GET.has_key(name):
            self.selected = request.GET[name]


    def output(self, qs):

        try:
            del(qs[self.name])
        except:
            pass

        output = ''
        output += '<h3>By %s</h3>\n' % self.name
        output += '<ul>\n'
                    
        filters = sorted(self.filters.iteritems(), key=itemgetter(1))

        if self.selected is not None:
            output += """<li><a href="%s">All</a></li>\n""" % get_query_string(qs)
        else:
            output += """<li class="selected"><a href="%s">All</a></li>\n""" % get_query_string(qs)
        for k, v in filters:
            if str(self.selected) == str(k):
                style = """class="selected" """
            else:
                style = ""
            qs[self.name] = k
            output += """<li %s><a href="%s">%s</a></li>\n""" % (style, get_query_string(qs), v)
            
        output += '</ul>'
            
        return output




class DateFilter(object):
    multi = True

    def __init__(self, request, name, header=''):
        self.name = name
        if header == '':
            self.header = name
        else:
            self.header = header
        params = dict(request.GET.items())
        
        self.field_generic = '%s__' % self.name

        self.date_params = dict([(k, v) for k, v in params.items() if k.startswith(self.field_generic)])

        today = datetime.date.today()
        one_week_ago = today - datetime.timedelta(days=7)
        today_str = today.strftime('%Y-%m-%d')

        self.links = (
            ('Any date', {}),
            ('Today', {'%s__year' % self.name: str(today.year),
                       '%s__month' % self.name: str(today.month),
                       '%s__day' % self.name: str(today.day)}),
            ('Past 7 days', {'%s__gte' % self.name: one_week_ago.strftime('%Y-%m-%d'),
                             '%s__lte' % self.name: today_str}),
            ('This month', {'%s__year' % self.name: str(today.year),
                             '%s__month' % self.name: str(today.month)}),
            ('This year', {'%s__year' % self.name: str(today.year)})
        )

    def choices(self):
        for title, param_dict in self.links:
            yield {'selected': self.date_params == param_dict,
                   'query_dict': param_dict,
                   'display': title}


    def output(self, qs):
        choices = self.choices()

        output = ''
        output += '<h3>By %s</h3>\n' % self.header
        output += '<ul>\n'
                    

        for choice in choices:
            for k,v in qs.items():
                if k.startswith(self.field_generic):
                    del(qs[k])
        
            for k,v in choice['query_dict'].items():
                qs[k] = v
            
            output += """<li %s><a href="%s">%s</a></li>\n""" % (choice['selected'] and "class='selected'" or '', get_query_string(qs), choice['display'])
            
        output += '</ul>'
        return output


class FilterBar(object):

    def __init__(self, request, filter_list):

        self.request = request
        self.filter_list = filter_list
        qs = {}
        for f in self.filter_list:
            if f.multi:
                params = dict(request.GET.items())
                field_generic = '%s__' % f.name
                m_params = dict([(k, v) for k, v in params.items() if k.startswith(field_generic)])
                for k,v in m_params.items():
                    qs[k] = v
                
            else:
                if self.request.GET.has_key(f.name):
                    qs[f.name] = self.request.GET[f.name]


        #if self.request.GET.has_key('p'):
        #    qs['p'] = self.request.GET['p']
        self.qs = qs


    def output(self):

        output = ''

        for f in self.filter_list:
            output += f.output(self.qs.copy())

        return output

    def __str__(self):
        return mark_safe(self.output())




class ObjectList(object):


    def __init__(self, request, object_list, headers, filters):

        self.headers = headers
        self.object_list = object_list
        
        
        
        
        
