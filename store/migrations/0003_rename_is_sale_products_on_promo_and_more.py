# Generated by Django 4.2.7 on 2023-11-13 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_products_is_sale_products_sale_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='is_sale',
            new_name='on_promo',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='sale_price',
            new_name='promo_price',
        ),
    ]
