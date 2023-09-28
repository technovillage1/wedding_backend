from rest_framework.routers import DefaultRouter

from .views import ServiceTypeViewSet, ServiceViewSet, AttachmentViewSet, ReviewViewSet

router = DefaultRouter(trailing_slash=False)
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
router.register('attachments', AttachmentViewSet, basename='attachments')
router.register('reviews', ReviewViewSet, basename='reviews')
urlpatterns = router.urls
