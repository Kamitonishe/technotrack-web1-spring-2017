# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20170313_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='description',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
