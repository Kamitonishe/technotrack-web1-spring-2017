# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_postlike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
