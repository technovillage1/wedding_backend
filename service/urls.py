from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, ServiceViewSet, AttachmentViewSet

router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
router.register('attachments', AttachmentViewSet, basename='attachments')
urlpatterns = router.urls