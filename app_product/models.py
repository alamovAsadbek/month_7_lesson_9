from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()

    created_at = models.TimeField(auto_created=True)
    updated_at = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
