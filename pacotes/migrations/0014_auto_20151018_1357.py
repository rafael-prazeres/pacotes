# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0013_pacote_consumo_permitido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='consumo_permitido',
            field=models.BooleanField(),
        ),
    ]
