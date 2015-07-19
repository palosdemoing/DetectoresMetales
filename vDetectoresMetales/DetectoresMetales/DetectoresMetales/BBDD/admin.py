from django.contrib import admin

from DetectoresMetales.BBDD.models import Expedientes #, Event


class ExpedientesAdmin(admin.ModelAdmin):
    list_display = ('ID_expediente', 'expediente', 'fecha_solicitud')
    list_filter = ('fecha_solicitud',)
    search_fields = ('expediente',)

#~ 
#~ class EventAdmin(admin.ModelAdmin):
    #~ pass


admin.site.register(Expedientes, ExpedientesAdmin)
#~ admin.site.register(Event, EventAdmin)
