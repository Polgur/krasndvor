# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 15:55
from __future__ import unicode_literals

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dvor', '0021_reconst_reconstphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='reconst',
            name='img',
            field=sorl.thumbnail.fields.ImageField(default='1', upload_to='reconstr'),
            preserve_default=False,
        ),
    ]
