
def get_object_or_new(model, **kwargs):

   # try:
        obj = model._default_manager.get(**kwargs)
    #except:
     #   return model()
