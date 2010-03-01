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


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect

def add_edit_object(request, Model, Form, object_id=None, template_name=None):
    if object_id:
        obj = get_object_or_404(Model, pk=object_id)
    else:
        obj = None

    if not template_name:
        app_label = Model._meta.app_label
        model_name = Model._meta.verbose_name
        template_name = '%s/%s_form.html' % (app_label, model_name.lower().replace(' ', ''))
                                          
    if request.method == 'POST':
        form = Form(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(obj.get_absolute_url())
    else:
        form = Form(instance=obj)
        
    return render_to_response(template_name, { 'form': form, 'object': obj }, context_instance=RequestContext(request))

                                                                                        
