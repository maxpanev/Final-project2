# Generated by Django 5.1.4 on 2024-12-20 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_order_items_delete_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='basket',
        ),
    ]