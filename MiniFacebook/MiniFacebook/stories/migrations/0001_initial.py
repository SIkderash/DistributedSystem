# Generated by Django 4.0.5 on 2022-07-23 17:21

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
            ],
        ),
    ]