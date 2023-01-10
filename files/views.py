from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils import get_instance_slice
from files.serializers import GallerySerializer, ScheduleSerializer, TitleSerializer, AccreditationSerializer, \
    SliderSerializer
from files.services import FilesService, AccreditationService, SliderService


class GalleryListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        queryset = FilesService.filter_gallery()
        serializer = GallerySerializer(queryset, many=True)
        return Response(serializer.data)


class GalleryAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryset = FilesService.get_gallery(id=kwargs.get('pk'))
        serializer = GallerySerializer(queryset, many=False)
        return Response(serializer.data)


class GalleryTitleAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryset = FilesService.get_gallery_titles()
        print(queryset)
        serializer = TitleSerializer(queryset, many=True)
        return Response(serializer.data)


class ScheduleListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        queryset = FilesService.filter_schedule()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)


class ScheduleAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryset = FilesService.get_schedule(id=kwargs.get('pk'))
        serializer = ScheduleSerializer(queryset, many=False)
        return Response(serializer)


class ScheduleTitleAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryset = FilesService.get_schedule_titles()
        serializer = TitleSerializer(queryset, many=True)
        return Response(serializer.data)


class AccreditationListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        queryset = AccreditationService.filter()
        serializer = AccreditationSerializer(queryset, many=True)
        return Response(serializer.data)


class AccreditationAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        queryset = AccreditationService.filter(id=kwargs.get('pk'))
        serializer = AccreditationSerializer(queryset, many=False)
        return Response(serializer.data)


class SliderListAPIView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        queryset = SliderService.filter()
        serializer = SliderSerializer(queryset, many=True)
        return Response(serializer.data)
