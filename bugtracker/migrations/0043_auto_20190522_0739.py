# Generated by Django 2.2 on 2019-05-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0042_organisation_usertoorg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='_id',
            field=models.UUIDField(blank=True, primary_key=True, serialize=False, unique=True),
        ),
    ]