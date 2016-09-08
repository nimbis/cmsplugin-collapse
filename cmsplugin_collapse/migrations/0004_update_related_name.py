# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_collapse', '0003_auto_20160210_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accordionheader',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_collapse_accordionheader', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='collapsible',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='cmsplugin_collapse_collapsible', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
