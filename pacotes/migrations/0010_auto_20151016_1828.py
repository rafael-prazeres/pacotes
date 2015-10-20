# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0009_auto_20151016_1719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacote',
            options={'verbose_name': 'Registro de Venda de Pacote', 'verbose_name_plural': 'Registros de Venda de Pacotes'},
        ),
    ]
