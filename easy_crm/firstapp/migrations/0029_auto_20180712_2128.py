# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-12 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0028_auto_20180712_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyobject',
            name='comment',
            field=models.CharField(max_length=300, verbose_name='Объект'),
        ),
    ]