# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('mob_no', models.CharField(max_length=13)),
                ('branch', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ProblemBank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem_statement', models.CharField(max_length=5000)),
                ('submitted_by', models.CharField(max_length=60)),
                ('mob_no', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
