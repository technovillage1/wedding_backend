from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, ServiceViewSet, ReviewListAPIView, ReviewDestroyAPIView
router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
urlpatterns = router.urls

urlpatterns += [
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/',ReviewDestroyAPIView.as_view()),
]