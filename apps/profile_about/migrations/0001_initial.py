# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-18 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u540d\u5b57')),
                ('birthday', models.CharField(max_length=20, verbose_name='\u751f\u65e5')),
                ('emial', models.CharField(max_length=50, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=11, verbose_name='\u624b\u673a\u53f7\u7801')),
                ('adress', models.CharField(max_length=50, verbose_name='\u5730\u5740')),
                ('good_at1', models.CharField(max_length=50, verbose_name='\u7279\u957f1')),
                ('good_at2', models.CharField(max_length=50, verbose_name='\u7279\u957f2')),
                ('good_at3', models.CharField(max_length=50, verbose_name='\u7279\u957f3')),
                ('poem_title', models.CharField(max_length=20, verbose_name='\u8bd7\u6b4c\u9898\u76ee')),
                ('poem_content1', models.CharField(max_length=50, verbose_name='\u8bd7\u53e51')),
                ('poem_content2', models.CharField(max_length=50, verbose_name='\u8bd7\u53e52')),
                ('poem_content3', models.CharField(max_length=50, verbose_name='\u8bd7\u53e53')),
                ('poem_content4', models.CharField(max_length=50, verbose_name='\u8bd7\u53e54')),
                ('poem_content5', models.CharField(max_length=50, verbose_name='\u8bd7\u53e55')),
                ('poem_content6', models.CharField(max_length=50, verbose_name='\u8bd7\u53e56')),
                ('poem_content7', models.CharField(max_length=50, verbose_name='\u8bd7\u53e57')),
                ('poem_content8', models.CharField(max_length=50, verbose_name='\u8bd7\u53e58')),
                ('poem_content9', models.CharField(max_length=50, verbose_name='\u8bd7\u53e59')),
                ('poem_content10', models.CharField(max_length=50, verbose_name='\u8bd7\u53e510')),
                ('poem_content11', models.CharField(max_length=50, verbose_name='\u8bd7\u53e511')),
            ],
            options={
                'verbose_name': '\u4e2a\u4eba\u7b80\u4ecb',
                'verbose_name_plural': '\u4e2a\u4eba\u7b80\u4ecb',
            },
        ),
    ]