# Generated by Django 2.2 on 2019-05-06 08:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0008_auto_20190506_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('64fde924-bcde-41d2-ae52-5f9819a12aa7'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 42, 36, 344751, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='errors',
            name='resolved_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='bugtracker.User'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('2946d8f6-c296-4c8a-be54-ef1296460fde'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 42, 36, 345787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('ce1cc29e-c98c-4b7a-b16c-73cdf3d8abd5'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('e3c17d76-4f12-41f9-8f48-2adc6f5d4c5d'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 42, 36, 344311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 42, 36, 343760, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 8, 42, 36, 343787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('b7cfc544-5df9-4e1c-a8a3-94b492da260a'), primary_key=True, serialize=False, unique=True),
        ),
    ]
