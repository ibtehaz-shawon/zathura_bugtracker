# Generated by Django 2.2.4 on 2019-09-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('error_logger', '0004_auto_20190926_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verboselog',
            name='log_title',
        ),
        migrations.AddField(
            model_name='verboselog',
            name='point_of_origin',
            field=models.CharField(default='Model default', max_length=100),
            preserve_default=False,
        ),
    ]
