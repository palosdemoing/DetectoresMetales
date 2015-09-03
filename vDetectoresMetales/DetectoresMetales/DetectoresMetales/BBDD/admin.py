from django.contrib import admin

from DetectoresMetales.BBDD.models import Expedientes #, Event


class ExpedientesAdmin(admin.ModelAdmin):
    list_display = ('ID_expediente', 'expediente', 'fecha_solicitud')
    list_filter = ('fecha_solicitud',)
    search_fields = ('expediente',)


class SolicitantesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Expedientes, ExpedientesAdmin)
admin.site.register(Solicitantes, SolicitantesAdmin)



"""
   
------------------------------------------------------------------------
Sobreescritura de las plantillas
------------------------------------------------------------------------

Muchas veces nos gustaría modificar un poco alguna de las plantillas 
de un determinado modelo de la administración, para añadir algun texto, 
alguna css, algun js, etc etc. Pués Django nos lo pone muy sencillo en 
este aspecto, lo unico que tendríamos que hacer es añadir una plantilla 
(o en una aplicación o en el directorio de plantillas de nuestro 
proyecto) con la siguiente estructura: 

    templates/app_name/model_name/plantilla_a_sobreescribir.html. 

Es decir por ejemplo si quisieramos personalizar la plantilla de 
edición de un grupo tendríamos que crear una plantilla llamada 
change_form.html en el directorio templates/auth/group/.




"""
