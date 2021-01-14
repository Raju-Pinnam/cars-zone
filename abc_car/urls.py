from django.contrib import admin
from django.urls import path, include
from django.conf import settings as django_settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
]

if django_settings.DEBUG:
    urlpatterns += static(django_settings.STATIC_URL, document_root=django_settings.STATIC_ROOT)
    urlpatterns += static(django_settings.MEDIA_URL, document_root=django_settings.MEDIA_ROOT)
