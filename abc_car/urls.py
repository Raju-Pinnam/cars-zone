from django.contrib import admin
from django.urls import path, include
from django.conf import settings as django_settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('cars/', include('cars.urls', namespace='cars')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]

if django_settings.DEBUG:
    urlpatterns += static(django_settings.STATIC_URL, document_root=django_settings.STATIC_ROOT)
    urlpatterns += static(django_settings.MEDIA_URL, document_root=django_settings.MEDIA_ROOT)
