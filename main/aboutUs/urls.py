from django.urls import path
from .views import MainAboutUsListAPIView, AboutUsAPIView, GetTeachersAPIView

urlpatterns = [
    path('', MainAboutUsListAPIView.as_view(), name='list'),
    path('<int:pk>', AboutUsAPIView.as_view(), name='detail'),
    path('teachers', GetTeachersAPIView.as_view(), name='teachers'),
]