# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-18 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_1', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe1')),
                ('banner_2', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe2')),
                ('banner_3', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='\u8f6e\u64ad\u56fe3')),
                ('welcome_title', models.CharField(max_length=100, verbose_name='\u6b22\u8fce\u6807\u9898')),
                ('welcome_text1', models.CharField(max_length=100, verbose_name='\u6b22\u8fce\u8bd71')),
                ('welcome_text2', models.CharField(max_length=100, verbose_name='\u6b22\u8fce\u8bd72')),
                ('welcome_text3', models.CharField(max_length=100, verbose_name='\u6b22\u8fce\u8bd73')),
            ],
            options={
                'verbose_name': '\u9996\u9875',
                'verbose_name_plural': '\u9996\u9875',
            },
        ),
    ]
