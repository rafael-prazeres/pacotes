# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0010_auto_20151016_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacote',
            options={'ordering': ['responsavel_financeiro__nome'], 'verbose_name': 'Registro de Venda de Pacote', 'verbose_name_plural': 'Registros de Venda de Pacotes'},
        ),
        migrations.AddField(
            model_name='pacote',
            name='observacoes',
            field=models.TextField(null=True, verbose_name=b'Observa\xc3\xa7\xc3\xb5es', blank=True),
        ),
    ]
