# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_collapse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accordionheader',
            name='show_first',
            field=models.BooleanField(default=True, help_text='If selected, the first collapsible will be displayed in the open state.'),
            preserve_default=True,
        ),
    ]
