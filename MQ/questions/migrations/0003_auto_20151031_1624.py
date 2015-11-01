# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151031_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(to='questions.Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='url',
            field=models.URLField(default='', null=True, max_length=100, blank=True),
        ),
    ]
