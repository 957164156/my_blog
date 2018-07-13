# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.EmailField(max_length=255)),
                ('user_url', models.URLField(blank=True)),
                ('article', models.ForeignKey(to='article.Article')),
            ],
        ),
    ]
