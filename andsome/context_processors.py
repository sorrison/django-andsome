from django.conf import settings

def base_url(request):
    ctx = {}
    ctx['base_url'] = settings.BASE_URL
    return ctx
