# Generated by Django 5.1.4 on 2024-12-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
    ]