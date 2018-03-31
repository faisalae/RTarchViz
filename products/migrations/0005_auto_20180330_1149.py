# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180330_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='file_path',
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.user_directory_path, verbose_name='Main Product Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, null=True, upload_to=products.models.user_directory_path, verbose_name='Product File'),
        ),
    ]
