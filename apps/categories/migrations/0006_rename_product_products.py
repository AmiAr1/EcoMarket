# Generated by Django 5.0 on 2023-12-21 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_product_category_alter_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Products',
        ),
    ]
