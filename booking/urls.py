from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import BookingViewSet, BookingAcceptedView, BookingRejectedView, BookingCancelledView, ScheduleAPIView, ScheduleDetailAPIView

router = DefaultRouter(trailing_slash=False)
router.register('bookings', BookingViewSet, basename='booking')
urlpatterns = router.urls
urlpatterns += [
    path('bookings/<int:pk>/accepted', BookingAcceptedView.as_view()),
    path('bookings/<int:pk>/rejected', BookingRejectedView.as_view()),
    path('bookings/<int:pk>/cancelled', BookingCancelledView.as_view()),
    path("schedules", ScheduleAPIView.as_view(), name='schedules'),
    path("schedules/<int:pk>", ScheduleDetailAPIView.as_view(), name='schedule-detail'),
]
