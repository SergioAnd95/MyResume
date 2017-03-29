# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 09:43
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170226_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='resumeblock',
            name='text_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='resumeblock',
            name='text_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='resumeblock',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='resumeblock',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
    ]
