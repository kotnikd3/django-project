# Generated by Django 3.2.5 on 2021-07-25 19:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 25, 19, 23, 3, 329114, tzinfo=utc)),
        ),
    ]
