# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='qtdInscricoes',
            field=models.IntegerField(null=True),
        ),
    ]
