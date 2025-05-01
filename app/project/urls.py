from django.contrib import admin
from django.urls import path, include
from django.conf import settings #nur für Entwicklungsumgebung
from django.conf.urls.static import static #nur für Entwicklungsumgebung

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('edu.urls')),
]
if settings.DEBUG:#nur für Entwicklungsumgebung
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
