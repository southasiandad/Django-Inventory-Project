# Generated by Django 5.1.2 on 2025-01-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
