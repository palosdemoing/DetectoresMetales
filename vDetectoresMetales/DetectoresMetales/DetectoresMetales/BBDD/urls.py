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
    url(r'^BBDD/expedientes_add/$', 'expedientes_add', name='expedientes_add'),
    url(r'^BBDD/expedientes_edit/(?P<expedienteitem_pk>\d+)/$', 'expedientes_edit', name='expedientes_edit'),
            # parametro para que servidor la identifique
    url(r'^BBDD/expedientes_delete/(?P<expedienteitem_pk>\d+)/$', 'expedientes_delete', name='expedientes_delete')
            
                # en pythex ->    ^BBDD/edit/(?P<newsitem_pk>\d+)/$
                # esta match con     BBDD/edit/3/
                
    # si cambio aqui las URL no interfiere con las llamadas desde templatetags, 
    # que van directamente a las funciones de las views.py
    
    
    #~ ha cambiado la estructura de URL, no se si a mi me interesa
    #~   porque en el curso solo hemos CRUD las news pero yo en BBDD tendre mas elementos
    #~ url(r'^$', 'news_list', name='news_list'),
    #~ url(r'^news/add/$', 'news_add', name='news_add'),
    #~ url(r'^news/edit/(?P<newsitem_pk>\d+)/$', 'news_edit', name='news_edit'),
    #~ url(r'^news/delete/(?P<newsitem_pk>\d+)/$', 'news_delete', name='news_delete')
    
    
)
