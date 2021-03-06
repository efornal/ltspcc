# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 15:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_add_field_attributes_to_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dns_name', models.CharField(max_length=200, verbose_name='dns_name')),
                ('mac_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='mac_address')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Group', verbose_name='grupo')),
            ],
            options={
                'db_table': 'nodes',
                'verbose_name': 'Node',
                'verbose_name_plural': 'Nodes',
            },
        ),
    ]
