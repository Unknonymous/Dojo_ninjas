# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 04:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='age',
        ),
        migrations.RemoveField(
            model_name='ninja',
            name='desc',
        ),
        migrations.AddField(
            model_name='ninja',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
