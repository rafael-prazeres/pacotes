# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0006_auto_20151013_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remadorautorizado',
            name='pacote',
            field=models.ForeignKey(to='pacotes.Pacote'),
        ),
    ]
