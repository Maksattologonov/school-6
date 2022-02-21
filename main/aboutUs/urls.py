from django.urls import path
from .views import MainAboutUsListAPIView

urlpatterns = [
    path('', MainAboutUsListAPIView.as_view(), name='get'),
]