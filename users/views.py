from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.permissions import UserPermission
from users.serializers import RegisterUserSerializer, UserSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = UserSerializer
