# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 14:38
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvor', '0010_auto_20170122_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrjKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price1', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('kit1', ckeditor.fields.RichTextField()),
                ('kit2', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Комплектации',
                'verbose_name': 'Комплектация',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='vid',
            field=models.SmallIntegerField(choices=[(1, 'Коттедж'), (2, 'Дуплекс'), (3, 'Баня')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prjkit',
            name='prn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kits', to='dvor.Project'),
        ),
        migrations.AddField(
            model_name='prjkit',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dvor.Techno'),
        ),
    ]
