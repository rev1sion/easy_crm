# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-24 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_auto_20180523_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycontact',
            name='company_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Company'),
        ),
    ]
