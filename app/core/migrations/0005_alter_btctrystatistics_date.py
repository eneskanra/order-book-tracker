# Generated by Django 4.0 on 2021-12-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_btctry_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btctrystatistics',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
