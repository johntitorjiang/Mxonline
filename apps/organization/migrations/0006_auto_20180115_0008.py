# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-15 00:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20180113_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tescher',
            new_name='Teacher',
        ),
    ]