from django.urls import path
from .views import NewsAPIView, NewsListAPIView

urlpatterns = [
    path('', NewsListAPIView.as_view(), name='List'),
    path('<int:pk>', NewsAPIView.as_view(), name='Detail'),
]