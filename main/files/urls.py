from django.urls import path
from .views import (
    GalleryAPIView, GalleryTitleAPIView, GalleryListAPIView,
    ScheduleListAPIView, ScheduleAPIView, ScheduleTitleAPIView, SliderAPIView)

urlpatterns = [
    path('gallery/', GalleryListAPIView.as_view(), name='List-gallery'),
    path('gallery/<int:pk>', GalleryAPIView.as_view(), name='Detail-gallery'),
    path('gallery/title/', GalleryTitleAPIView.as_view(), name='Title-gallery'),
    path('schedule/', ScheduleListAPIView.as_view(), name='List-schedule'),
    path('schedule/<int:pk>', ScheduleAPIView.as_view(), name='Detail-schedule'),
    path('schedule/title/', ScheduleTitleAPIView.as_view(), name='Title-schedule'),
    path('slider', SliderAPIView.as_view(), name='slider'),
]
