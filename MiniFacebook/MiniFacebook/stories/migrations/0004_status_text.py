# Generated by Django 4.0.5 on 2022-07-23 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_status_time_stories_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='text',
            field=models.CharField(default='HEllo', max_length=1000),
            preserve_default=False,
        ),
    ]
