# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0008_auto_20151015_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pacote',
            old_name='data_de_compra',
            new_name='data_de_venda',
        ),
        migrations.AlterField(
            model_name='tipodepacote',
            name='prazo_de_validade',
            field=models.PositiveSmallIntegerField(verbose_name=b'Prazo de Validade (em meses)'),
        ),
    ]
