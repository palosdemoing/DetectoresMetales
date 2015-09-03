#from django.test import TestCase

# por si las moscas me aburro, ya adaptado a mis variables/funciones

# no probado

from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import six
from django.test import TestCase
from django.test.client import Client

from DetectoresMetales.BBDD.models import Expedientes


class ExpedientesTestCase(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def authentication(self):
        user, is_created = User.objects.get_or_create(username='admin')
        if is_created:
            user.is_superuser = True
            user.set_password('admin')
            user.save()
        self.client.login(username='admin', password='admin')

    def test_newslist(self):
        Expedientes.objects.create(expediente='Mi expediente test',
                            fecha_solicitud=datetime.now())
        response = self.client.get(reverse('expedientes_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mi expediente test', response.content)
        self.assertNotIn(b'ESTA CADENA NO SE ENCUENTRA EN EL RESPONSE',
                         response.content)


    def test_expedientes_add(self):
        self.authentication()
        response1 = self.client.get(reverse('expedientes_add'))
        self.assertEqual(response1.status_code, 200)
        self.assertIn(b'TEXTO DE AYUDA', response1.content)

        data = {'expediente': 'Mi expediente test 2',
                'fecha_solicitud': datetime.now()}
        response2 = self.client.post(reverse('expedientes_add'),
                                     data=data)
        self.assertEqual(response2.status_code, 302)

        response3 = self.client.get(reverse('expedientes_list'))
        self.assertIn(b'Mi expediente test 2', response3.content)

        response4 = self.client.post(reverse('expedientes_add'),
                                     data={})
        self.assertEqual(response4.status_code, 200)
        self.assertIn(b'Este campo es obligatorio.', response4.content)

    def test_print_expediente(self):
        expediente = Expedientes.objects.create(expediente='Mi expediente impresion test',
                                   fecha_solicitud=datetime.now())
        self.assertEqual(expediente.expediente, six.text_type(expediente))

