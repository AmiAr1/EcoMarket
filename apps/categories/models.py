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
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.title


class CartItem(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)





