from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ServiceTypeReadOnlyViewSet, ServiceViewSet

router = DefaultRouter()
router.register('service-types', ServiceTypeReadOnlyViewSet, basename='servise-types')
router.register('services', ServiceViewSet, basename='services')
urlpatterns = router.urls
