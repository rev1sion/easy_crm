# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-24 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_auto_20180524_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycontact',
            name='company_object_contact',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='firstapp.CompanyObject'),
        ),
    ]