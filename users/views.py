from rest_framework import generics, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.permissions import UserPermission
from users.serializers import RegisterUserSerializer, UserSerializer, PhoneConfirmationSerializer, \
    ResendConfirmationSerializer


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


class UserResendConfirmationView(generics.CreateAPIView):
    serializer_class = ResendConfirmationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_200_OK)


class UserViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'delete']
    serializer_class = UserSerializer

    @action(methods=["GET"], detail=False, url_path="me", url_name="users_me")
    def me(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
