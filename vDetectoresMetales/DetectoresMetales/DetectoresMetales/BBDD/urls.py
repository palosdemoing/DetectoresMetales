'''

especifico de la utilidad BBDD

urlpatterns = patterns('',
    url(r'^a_REGULAR$', 'NOMBRE_APP.views.NOMBRE_FUNCION', name='NOMBRE_VISTA'),
    url(r'^a_REGULAR/', include('NOMBRE_APP.urls')),
)


'''

from django.conf.urls import patterns, url


urlpatterns = patterns('DetectoresMetales.BBDD.views',
    url(r'^$', 'expedientes_list', name='expedientes_list'),
    url(r'^BBDD/add/$', 'expedientes_add', name='expedientes_add'),
    url(r'^BBDD/edit/(?P<expedienteitem_pk>\d+)/$', 'expedientes_edit', name='expedientes_edit'),
)
