# Generated by Django 5.0 on 2024-03-08 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart_cartitem_cart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
