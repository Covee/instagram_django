# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-11 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='passed_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]