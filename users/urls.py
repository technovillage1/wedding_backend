from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView

from .views import UserRegistrationView, UserViewSet, UserConfirmationView

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
                  path('users/register/', UserRegistrationView.as_view()),
                  path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('users/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
                  path('users/confirm/', UserConfirmationView.as_view(), name="user_confirm"),
              ] + router.urls
