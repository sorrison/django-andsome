from django.newforms import *
#from django.newforms.widgets import RadioInput
from django.newforms.util import smart_unicode
from django.utils.html import escape, conditional_escape
from django.utils.simplejson import *
from django.utils.safestring import mark_safe   
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.safestring import mark_safe
from django.newforms.util import flatatt

class TinyMCE(Textarea):
    """
    TinyMCE widget. requires you include tiny_mce_src.js in your template
    you can customize the mce_settings by overwriting instance mce_settings,
    or add extra options using update_settings
    """ 
    
    mce_settings = dict(
        mode = "exact",
        theme = "simple",
        theme_advanced_toolbar_location = "top",
        theme_advanced_toolbar_align = "center",
    )    
             
    def update_settings(self, custom):
        return_dict = self.mce_settings.copy()
        return_dict.update(custom)
        return return_dict
    
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs, name=name)
                   
        self.mce_settings['elements'] = "id_%s" % name
        mce_json = JSONEncoder().encode(self.mce_settings)
        
        return mark_safe(u'<textarea%s>%s</textarea> <script type="text/javascript">\
                tinyMCE.init(%s)</script>' % (flatatt(final_attrs), escape(value), mce_json))



class RadioInput(StrAndUnicode):
    """
    An object used by RadioFieldRenderer that represents a single
    <input type='radio'>.
    """

    def __init__(self, name, value, attrs, choice, index):
        self.name, self.value = name, value
        self.attrs = attrs
        self.choice_value = force_unicode(choice[0])
        self.choice_label = force_unicode(choice[1])
        self.index = index

    def __unicode__(self):
        return mark_safe(u'%s<label for=%s>%s</label>' % (self.tag(), self.attrs['id'],
                conditional_escape(force_unicode(self.choice_label))))

    def is_checked(self):
        return self.value == self.choice_value

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = '%s_%s' % (self.attrs['id'], self.index)
        final_attrs = dict(self.attrs, type='radio', name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return mark_safe(u'<input%s />' % flatatt(final_attrs))



class InlineRadioFieldRenderer(StrAndUnicode):
    """
    An object used by RadioSelect to enable customization of radio widgets.
    """

    def __init__(self, name, value, attrs, choices):
        self.name, self.value, self.attrs = name, value, attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield RadioInput(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return RadioInput(self.name, self.value, self.attrs.copy(), choice, idx)

    def __unicode__(self):
        return self.render()

    def render(self):
        """Outputs a <ul> for this set of radio fields."""
        return mark_safe(u'<ul class="radiolist inline">\n%s\n</ul>' % u'\n'.join([u'<li>%s</li>'
                % force_unicode(w) for w in self]))
