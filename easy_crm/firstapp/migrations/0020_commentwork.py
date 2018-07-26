# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-17 21:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0019_auto_20180617_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('moder', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.CompanyObjectWork')),
            ],
            options={
                'verbose_name': 'Комментарий работе',
                'verbose_name_plural': 'Комментарии объектов',
            },
        ),
    ]
