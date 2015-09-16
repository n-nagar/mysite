# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlanMe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='image_url',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_tok',
            field=models.CharField(default=None, max_length=1024),
            preserve_default=False,
        ),
    ]
