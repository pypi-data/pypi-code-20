# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsonconfig', '0015_config_mac_address_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpn',
            name='dh',
            field=models.TextField(blank=True),
        ),
    ]
