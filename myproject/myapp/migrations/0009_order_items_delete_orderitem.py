# Generated by Django 5.1.4 on 2024-12-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='myapp.basketitem'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]