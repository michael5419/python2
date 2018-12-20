# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-18 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20181018_0312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-age'], 'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(null=True, upload_to='static/upload', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮件'),
        ),
        migrations.AlterField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='激活用户'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30, verbose_name='姓名'),
        ),
    ]