"""DetectoresMetales URL Configuration

The 'urlpatterns' list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""



"""
Enlazan las urls con las vistas o incluyen otros archivos urls. 

from django.conf.urls import patterns, url (hecho)

urlpatterns = patterns('',
    url(r'^a_REGULAR$', 'NOMBRE_APP.views.NOMBRE_FUNCION', name='NOMBRE_VISTA'),
    url(r'^a_REGULAR/', include('NOMBRE_APP.urls')),
)

El primer caso es el normal dentro de las aplicaciones y el segundo es 
el normal en el urls del proyecto.

El nombre de la vista es el que usaremos en las plantillas. Por 
ejemplo si nuestra aplicacion es de noticias, y hablamos de la vista 
de edicion, el nombre de la funcion podria ser edit y el nombre de la 
vista edit_news.

Para saber si nuestra a regular es correcta podemos usar pythex. 
Una web que nos facilita dicha labor, sobretodo si tenemos un poco 
oxidadas estas.

"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('DetectoresMetales.BBDD.urls')),
]
