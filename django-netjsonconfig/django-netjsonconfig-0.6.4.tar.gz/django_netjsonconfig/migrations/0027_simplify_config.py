# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0026_config_device_not_null'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='name',
        ),
        migrations.RemoveField(
            model_name='config',
            name='key',
        ),
        migrations.RemoveField(
            model_name='config',
            name='mac_address',
        ),
    ]
