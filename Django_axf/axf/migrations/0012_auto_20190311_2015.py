# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-11 12:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0011_cart'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='axf_cart',
        ),
    ]
