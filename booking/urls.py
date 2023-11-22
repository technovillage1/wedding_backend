from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookingViewSet, BookingAcceptedView, BookingRejectedView, BookingCancelledView, ScheduleAPIView, \
    ScheduleDetailAPIView

router = DefaultRouter(trailing_slash=False)
router.register('bookings', BookingViewSet, basename='booking')
urlpatterns = router.urls + [
    path('bookings/<int:pk>/accept', BookingAcceptedView.as_view()),
    path('bookings/<int:pk>/reject', BookingRejectedView.as_view()),
    path('bookings/<int:pk>/cancel', BookingCancelledView.as_view()),
    path("schedules", ScheduleAPIView.as_view(), name='schedules'),
    path("schedules/<int:pk>", ScheduleDetailAPIView.as_view(), name='schedule-detail'),
]
