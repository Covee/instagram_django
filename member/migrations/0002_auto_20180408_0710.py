# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('m', '남성'), ('f', '여성'), ('o', '기타')], default='o', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, upload_to='user'),
        ),
    ]
