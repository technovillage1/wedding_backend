from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ServiceType, Service, Review

# Register your models here.

@admin.register(ServiceType)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    
@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ("title",)
    
@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ("service",)