# Generated by Django 2.0.1 on 2018-01-08 16:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0021_auto_20180108_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='address',
            field=models.TextField(blank=True, max_length=512, verbose_name='адрес'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 16, 38, 58, 813013, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
