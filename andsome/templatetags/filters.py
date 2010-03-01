from django.template import Library
from django.contrib.humanize.templatetags.humanize import intcomma
from django.template.defaultfilters import filesizeformat

register = Library()

@register.filter
def timeformat(value):
    
    if value == '':
        return ''

    if value is None:
        return '0s'
    if value < 60:
        return '%ss' % intcomma(int(value))
    # less than 1 hour
    elif value < 3600:
        v = int(value/60)
        return '%sm' % intcomma(v)
    # less than 1 day
    #elif value < 86400:
    #    v = int(value/3600)
    #    return '%sh' % intcomma(v)
    # less than a month
    #elif value < 2592000:
    #    v = int(value/86400)
    #    return '%sd' % intcomma(v)
    # less than 1 year
    #elif value < 31104000:
    #    v = int(value/2592000)
    #    return '%smonth' % intcomma(v)
    else:
        v = int(value/3600)
        return '%sh' % intcomma(v)

@register.filter
def fileformat(kilobytes):

    return filesizeformat(kilobytes*1024)


