from django.db import models
import os
from categories.models import SubProductCategoriesModel


class BrandModel(models.Model):
    class Meta:
        db_table = 'product_brand'

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.id} {self.name}'


class ColorModel(models.Model):
    class Meta:
        db_table = 'product_color'

    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.id} {self.name}'


class TitleModel(models.Model):
    class Meta:
        db_table = 'product_title'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} {self.name}'


class DescriptionModel(models.Model):
    class Meta:
        db_table = 'product_description'

    name = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.id} {self.name}'


class ProductModel(models.Model):
    class Meta:
        db_table = 'product'

    sub_category = models.ForeignKey(SubProductCategoriesModel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    img = models.ImageField(upload_to=os.path.join('product', 'img'))
    brand = models.ForeignKey(BrandModel, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(ColorModel, on_delete=models.SET_NULL, null=True)
    title = models.ForeignKey(TitleModel, on_delete=models.SET_NULL, null=True)
    description = models.ForeignKey(DescriptionModel, on_delete=models.SET_NULL, null=True)
