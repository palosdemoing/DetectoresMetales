# de momento a modo de plantilla/ejemplo

"""
"""


from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

#from django.utils import translation


class No404Middleware(object):

    def process_response(self, request, response):
        if response.status_code == 404:
            return HttpResponseRedirect(reverse('expedientes_list'))
        return response

# en settings.py [MIDDLEWARE_CLASSES]  'DetectoresMetales.middleware.No404Middleware',



""" ejemplo del curso respecto a la internacionalizacion, mas gestion de cookies

class LocaleMiddleware(object):
    #This middleware checks if we have a language cookie. In that case we use
    #that language

    def process_request(self, request):
        cookie = settings.LANGUAGE_COOKIE_NAME
        forced_lang = request.GET.get(cookie, None)
        request.forced_lang = forced_lang
        if forced_lang:
            translation.activate(forced_lang)
            request.LANGUAGE_CODE = translation.get_language()
            if hasattr(request, 'session'):
                request.session[translation.LANGUAGE_SESSION_KEY] = forced_lang
"""



"""
------------------------------------------------------------------------
Middlewares
------------------------------------------------------------------------

Segun el flujo de las peticiones

HTTPRequests -> urls.py -> (middleware)

	cuando urls.py hace un match llama a todos los middleware, al método
	
		process_request()
		
		
		
	
Los Middlewares son clases que pueden tener 5 métodos y que serán 
llamados (en caso de que estén) antes de llamar a la vista y después de 
llamar a la vista.
 Un middleware es algo que envuelve a la vista, y 
que nos es muy util si queremos añadirle algun atributo al request, 
si queremos capturar alguna excepción por ejemplo para devolver algun 
código de error (errores http 4XX), hacer alguna tarea antes o después 
de una vista....

-Estructura- no es necesaria entera

    class MyMiddleware(object):

        def process_request(self, request):
            # Se llama antes de invocar a la vista

        def process_view(self, request, view, *args, **kwargs):
            # Se llama antes de invoca a la vista
            # tenemos acceso a la vista (view)
            # y a los parámetros de la URL (args y kwargs)

        def process_exception(self, request, exception):
            # Se llama en caso de que se lanze una excepción

        def process_response(self, request, response):
            # Se llama tras invocar a la vista
            return response

        def process_template_response(self, request, response):
            # Se llama tras invocar a la vista,
            # si el response es un TemplateResponse
            # Esto no lo usaremos nosotros
			# por ejemplo cunado un HTTPResponse directamente, un JSON...
            return response


Los middleware que vamos a usar se definen en el settings, estos son 
los que Django añade por defecto:


    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
    )

"""
