# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-03 00:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citydict',
            options={'verbose_name': '\u57ce\u5e02\u4fe1\u606f', 'verbose_name_plural': '\u57ce\u5e02\u4fe1\u606f'},
        ),
        migrations.RenameField(
            model_name='tescher',
            old_name='work_yesr',
            new_name='work_year',
        ),
    ]
