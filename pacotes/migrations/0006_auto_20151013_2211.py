# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0005_auto_20151013_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumodepacote',
            name='tempo_de_duracao_da_remada',
            field=models.PositiveSmallIntegerField(verbose_name=b'Dura\xc3\xa7\xc3\xa3o da remada (em minutos)', choices=[(15, b'00:15'), (30, b'00:30'), (45, b'00:45'), (60, b'01:00'), (75, b'01:15'), (90, b'01:30'), (105, b'01:45'), (120, b'02:00')]),
        ),
    ]
