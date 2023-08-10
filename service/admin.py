from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ServiceType

# Register your models here.

@admin.register(ServiceType)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ("name",)