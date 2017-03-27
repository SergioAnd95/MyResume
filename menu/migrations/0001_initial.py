# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 18:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('href', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('\\/[\\w_+]\\/', message='Это не внутренняя ссылка')], verbose_name='Ссылка')),
            ],
        ),
    ]