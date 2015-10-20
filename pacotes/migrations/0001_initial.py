# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_de_compra', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=14)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('data_nascimento', models.DateField(null=True, blank=True)),
                ('tipo_sanguineo', models.CharField(max_length=3, choices=[(b'A+', b'Tipo A Rh+'), (b'B+', b'Tipo B Rh+'), (b'AB+', b'Tipo AB Rh+'), (b'O+', b'Tipo O Rh+'), (b'A-', b'Tipo A Rh-'), (b'B-', b'Tipo B Rh-'), (b'AB-', b'Tipo AB Rh-'), (b'O-', b'Tipo O Rh-')])),
                ('sexo', models.CharField(max_length=1, choices=[(b'F', b'Feminino'), (b'M', b'Masculino')])),
            ],
        ),
        migrations.CreateModel(
            name='RemadorAutorizado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_de_autorizacao', models.DateField(auto_now_add=True)),
                ('pacote', models.ForeignKey(to='pacotes.Pacote')),
                ('pessoa', models.ForeignKey(to='pacotes.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDePacote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('quantidade_de_horas', models.PositiveSmallIntegerField()),
                ('prazo_de_validade', models.PositiveSmallIntegerField()),
                ('venda_autorizada', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='pacote',
            name='remadores_autorizados',
            field=models.ManyToManyField(to='pacotes.Pessoa', through='pacotes.RemadorAutorizado'),
        ),
        migrations.AddField(
            model_name='pacote',
            name='responsavel_financeiro',
            field=models.ForeignKey(related_name='responsavel_financeiro_pacote', to='pacotes.Pessoa'),
        ),
        migrations.AddField(
            model_name='pacote',
            name='tipo_de_pacote',
            field=models.ForeignKey(to='pacotes.TipoDePacote'),
        ),
        migrations.AlterUniqueTogether(
            name='remadorautorizado',
            unique_together=set([('pacote', 'pessoa')]),
        ),
    ]
