# Generated by Django 3.1 on 2020-10-26 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 26, 15, 2, 20, 985453, tzinfo=utc)),
        ),
    ]
