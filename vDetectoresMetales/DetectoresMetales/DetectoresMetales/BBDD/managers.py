
# librerias de aplicacion django

"""
Con los managers conseguimos no tener que repetir una serie de consultas 
típicas de cada modelo

    # managers.py

        from django.db import models
        from django.db.models.query import QuerySet


        class MyModelQuerySet(QuerySet):

            def my_query(self):
                return self.filter(attr1=value1, attr2=value2)


        class MyModelManager(models.Manager):

            def get_query_set(self):
                return MyModelQuerySet(self.model, using=self._db)

            def my_query(self):
                return self.get_query_set().my_query()


    ....

    # models.py

        class MyModel(models.Model):

        ...
        objects = MyModelManager()



De esta manera podremos hacer cosas como esta:

    MyModel.objects.my_query()
    MyModel.objects.my_query().filter(...).exclude(...)
    MyModel.objects.filter(...).exclude(...).my_query()


Utiliza todo el flujo de llamadas internas de Django
"""


from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet



class BaseExpedientesQuerySet(QuerySet):

    def solicitado(self):
        # esto puede que no funcione, y si funciona tampoco es muy reusable
        # deberia recibir la variable por la que filtrar/ordenar....
        #     se llamaria todo esto.... BaseBBDDQuerySet  BaseBBDDManager
        return self.filter(fecha_solicitud__lte=datetime.now()).order_by('fecha_solicitud')


class BaseExpedientesManager(models.Manager):

    def get_queryset(self):
        return BaseExpedientesQuerySet(self.model, using=self._db)

    def solicitado(self):
        return self.get_queryset().solicitado()




# porque de usar estas dos funciones y no solo una directamente
"""
En caso de no seguir el esquema propuesto, y no utilizar 
        MyModelQuerySet, es decir hacer algo como esto:

    # managers.py

        from django.db import models

        class MyModelManager(models.Manager):

            def my_query(self):
                return self.filter(attr1=value1, attr2=value2)

    ....

    # models.py

    class MyModel(models.Model):

        ...
        objects = MyModelManager()


No podríamos hacer la ultima consulta, es decir:

    MyModel.objects.my_query() # Se puede hacer
    MyModel.objects.my_query().filter(...).exclude(...) # Se puede hacer
    MyModel.objects.filter(...).exclude(...).my_query() # No se puede hacer

Por eso siempre vamos a intentar seguir el primer esquema,

"""
