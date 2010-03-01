from django.template import Library
from django.conf import settings
from django import template
from django.template import resolve_variable

register = Library()


@register.inclusion_tag('inlineformfield.html')
def inlineformfield(field1, field2, field3=False):
    return locals()

@register.inclusion_tag('checkbox_formfield.html')
def checkbox_formfield(field):
    return {'field': field, }

@register.inclusion_tag('form_as_div.html')
def form_as_div(form):
    return {'form': form, }

@register.inclusion_tag('search_form.html')
def search_form(url='', terms=''):
    return { 'url': url, 'terms': terms, 'MEDIA_URL': settings.MEDIA_URL }


@register.tag
def formfield(parser, token):
    try:
        tag_name, field = token.split_contents()
    except:
        raise template.TemplateSyntaxError, "%r tag requires exactly one argument" % token.contents.split()[0]
    return FormFieldNode(field)


class FormFieldNode(template.Node):
    def __init__(self, field):
        self.field = template.Variable(field)

    def get_template(self, class_name):
        try:
            template_name = 'formfield/%s.html' % class_name
            return template.loader.get_template(template_name)
        except template.TemplateDoesNotExist:
            return template.loader.get_template('formfield/default.html')

    def render(self, context):
        try:
            field = self.field.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        label_class_names = []
        if field.field.required:
            label_class_names.append('required')

        widget_class_name = field.field.widget.__class__.__name__.lower()
        field_class_name = field.field.__class__.__name__.lower()
        if widget_class_name == 'checkboxinput':
            label_class_names.append('vCheckboxLabel')
        

        class_str = label_class_names and u' class="%s"' % u' '.join(label_class_names) or u''

        context.push()
        context.push()
        context['class'] = class_str
        context['formfield'] = field
        output = self.get_template(field.field.widget.__class__.__name__.lower()).render(context)
        context.pop()
        context.pop()
        return output
        

        
        
            