# Generated by Django 2.2.4 on 2021-06-06 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_order_orderdesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
    ]