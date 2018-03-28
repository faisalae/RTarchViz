# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180321_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=200, unique_for_month='published_date'),
        ),
    ]