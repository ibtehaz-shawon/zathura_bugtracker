# Generated by Django 2.2 on 2019-05-06 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0004_auto_20190506_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('217d8fc8-5ed2-4a0e-8fd3-ba499757293a'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 38, 37, 452196, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('9e255ec9-f2f9-4e5d-b454-9adab276001d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 38, 37, 453839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('942ab487-916d-43d1-86cf-4365ce449e08'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('e9b88d36-178b-47dc-ba8d-1ac33410b803'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 38, 37, 451433, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 38, 37, 450216, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 38, 37, 450246, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('128dc847-adbf-41ce-8621-ca2de8245e27'), primary_key=True, serialize=False, unique=True),
        ),
    ]
