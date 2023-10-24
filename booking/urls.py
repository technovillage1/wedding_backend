from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import BookingViewSet, ScheduleAPIView, ScheduleDetailAPIView

router = DefaultRouter(trailing_slash=False)
router.register('bookings', BookingViewSet, basename='booking')
urlpatterns = router.urls  + [
    path("schedules", ScheduleAPIView.as_view(), name='schedules'),
    path("schedules/<int:pk>", ScheduleDetailAPIView.as_view(), name='schedule-detail'),
]
