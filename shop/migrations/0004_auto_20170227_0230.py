# -*- coding: utf-8 -*-
# Generated by Django 1.10.6.dev20170224211624 on 2017-02-27 01:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_glossary_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='mail_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='post_office.EmailTemplate', verbose_name='Template'),
        ),
    ]
