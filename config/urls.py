from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as doc_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('service.urls')),
    path('api/v1/', include('base.urls')),
    path('api/v1/', include('users.urls')),
    path('api/v1/', include('booking.urls')),
]
urlpatterns += doc_api

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
