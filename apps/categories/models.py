from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(
        max_length=100, null=True, blank=False, verbose_name='Название'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(max_length=20, null=True, blank=True, verbose_name='цена')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  default=1)


    def __str__(self):
        return self.title







