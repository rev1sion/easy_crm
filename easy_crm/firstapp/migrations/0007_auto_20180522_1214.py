# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-22 09:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20180522_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentcompany',
            old_name='user',
            new_name='owner',
        ),
    ]