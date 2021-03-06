# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import member.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        ('member', '0002_auto_20180408_0710'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', member.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='like_posts',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='post.Post'),
        ),
    ]
