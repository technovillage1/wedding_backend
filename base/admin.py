from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Region, District

# Register your models here.

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ("name",)
    
@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    list_display = ("name",)