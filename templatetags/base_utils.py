from django.template import Library, Node, NodeList, resolve_variable
from django.template import TemplateSyntaxError, VariableDoesNotExist
import datetime

#sample taken form ubernostrums blog

register = Library()

class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest\
              tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])
get_latest = register.tag(get_latest)

class CompareNode(Node):
    def __init__(self, var1, var2, nodelist_true, nodelist_false, lessthan, orequal):
        self.var1, self.var2 = var1, var2
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.lessthan = lessthan
        self.orequal = orequal

    def render(self, context):
        try:
            val1 = resolve_variable(self.var1, context)
        except VariableDoesNotExist:
            val1 = None
        try:
            val2 = resolve_variable(self.var2, context)
        except VariableDoesNotExist:
            val2 = None
        try:
            if self.lessthan:
                if self.orequal:
                    if val1 <= val2:
                        return self.nodelist_true.render(context)
                else:
                    if val1 < val2:
                        return self.nodelist_true.render(context)
            else:
                if self.orequal:
                    if val1 >= val2:
                        return self.nodelist_true.render(context)
                else:
                    if val1 > val2:
                        return self.nodelist_true.render(context)
        except:
            pass
        return self.nodelist_false.render(context)

def do_compare(parser, token, lessthan, orequal):
    """
    Output the contents of the block if depending on how two objects compare to each other.

    Examples::

        {% iflessthan alpha bravo %}
            ...
        {% endiflessthan %}

        {% ifgreaterthan alpha bravo %}
            ...
        {% else %}
            ...
        {% endifnotequal %}

        {% iflessthanorequal alpha bravo %}
            ...
        {% endiflessthanorequal %}

        {% ifgreaterthanorequal alpha bravo %}
            ...
        {% endifgreaterthanorequal %}
    """
    bits = list(token.split_contents())
    if len(bits) != 3:
        raise TemplateSyntaxError, "%r takes two arguments" % bits[0]
    end_tag = 'end' + bits[0]
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    return CompareNode(bits[1], bits[2], nodelist_true, nodelist_false, lessthan, orequal)

@register.tag
def iflessthan(parser, token):
    return do_compare(parser, token, True, False)

@register.tag
def ifgreaterthan(parser, token):
    return do_compare(parser, token, False, False)

@register.tag
def iflessthanorequal(parser, token):
    return do_compare(parser, token, True, True)

@register.tag
def ifgreaterthanorequal(parser, token):
    return do_compare(parser, token, False, True)





