# Generated by Django 4.0 on 2021-12-24 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_btctrystatistics_btctry_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btctry',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
