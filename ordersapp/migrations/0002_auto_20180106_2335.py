# Generated by Django 2.0.1 on 2018-01-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отправлен в обработку'), ('PD', 'оплачен'), ('PRD', 'обрабатывается'), ('RDY', 'готов к выдаче')], default='FM', max_length=3, verbose_name='статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создан'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='обновлен'),
        ),
    ]
