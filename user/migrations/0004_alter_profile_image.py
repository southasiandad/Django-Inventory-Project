# Generated by Django 5.1.2 on 2025-01-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_staff_profile_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default avatar.jpg', upload_to='profile_images'),
        ),
    ]
