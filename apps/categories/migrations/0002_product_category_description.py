# Generated by Django 5.0 on 2023-12-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(blank=True, max_length=20, null=True, verbose_name='цена')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
