# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BBDD', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expedientes',
            options={'ordering': ['ID_expediente'], 'verbose_name': 'Expediente', 'verbose_name_plural': 'Expedientes'},
        ),
        migrations.RenameField(
            model_name='expedientes',
            old_name='ID_Expediente',
            new_name='ID_expediente',
        ),
        migrations.AlterField(
            model_name='expedientes',
            name='expediente',
            field=models.TextField(max_length=50, null=True, verbose_name='Expediente', blank=True),
        ),
    ]
