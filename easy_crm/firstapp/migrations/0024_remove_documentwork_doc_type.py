# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-25 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0023_auto_20180619_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentwork',
            name='doc_type',
        ),
    ]
