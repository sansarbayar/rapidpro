# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 19:08
from __future__ import unicode_literals

from django.db import migrations


def fail():
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0086_is_squashed'),
    ]

    operations = [
        migrations.RunPython(fail)
    ]
