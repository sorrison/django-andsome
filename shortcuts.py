
def get_object_or_new(model, **kwargs):

   # try:
        obj = model._default_manager.get(**kwargs)
    #except:
     #   return model()


def p(**kwargs):
        print kwargs
        print 'kkkkkkk'

def pp(**kwargs):
        p(**kwargs)
        print kwargs
        for i,v in kwargs.items():
                print i
                print v
