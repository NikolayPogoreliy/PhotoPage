# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 12:20
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='full_text',
        ),
        migrations.RemoveField(
            model_name='services',
            name='shot_text',
        ),
        migrations.AddField(
            model_name='category',
            name='shot_description',
            field=tinymce.models.HTMLField(blank=True, help_text='Этот текст будет выведен до подчиненных категорий или сервисов', verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='materials',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='materials',
            name='meta_desc',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Мета описание'),
        ),
        migrations.AddField(
            model_name='materials',
            name='meta_key',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='materials',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Этот текст будет выведен после подчиненных категорий или сервисов', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_key',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='services',
            name='meta_key',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Ключевые слова'),
        ),
    ]