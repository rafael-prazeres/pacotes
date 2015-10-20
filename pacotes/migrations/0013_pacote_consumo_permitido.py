# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0012_auto_20151018_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='consumo_permitido',
            field=models.BooleanField(default=True),
        ),
    ]
