# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvor', '0008_auto_20170121_0554'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prjphoto',
            options={'verbose_name': 'Фото проекта', 'verbose_name_plural': 'Фото проекта'},
        ),
        migrations.AlterField(
            model_name='prjphoto',
            name='prn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='dvor.Project'),
        ),
    ]