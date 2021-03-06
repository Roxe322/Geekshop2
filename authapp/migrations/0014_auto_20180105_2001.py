# Generated by Django 2.0.1 on 2018-01-05 15:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20180105_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='me',
            field=models.CharField(blank=True, max_length=256, verbose_name='me'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 15, 1, 22, 236017, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
