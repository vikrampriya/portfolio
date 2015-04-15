# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150405_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_project',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
