# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='rate',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]