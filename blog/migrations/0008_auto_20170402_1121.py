# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categories',
        ),
    ]
