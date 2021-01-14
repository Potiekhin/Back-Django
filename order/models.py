from django.db import models

from product.models import ProductModel
from user.models import UserModel


class CartModel(models.Model):
    class Meta:
        db_table = 'cart'

    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()


class OrderModel(models.Model):
    class Meta:
        db_table = 'order'

    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now=True)
