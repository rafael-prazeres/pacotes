# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0011_auto_20151017_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='tipo_sanguineo',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'A+', b'Tipo A Rh+'), (b'B+', b'Tipo B Rh+'), (b'AB+', b'Tipo AB Rh+'), (b'O+', b'Tipo O Rh+'), (b'A-', b'Tipo A Rh-'), (b'B-', b'Tipo B Rh-'), (b'AB-', b'Tipo AB Rh-'), (b'O-', b'Tipo O Rh-')]),
        ),
    ]
