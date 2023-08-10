from django.urls import path
from .views import ServiceTypeList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service-types', ServiceTypeList, basename='service')
urlpatterns = router.urls