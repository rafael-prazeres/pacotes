# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0003_auto_20151012_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacote',
            name='responsavel_financeiro',
            field=models.ForeignKey(related_name='responsavel_financeiro_pacote', on_delete=django.db.models.deletion.PROTECT, to='pacotes.Pessoa'),
        ),
        migrations.AlterField(
            model_name='tipodepacote',
            name='duracao_min',
            field=models.PositiveSmallIntegerField(verbose_name=b'Dura\xc3\xa7\xc3\xa3o (em minutos)'),
        ),
    ]
