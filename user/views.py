from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .serializers import UserSerializer, GetUserSerializer
from .models import UserModel
from rest_framework.views import APIView
from rest_framework.response import Response


class SingUpView(CreateAPIView):
    serializer_class = UserSerializer


class UserView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class GetUserDataView(APIView):
    def get(self, request):
        user = UserSerializer(request.user).data
        return Response(user)
