# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-05-04 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_document_showsequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='ShowSequence',
            field=models.BooleanField(default=False),
        ),
    ]
