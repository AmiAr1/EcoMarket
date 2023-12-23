from django.db import models
from PIL import Image


def resize_image(image_path, max_size):
    img = Image.open(image_path)
    if img.height > max_size[1] or img.width > max_size[0]:
        img.thumbnail(max_size)
        img.save(image_path)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path, (300, 300))


class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=Category.objects.first())

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path, (300, 300))


class CartItem(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)




