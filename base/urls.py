from rest_framework.routers import DefaultRouter
from .views import RegionList, DistrictList

router = DefaultRouter()
router.register('regions', RegionList, basename='regions')
router.register('districts', DistrictList, basename='districts')
urlpatterns = router.urls