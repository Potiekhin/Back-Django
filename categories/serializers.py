from rest_framework import serializers
from .models import ProductCategoriesModel, SubProductCategoriesModel


class ProductCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoriesModel
        fields = '__all__'


class ProductSubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProductCategoriesModel
        fields = '__all__'
        extra_kwargs = {'categories': {'read_only': True}}
