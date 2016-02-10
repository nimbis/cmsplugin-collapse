# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_collapse', '0002_auto_20160210_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collapsible',
            name='title',
            field=models.CharField(max_length=512),
            preserve_default=True,
        ),
    ]
