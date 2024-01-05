from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from apps.blog.views import NotFoundView


handler404 = NotFoundView.as_view()


urlpatterns = [
    path('', include('apps.blog.urls')),
    path("", include('apps.contacto.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
