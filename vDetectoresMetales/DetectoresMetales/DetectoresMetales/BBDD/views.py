from datetime import datetime

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


from DetectoresMetales.BBDD.forms import ExpedientesForm
from DetectoresMetales.BBDD.models import Expedientes

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from DetectoresMetales import settings



def expedientes_list(request):
    expedientes_filtered = Expedientes.objects.filter(
        fecha_solicitud__lte=datetime.now()).order_by('fecha_solicitud')
    paginator = Paginator(expedientes_filtered, 3) #settings.PAGINATION_PAGES) # variable en settings.py

    page = request.GET.get('page')
    try:
        expedientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        expedientes = paginator.page(1)
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
    return render_to_response('expedientes/expedientes_list.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


def expedientes_edit(request, expedienteitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    expedientes_item = Expedientes.objects.get(pk=expedienteitem_pk)
    expedientes_form = ExpedientesForm(data=data,
                         instance=expedientes_item)
    if expedientes_form.is_valid():
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_edit.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))

