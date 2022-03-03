from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', include('aboutUs.urls')),
    path('news/',  include('news.urls')),
    path('files/',  include('files.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
