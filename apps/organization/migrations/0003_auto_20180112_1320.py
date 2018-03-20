# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-01-12 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180103_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='catgory',
            field=models.CharField(choices=[('orgs', '\u57f9\u8bad\u673a\u6784'), ('humans', '\u4e2a\u4eba'), ('university', '\u9ad8\u6821')], default='orgs', max_length=20, verbose_name='\u673a\u6784\u7c7b\u522b'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='org/%Y/%m', verbose_name='org_logo'),
        ),
    ]