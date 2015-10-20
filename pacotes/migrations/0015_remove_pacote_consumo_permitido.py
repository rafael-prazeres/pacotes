# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0014_auto_20151018_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacote',
            name='consumo_permitido',
        ),
    ]
