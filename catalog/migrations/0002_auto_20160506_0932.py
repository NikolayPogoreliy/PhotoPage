# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 06:32
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default="", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Category'),
        ),
    ]
