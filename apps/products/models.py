from django.db import models
from apps.categories.models import Category, resize_image
# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=False, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, verbose_name='фото')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            resize_image(self.image.path, (300, 300))
