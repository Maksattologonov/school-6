from django.urls import path
from .views import NewsAPIView, NewsListAPIView, NotificationDetailAPIView, NotificationAPIView

urlpatterns = [
    path('', NewsListAPIView.as_view(), name='List'),
    path('<int:pk>', NewsAPIView.as_view(), name='Detail'),
    path('notification', NotificationAPIView.as_view(), name='List-notification'),
    path('notification/<int:pk>', NotificationDetailAPIView.as_view(), name='Detail-notification'),
]