# Generated by Django 4.2.6 on 2023-11-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_order_options_alter_order_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_dt',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата заказа'),
        ),
    ]
