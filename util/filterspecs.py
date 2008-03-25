from django.utils.safestring import mark_safe


def get_query_string(qs):
    return '?' + '&amp;'.join([u'%s=%s' % (k, v) for k, v in qs.items()]).replace(' ', '%20')
    

class Filter(object):

    def __init__(self, request, name, filters):
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
        if self.selected is not None:
            output += """<li><a href="%s">All</a></li>\n""" % get_query_string(qs)
        else:
            output += """<li class="selected"><a href="%s">All</a></li>\n""" % get_query_string(qs)
        for k, v in self.filters.items():
            if str(self.selected) == str(k):
                style = """class="selected" """
            else:
                style = ""
            qs[self.name] = k
            output += """<li %s><a href="%s">%s</a></li>\n""" % (style, get_query_string(qs), v)
            
        output += '</ul>'
            
        return output


class FilterBar(object):

    def __init__(self, request, filter_list):

        self.request = request
        self.filter_list = filter_list
        qs = {}
        for f in self.filter_list:
            if self.request.GET.has_key(f.name):
                qs[f.name] = self.request.GET[f.name]

        self.qs = qs


    def output(self):

        output = ''

        for f in self.filter_list:
            output += f.output(self.qs.copy())

        return output

    def __str__(self):
        return mark_safe(self.output())
