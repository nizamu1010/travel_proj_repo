from django.contrib import admin
from django.urls import include, path

from TRL_Proj import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('TRL_app.urls')),
    path('admin/', admin.site.urls),
    path('auth_app/', include('auth_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
