# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rvce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='sub_code',
            field=models.CharField(default=b'', max_length=9, verbose_name=b'SubCode'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_name',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'SubName'),
        ),
    ]
