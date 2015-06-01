# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('result_name', models.CharField(default=b'', max_length=200, verbose_name=b'Name')),
                ('result_usn', models.CharField(default=b'', max_length=10, serialize=False, verbose_name=b'USN', primary_key=True)),
                ('result_sem', models.PositiveIntegerField(default=0, verbose_name=b'Semester')),
                ('result_sgpa', models.FloatField(default=0.0, verbose_name=b'SGPA')),
                ('result_branch', models.CharField(default=b'', max_length=40, verbose_name=b'Branch')),
                ('result_sub', django_hstore.fields.DictionaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_id', models.AutoField(serialize=False, primary_key=True)),
                ('sub_code', models.CharField(default=b'', max_length=8, verbose_name=b'SubCode')),
                ('sub_name', models.CharField(default=b'', max_length=50, verbose_name=b'SubName')),
                ('sub_sem', models.PositiveIntegerField(default=0, verbose_name=b'SubSem')),
                ('sub_branch', models.CharField(default=b'', max_length=40, verbose_name=b'SubBranch')),
            ],
        ),
    ]
