from rest_framework import serializers

from order.models import OrderModel, CartModel
from product.models import ProductModel
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'
        extra_kwargs = {"user": {"write_only": True}}
        # exclude = ('user',)

    # def create(self, validated_data):
    #     print(validated_data)
    #     return super().create(validated_data)


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartModel
        fields = ['id', 'product', 'user', 'quantity']
        extra_kwargs = {"user": {"write_only": True}, "product": {"read_only": True}}


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
