# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 08:36
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/home/dang/Test/djangoTest/testProject/image'), upload_to='push/%Y/%m/%d')),
            ],
        ),
    ]
