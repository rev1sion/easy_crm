# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-18 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import firstapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0022_documentwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentwork',
            name='document',
            field=models.FileField(upload_to='work/documents/%Y/%m/%d', validators=[firstapp.validators.validate_file_extension]),
        ),
    ]