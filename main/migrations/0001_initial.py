# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 11:13
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChronologicalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('from_date', models.DateField(auto_now_add=True, verbose_name='Дата начала')),
                ('to_date', models.DateField(auto_now_add=True, verbose_name='Дата окончания')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
            ],
            options={
                'ordering': ['from_date', 'to_date'],
                'verbose_name': 'Хронологические данные',
                'verbose_name_plural': 'Хронологические данные',
            },
        ),
        migrations.CreateModel(
            name='ResumeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
                ('is_display', models.BooleanField(default=True, verbose_name='Отображать?')),
            ],
            options={
                'verbose_name': 'Раздел резюме',
                'verbose_name_plural': 'Разделы резюме',
            },
        ),
        migrations.CreateModel(
            name='SkillsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Значение')),
                ('resume_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills_data', to='main.ResumeBlock', verbose_name='Раздел резюме')),
            ],
            options={
                'verbose_name': 'Размерные данные',
                'verbose_name_plural': 'Размерные данные',
            },
        ),
        migrations.AddField(
            model_name='chronologicaldata',
            name='resume_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chrono_data', to='main.ResumeBlock', verbose_name='Раздел резюме'),
        ),
    ]
