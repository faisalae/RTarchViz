# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_active'),
        ('checkout', '0007_auto_20180416_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasehistory',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='product_file',
        ),
        migrations.RemoveField(
            model_name='purchasehistory',
            name='product_id',
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
            preserve_default=False,
        ),
    ]