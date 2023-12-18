from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='', null=True)
    title = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Название'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(max_length=20, null=True, blank=True, verbose_name='цена')

    def __str__(self):
        return self.title







