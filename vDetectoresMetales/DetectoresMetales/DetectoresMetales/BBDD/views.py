import json

#from datetime import datetime

#from django.conf import settings
# si lo voy a implementar.... no tendre forma de controlar el uso desde el frontend si no
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
#from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import (HttpResponseRedirect,
                         HttpResponseBadRequest, HttpResponse)
from django.shortcuts import get_object_or_404, render_to_response
#from django.template import RequestContext

# esto para crear vistas como clases
#from django.views.generic import CreateView, ListView



from datetime import datetime

#from DetectoresMetales import settings    MAL
from django.conf import settings         # BIEN   pilla el mio igual
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from django.core.urlresolvers import reverse
#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
from django.template import RequestContext


from DetectoresMetales.BBDD.forms import ExpedientesForm, SolicitantesForm
from DetectoresMetales.BBDD.models import Expedientes, Solicitantes


"""
Vistas para tabla Expedientes
"""
def expedientes_list(request):
    # llama al manager 'solicitado'
    # evaluar como se utilizara este manager
    expedientes_filtered = Expedientes.objects.solicitado()
    paginator = Paginator(expedientes_filtered, settings.PAGINATION_PAGES) # variable en settings.py
    page_default = 1 # en detectores seria la ultima

    page = request.GET.get('page', page_default)
        # por defecto daria 1, porque .get() solo devuelve 1 objeto, el segundo es default
        # asi ya no entraria al -> except EmptyPage
        # resulta más limpio que dejarlo pasar por las excepciones
    try:
        expedientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        expedientes = paginator.page(page_default)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        expedientes = paginator.page(paginator.num_pages)

    return render_to_response('expedientes/expedientes_list.html', 
                                {"expedientes": expedientes},
                              context_instance=RequestContext(request))
                              


#decorador que controla si usuario logeado, en su defecto redirige a /admin/
@login_required(login_url='/admin/')
def expedientes_add(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    initial = {'fecha_solicitud': datetime.now()}
        # establece valor inicial a este campo
    expedientes_form = ExpedientesForm(data=data,
                         initial=initial)
    if expedientes_form.is_valid():
        #basicos en funcion al tipo de datos
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_add.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def expedientes_edit(request, expedienteitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    #expediente_item = Expedientes.objects.get(pk=expedienteitem_pk)
    expedientes_item = get_object_or_404(Expedientes, pk=expedienteitem_pk)
    expedientes_form = ExpedientesForm(data=data,
                         instance=expediente_item)
    if expedientes_form.is_valid():
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_edit.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def expedientes_delete(request, expedienteitem_pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    expedientes_item = get_object_or_404(Expedientes, pk=expedienteitem_pk)
    expedientes_item.delete()
    if request.is_ajax():
        # necesario para informar del exito de la solicitud
        # no me acuerdo muy bien revisar video
        return HttpResponse(json.dumps({'status': 'ok'}))
    return HttpResponseRedirect(reverse('expedientes_list'))



"""
Vistas para tabla Solicitantes
def solicitantes_list(request):
    # llama al manager 'solicitado'
    # evaluar como se utilizara este manager
    solicitantes_filtered = Solicitantes.objects.solicitado()
    paginator = Paginator(expedientes_filtered, settings.PAGINATION_PAGES) # variable en settings.py
    page_default = 1 # en detectores seria la ultima

    page = request.GET.get('page', page_default)
        # por defecto daria 1, porque .get() solo devuelve 1 objeto, el segundo es default
        # asi ya no entraria al -> except EmptyPage
        # resulta más limpio que dejarlo pasar por las excepciones
    try:
        expedientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        expedientes = paginator.page(page_default)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        expedientes = paginator.page(paginator.num_pages)

    return render_to_response('expedientes/expedientes_list.html', 
                                {"expedientes": expedientes},
                              context_instance=RequestContext(request))
                              


#decorador que controla si usuario logeado, en su defecto redirige a /admin/
@login_required(login_url='/admin/')
def expedientes_add(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    initial = {'fecha_solicitud': datetime.now()}
        # establece valor inicial a este campo
    expedientes_form = ExpedientesForm(data=data,
                         initial=initial)
    if expedientes_form.is_valid():
        #basicos en funcion al tipo de datos
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_add.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def expedientes_edit(request, expedienteitem_pk):
    data = None
    if request.method == 'POST':
        data = request.POST
    #expediente_item = Expedientes.objects.get(pk=expedienteitem_pk)
    expedientes_item = get_object_or_404(Expedientes, pk=expedienteitem_pk)
    expedientes_form = ExpedientesForm(data=data,
                         instance=expediente_item)
    if expedientes_form.is_valid():
        expedientes_form.save()
        return HttpResponseRedirect(reverse('expedientes_list'))
    return render_to_response('expedientes/expedientes_edit.html',
                              {'expedientes_form': expedientes_form},
                              context_instance=RequestContext(request))


@login_required(login_url='/admin/')
def expedientes_delete(request, expedienteitem_pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    expedientes_item = get_object_or_404(Expedientes, pk=expedienteitem_pk)
    expedientes_item.delete()
    if request.is_ajax():
        # necesario para informar del exito de la solicitud
        # no me acuerdo muy bien revisar video
        return HttpResponse(json.dumps({'status': 'ok'}))
    return HttpResponseRedirect(reverse('expedientes_list'))



"""
