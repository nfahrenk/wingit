# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seating', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='industry',
            field=models.CharField(default='Computer Science', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='prefersBusiness',
            field=models.BooleanField(default=False),
        ),
    ]
