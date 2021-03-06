# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 14:58
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('published', models.BooleanField(default=1, verbose_name='Опубликовать')),
                ('slug', models.SlugField(blank=True, default='about_us', max_length=250, verbose_name='УРЛ')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Информация о нас',
                'verbose_name_plural': 'Информация о нас',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(blank=True, max_length=300, null=True, verbose_name='Контакт')),
                ('published', models.BooleanField(verbose_name='Доступен')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=250, verbose_name='Тип контакта')),
            ],
            options={
                'verbose_name': 'Тип контакта',
                'verbose_name_plural': 'Типы контактов',
            },
        ),
        migrations.AddField(
            model_name='contacts',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inform.ContactType', verbose_name='Тип контакта'),
        ),
    ]
