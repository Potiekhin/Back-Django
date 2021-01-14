from rest_framework import serializers

from product.models import ProductModel, BrandModel, ColorModel


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ['id', 'name']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    color = ColorSerializer(read_only=True)

    class Meta:
        model = ProductModel
        fields = [
            'id',
            'name',
            'img',
            'price',
            'quantity',
            'title',
            'description',
            'brand',
            'color'
        ]

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)


class ProductChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'id',
            'name',
            'img',
            'price',
            'quantity',
            'title',
            'description',
            'brand',
            'color'
        ]
