# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='href',
            field=models.CharField(max_length=100, verbose_name='Ссылка'),
        ),
    ]
