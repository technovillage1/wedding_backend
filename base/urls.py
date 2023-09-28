from rest_framework.routers import DefaultRouter

from .views import RegionList, DistrictList

router = DefaultRouter(trailing_slash=False)
router.register('regions', RegionList, basename='regions')
router.register('districts', DistrictList, basename='districts')
urlpatterns = router.urls
