# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imageledger', '0012_add_user_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tags', to='imageledger.Tag'),
        ),
    ]
