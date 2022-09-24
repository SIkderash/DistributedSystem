# Generated by Django 4.1 on 2022-08-28 06:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('uid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]