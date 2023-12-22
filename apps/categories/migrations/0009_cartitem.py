# Generated by Django 5.0 on 2023-12-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0008_alter_products_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]