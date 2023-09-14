from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin):
    list_display = ("service", 'user', 'booking_date', 'created_at')
