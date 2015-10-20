# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumoDePacote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_e_hora_da_remada', models.DateTimeField()),
                ('tempo_de_duracao_da_remada', models.PositiveSmallIntegerField(choices=[(15, b'00:15'), (30, b'00:30'), (45, b'00:45'), (60, b'01:00'), (75, b'01:15'), (90, b'01:30'), (105, b'01:45'), (120, b'02:00')])),
                ('numero_de_pranchas_utilizadas', models.PositiveSmallIntegerField(choices=[(1, b'Uma Prancha'), (2, b'Duas Pranchas'), (3, b'Tres Pranchas'), (4, b'Quatro Pranchas'), (5, b'Cinco pranchas'), (6, b'Seis Pranchas'), (7, b'Sete Pranchas'), (8, b'Oito Pranhcas')])),
                ('nota_sobre_consumo', models.TextField(null=True, blank=True)),
                ('pacote_consumido', models.ForeignKey(to='pacotes.Pacote')),
                ('remador_autorizado', models.ForeignKey(to='pacotes.RemadorAutorizado')),
            ],
        ),
    ]
