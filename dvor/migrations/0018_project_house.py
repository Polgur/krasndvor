# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvor', '0017_auto_20170204_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='house',
            field=models.SmallIntegerField(choices=[(1, 'Одноэтажный'), (2, 'С мансардой'), (3, 'Двухэтажный'), (4, 'Баня'), (5, 'Дуплекс')], default=3),
            preserve_default=False,
        ),
    ]
