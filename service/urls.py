from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, ServiceViewSet, ReviewViewSet

router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
router.register('reviews', ReviewViewSet, basename='reviews')
urlpatterns = router.urls