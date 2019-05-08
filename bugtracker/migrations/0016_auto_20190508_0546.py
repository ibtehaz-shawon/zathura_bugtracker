# Generated by Django 2.2 on 2019-05-08 05:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0015_auto_20190508_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('d0852000-74e7-4466-a835-4b09ec515865'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 643056, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='errors',
            name='point_of_origin',
            field=models.CharField(default=datetime.datetime(2019, 5, 8, 5, 46, 21, 914933, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('85cd1351-436b-4e18-b5b0-7905586786d0'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 643871, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('592b6e0a-f243-4596-b6fa-63635606fcac'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('7c1073f4-b338-4c4f-84ce-b4e461938107'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 641892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('19a6e40e-7e70-4bdc-b5cc-7006e6dcfd93'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 642516, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('1fafde4c-e99d-4ea3-86ef-894a668dfd9f'), unique=True),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('ebf2a36e-4fc0-4a46-b95c-c94d8b6f40d8'), unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 641071, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 8, 5, 45, 45, 641221, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('6345d95c-2bc6-4052-bf42-58ad37fb7059'), primary_key=True, serialize=False, unique=True),
        ),
    ]