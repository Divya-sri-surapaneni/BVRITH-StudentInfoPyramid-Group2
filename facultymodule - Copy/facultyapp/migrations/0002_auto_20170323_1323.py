# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Remarks',
            new_name='Student_ID',
        ),
    ]
