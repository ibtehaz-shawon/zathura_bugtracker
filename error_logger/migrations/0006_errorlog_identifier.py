# Generated by Django 2.2.4 on 2019-09-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('error_logger', '0005_auto_20190926_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorlog',
            name='identifier',
            field=models.CharField(blank=True, default='Anonymous', max_length=50, null=True),
        ),
    ]
