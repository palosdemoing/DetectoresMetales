# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expedientes',
            fields=[
                ('ID_Expediente', models.AutoField(verbose_name=b'ID_Expediente', serialize=False, auto_created=True, primary_key=True)),
                ('expediente', models.TextField(null=True, verbose_name='Expediente', blank=True)),
                ('fecha_solicitud', models.DateTimeField(verbose_name='Fecha de Solicitud')),
            ],
            options={
                'verbose_name': 'Expediente',
                'verbose_name_plural': 'Expedientes',
            },
        ),
    ]
