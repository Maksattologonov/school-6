from django.urls import path
from .views import MainAboutUsListAPIView, AboutUsAPIView, GetTeachersAPIView, GloryBoardAPIView, SchoolAdmissionAPIView

urlpatterns = [
    path('', MainAboutUsListAPIView.as_view(), name='list'),
    path('<int:pk>', AboutUsAPIView.as_view(), name='detail'),
    path('teachers', GetTeachersAPIView.as_view(), name='teachers'),
    path('glory-board', GloryBoardAPIView.as_view(), name='glory-board'),
    path('school-admission', SchoolAdmissionAPIView.as_view(), name='school-admission'),
]