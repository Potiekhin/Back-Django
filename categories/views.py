from rest_framework.views import APIView
from rest_framework.response import Response

from categories.models import ProductCategoriesModel, SubProductCategoriesModel
from categories.serializers import ProductCategoriesSerializer, ProductSubCategoriesSerializer


class ProductCategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def get(self, request):
        category = ProductCategoriesModel.objects.all()
        return Response(ProductCategoriesSerializer(category, many=True).data)

    def post(self, request):
        serializer = ProductCategoriesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)


class EditProductCategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        category = ProductCategoriesModel.objects.filter(pk=pk).first()
        if not category:
            return Response({'msg': 'Category not found'})
        serializer = ProductCategoriesSerializer(category, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        category = ProductCategoriesModel.objects.filter(pk=pk).first()
        if not category:
            return Response({'msg': 'Category not found'})
        category.delete()
        return Response({'msg': 'Category deleted'})


class ProductSubCategoriesView(APIView):
    serializer_class = ProductSubCategoriesSerializer

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        sub_category = SubProductCategoriesModel.objects.filter(categories_id=pk)
        return Response(ProductSubCategoriesSerializer(sub_category, many=True).data)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = ProductSubCategoriesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data)
        serializer.save(categories_id=pk)
        return Response(serializer.data)


class EditSubProductCategoriesView(APIView):
    serializer_class = ProductSubCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        sub_category = SubProductCategoriesModel.objects.filter(pk=pk).first()
        if not sub_category:
            return Response({'msg': 'Subcategory not found'})
        serializer = ProductSubCategoriesSerializer(sub_category, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        sub_category = SubProductCategoriesModel.objects.filter(pk=pk).first()
        if not sub_category:
            return Response({'msg': 'Subcategory not found'})
        sub_category.delete()
        return Response({'msg': 'Subcategory deleted'})
