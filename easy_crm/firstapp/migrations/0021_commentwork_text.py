# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-18 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0020_commentwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentwork',
            name='text',
            field=models.TextField(default='1', max_length=100, verbose_name='Комментарий'),
            preserve_default=False,
        ),
    ]
