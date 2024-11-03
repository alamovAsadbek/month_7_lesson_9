from django.db import models

from app_product.models import ProductModel
from app_user.models import UserModel


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product')
    comment = models.TextField()

    created_at = models.TimeField(auto_now_add=True)
    update_at = models.TimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.comment
