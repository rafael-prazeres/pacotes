# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0004_auto_20151013_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumodepacote',
            name='pacote_consumido',
            field=models.ForeignKey(to='pacotes.Pacote', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='pacote',
            name='tipo_de_pacote',
            field=models.ForeignKey(to='pacotes.TipoDePacote', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='remadorautorizado',
            name='pacote',
            field=models.ForeignKey(to='pacotes.Pacote', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AlterField(
            model_name='remadorautorizado',
            name='pessoa',
            field=models.ForeignKey(to='pacotes.Pessoa', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
