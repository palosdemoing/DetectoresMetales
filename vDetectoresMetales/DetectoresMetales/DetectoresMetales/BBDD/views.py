from datetime import datetime

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


from DetectoresMetales.BBDD.forms import ExpedientesForm
from DetectoresMetales.BBDD.models import Expedientes

#from DetectoresMetales import settings    MAL
#from django.conf import settings          BIEN   pilla el mio igual



def expedientes_list(request):
    expedientes_filtered = Expedientes.objects.filter(
        fecha_solicitud__lte=datetime.now()).order_by('fecha_solicitud')
    paginator = Paginator(expedientes_filtered, 3) #settings.PAGINATION_PAGES) # variable en settings.py
    page_default = 1

    page = request.GET.get('page', page_default)
        # por defecto daría 1, porque .get() solo devuelve 1 objeto, el segundo es default
        # así ya no entraría al -> except EmptyPage
        # resulta más limpio que dejarlo pasar por las excepciones
    try:
        expedientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        expedientes = paginator.page(page_default)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        expedientes = paginator.page(paginator.num_pages)

    return render_to_response('expedientes/expedientes_list.html', {"expedientes": expedientes})
                              



def expedientes_add(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    initial = {'fecha_solicitud': datetime.now()}
        # establece valor inicial a este campo
    expedientes_form = ExpedientesForm(data=data,
                         initial=initial)
    if expedientes_form.is_valid():
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_add.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


def expedientes_edit(request, expedienteitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    expediente_item = Expedientes.objects.get(pk=expedienteitem_pk)
    expedientes_form = ExpedientesForm(data=data,
                         instance=expediente_item)
    if expedientes_form.is_valid():
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_edit.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))

