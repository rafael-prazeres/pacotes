# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0002_consumodepacote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipodepacote',
            old_name='quantidade_de_horas',
            new_name='duracao_min',
        ),
        migrations.AlterField(
            model_name='consumodepacote',
            name='remador_autorizado',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'pacote', chained_field=b'pacote_consumido', auto_choose=True, to='pacotes.RemadorAutorizado'),
        ),
    ]
