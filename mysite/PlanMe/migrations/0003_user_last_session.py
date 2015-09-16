# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlanMe', '0002_auto_20150915_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_session',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
