# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0007_auto_20151015_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumodepacote',
            options={'verbose_name': 'Registro de Consumo de Pacote', 'verbose_name_plural': 'Registros de Consumo de Pacotes'},
        ),
        migrations.AlterModelOptions(
            name='pacote',
            options={'verbose_name': 'Registro de Compra Pacote', 'verbose_name_plural': 'Registros de Compra de Pacotes'},
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Cadastro de Clientes'},
        ),
        migrations.AlterModelOptions(
            name='tipodepacote',
            options={'verbose_name': 'Tipo de Pacote', 'verbose_name_plural': 'Cadastro de Tipos de Pacotes'},
        ),
    ]
