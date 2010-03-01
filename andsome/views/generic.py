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

                                                                                        
