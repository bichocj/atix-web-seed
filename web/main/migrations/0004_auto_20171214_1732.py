# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 17:32
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171207_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=redactor.fields.RedactorField(verbose_name='contenido'),
        ),
    ]