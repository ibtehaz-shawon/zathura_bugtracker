# Generated by Django 2.2 on 2019-05-20 19:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0040_auto_20190515_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertoken',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 20, 19, 30, 29, 964353, tzinfo=utc), verbose_name='First entry time'),
            preserve_default=False,
        ),
    ]