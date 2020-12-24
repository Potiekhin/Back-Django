from rest_framework import serializers

from product.models import ProductModel, BrandModel, ColorModel, ProductCartModel
from user.serializers import GetUserIdSerializer
from django.contrib.auth import get_user_model


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


class GetProductIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id']


class ProductCartSerializer(serializers.ModelSerializer):
    product = GetProductIdSerializer(many=True)
    user = GetUserIdSerializer()

    class Meta:
        model = ProductCartModel
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
        # exclude = ['user']

    def create(self, validated_data):
        print(validated_data)
        user = validated_data.get('user')
        print('ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
        print(user['user_id'])
        userModel = get_user_model()
        user = userModel.objects.get(pk=user.get('id'))
        obj = ProductCartModel(user=user, **validated_data)
        obj.save()
        return obj
