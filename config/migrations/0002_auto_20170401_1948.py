# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='hello_text_en',
            field=models.TextField(null=True, verbose_name='Приветственный текст'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='hello_text_ru',
            field=models.TextField(null=True, verbose_name='Приветственный текст'),
        ),
    ]
