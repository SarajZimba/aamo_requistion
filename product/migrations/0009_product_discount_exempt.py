# Generated by Django 4.0.6 on 2024-06-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_ledger'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_exempt',
            field=models.BooleanField(default=False),
        ),
    ]
