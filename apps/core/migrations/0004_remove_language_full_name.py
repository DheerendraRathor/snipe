# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-25 05:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_language_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='full_name',
        ),
    ]
