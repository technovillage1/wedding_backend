from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.permissions import UserPermission
from users.serializers import RegisterUserSerializer, UserSerializer, PhoneConfirmationSerializer


# class UserLoginView(TokenObtainPairView):
#     # permission_classes = [ConfirmedUserPermission]


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class UserConfirmationView(generics.CreateAPIView):
    serializer_class = PhoneConfirmationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = UserSerializer
