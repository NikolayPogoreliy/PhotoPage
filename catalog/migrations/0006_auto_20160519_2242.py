# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20160519_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(blank=True, default='', max_length=250, verbose_name='Название'),
        ),
    ]
