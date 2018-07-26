# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-04 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0015_remove_companycontact_company_object_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Контактные лица объекта',
                'verbose_name_plural': 'Контактные лица объекта',
            },
        ),
        migrations.AlterModelOptions(
            name='companycontact',
            options={'verbose_name': 'Контактные лица', 'verbose_name_plural': 'Контактные лица'},
        ),
        migrations.AddField(
            model_name='objectcontact',
            name='object_contact',
            field=models.ManyToManyField(to='firstapp.CompanyContact'),
        ),
    ]
