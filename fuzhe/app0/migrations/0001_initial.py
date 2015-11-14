# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=30)),
                ('Publisher', models.CharField(max_length=30)),
                ('PublishDate', models.CharField(max_length=30)),
                ('Price', models.CharField(max_length=30)),
                ('AuthorID', models.ForeignKey(to='app0.Author')),
            ],
        ),
    ]
