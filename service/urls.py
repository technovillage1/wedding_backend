from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ServiceTypeViewSet, ServiceViewSet, ReviewAPILict, ReviewAPIDetailView
router = DefaultRouter()
router.register('service-types', ServiceTypeViewSet, basename='service-types')
router.register('services', ServiceViewSet, basename='services')
urlpatterns = router.urls

urlpatterns += [
    path('reviews/', ReviewAPILict.as_view()),
    path('reviews/<int:pk>/', ReviewAPIDetailView.as_view())
]