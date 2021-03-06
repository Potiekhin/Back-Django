from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from order.models import CartModel
from order.serializers import CartSerializer, CartProductSerializer


class CartView(APIView):
    serializer_class = CartSerializer

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        if type(data) is list:
            for item in data:
                item2 = {'user': pk, "quantity": item['quantity'], "product": item['product']['id']}
                serializer = CartSerializer(data=item2, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            return Response(data, status.HTTP_201_CREATED)
        else:
            data['user'] = pk
            serializer = CartSerializer(data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        user = kwargs.get('pk')
        cart = CartModel.objects.filter(user=user)
        if not cart:
            return Response({'msg': 'user not found'})
        return Response(CartProductSerializer(cart, many=True).data, status.HTTP_200_OK)


class EditCartView(APIView):
    serializer_class = CartSerializer

    def delete(self, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = CartModel.objects.filter(product=product_id).first()
        if not product:
            return Response({'msg': 'product not found'}, status.HTTP_200_OK)
        product.delete()
        return Response({'msg': 'product deleted'}, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = CartModel.objects.filter(product=product_id).first()
        if not product:
            return Response({'msg': 'product not found'})
        serializer = CartSerializer(product, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class CleanCartView(APIView):
    def delete(self, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CartModel.objects.filter(user=user_id)
        if not user:
            return Response({'msg': 'user not found'}, status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'msg': 'cart deleted'}, status.HTTP_200_OK)
