from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Документация для API",
      default_version='v1',
      description="Документация для API Школы №6",
      contact=openapi.Contact(email="maksattologonovn@gmail.com", name="Maksat Tologonov"),
      license=openapi.License(name="Лиценция компании Redtrace.inc"),
   ),
   public=True,
)

i18n_urls = (
    re_path('admin/', admin.site.urls),
    re_path('i18n/', include('django.conf.urls.i18n')),
)


urlpatterns = [
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/about_us/', include('aboutUs.urls')),
    path('api/news/',  include('news.urls')),
    path('api/files/',  include('files.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)
urlpatterns.extend(i18n_patterns(*i18n_urls, prefix_default_language=False))
urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

admin.site.site_header = "Школа №6"
