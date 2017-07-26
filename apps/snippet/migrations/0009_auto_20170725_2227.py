# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0008_auto_20170725_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippetsearchupdate',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='snippetsearchupdate',
            name='deletable_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]