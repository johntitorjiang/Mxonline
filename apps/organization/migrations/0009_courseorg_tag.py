# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-02-03 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0008_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='\u667a\u6167\u725b\u903c', max_length=100, verbose_name='\u673a\u6784\u6807\u7b7e'),
        ),
    ]
