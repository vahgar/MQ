# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('downvoted_by', models.ManyToManyField(blank=True, related_name='answers_downvoted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('desc', models.CharField(max_length=1024, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('url', models.URLField(max_length=100, default='')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(to='questions.Topic'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questions.Question', related_name='answers'),
        ),
        migrations.AddField(
            model_name='answer',
            name='upvoted_by',
            field=models.ManyToManyField(blank=True, related_name='answers_upvoted', to=settings.AUTH_USER_MODEL),
        ),
    ]
