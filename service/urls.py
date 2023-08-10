from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, ServiceViewSet

router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
urlpatterns = router.urls