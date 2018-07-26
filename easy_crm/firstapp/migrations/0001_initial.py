# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 20:59
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_fio', models.CharField(max_length=100, verbose_name='Ф.И.О.')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('hobby', models.CharField(max_length=100, verbose_name='Хобби')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('avatar', models.ImageField(upload_to='user_avatar/')),
                ('account_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Организация')),
                ('address', models.CharField(max_length=80, verbose_name='Юридический адрес')),
                ('actual_adress', models.CharField(max_length=80, verbose_name='Фактический адрес')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть введен в формате:\n                «+999999999». Допускается до 15 цифр.', regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон')),
                ('url', models.URLField(verbose_name='Сайт')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_company', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=80, verbose_name='Ф.И.О.')),
                ('position', models.CharField(max_length=80, verbose_name='Должность')),
                ('tel', models.CharField(max_length=80, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('company_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_contact', to='firstapp.Company')),
            ],
            options={
                'verbose_name': 'Контактные лича',
                'verbose_name_plural': 'Контактные лица',
            },
        ),
        migrations.CreateModel(
            name='CompanyObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=80, verbose_name='Адрес объекта')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.Company')),
                ('order_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_object', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.CreateModel(
            name='CompanyObjectWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=80, verbose_name='Работа')),
                ('company_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.CompanyObject')),
                ('user_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Работа',
                'verbose_name_plural': 'Работы',
            },
        ),
        migrations.AddField(
            model_name='companycontact',
            name='company_object_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_object_contact', to='firstapp.CompanyObject'),
        ),
    ]
