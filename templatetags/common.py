from django.template import Library
from django.conf import settings
import datetime

register = Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search('^/%s%s' % (settings.BASE_URL, pattern), request.path):
        return 'active'
    return ''



@register.simple_tag
def date_filter(start, end):
    
    today = datetime.date.today()

    last_7 = (today - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    last_90 = (today - datetime.timedelta(days=90)).strftime('%Y-%m-%d')
    last_365 = (today - datetime.timedelta(days=365)).strftime('%Y-%m-%d')


    view_7, view_90, view_365 = False, False, False

    if end == today:
        if start == today - datetime.timedelta(days=7):
            view_7 = True
        if start == today - datetime.timedelta(days=90):
            view_90 = True
        if start == today - datetime.timedelta(days=365):
            view_365 = True

    s = ''

    if view_7:
        s += 'Last 7 Days'
    else:
        s += """<a href="./?start=%s">Last 7 Days</a>""" % last_7
    s += " | "

    if view_90:
        s += "Last 90 Days"
    else:
        s += """<a href="./?start=%s">Last 90 Days</a>""" % last_90
    s += " | "
    if view_365:
        s += "Last 365 Days"
    else:
        s += """<a href="./?start=%s">Last 365 Days</a>""" % last_365


    return s


@register.simple_tag
def yes_no_img(boolean, reversed=False):
    
    if reversed == 'reversed': 
        if boolean:
            boolean = False
        else:
            boolean = True

    if boolean:
        return """<img src="%simg/admin/icon-yes.gif" alt="Active" />""" % settings.MEDIA_URL
    else:
        return """<img src="%simg/admin/icon-no.gif" alt="Not Active"/>""" % settings.MEDIA_URL

#yes_no_img.mark_safe = True
