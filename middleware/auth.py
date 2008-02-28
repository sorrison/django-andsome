from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.conf import settings

class SiteLogin:
    "This middleware requires a login for every view"
    def process_request(self, request):
        if request.path != settings.LOGIN_URL and request.user.is_anonymous():
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL,request.path))

