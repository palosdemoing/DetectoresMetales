from django.core.management.base import BaseCommand

from DetectoresMetales.BBDD.models import Expedientes


class Command(BaseCommand):
    help = 'Cuenta registros en tabla expedientes.'

    def handle(self, *args, **options):
        print(Expedientes.objects.count())



"""
Por ejemplo para llamarlo con 
    
    python manage.py count_expedientes
    

Ejecuta 

    python manage.py  # para ver lista y módulo donde están los comandos

Coge como plantilla django/contrib/auth/management/command/createsuperuser
"""
