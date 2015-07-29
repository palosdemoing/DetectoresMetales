# de momento a modo de plantilla/ejemplo


from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

#from django.utils import translation


class No404Middleware(object):

    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('expedientes_list'))
        return response
