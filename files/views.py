from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils import get_instance_slice
from files.serializers import GallerySerializer, ScheduleSerializer, TitleSerializer, AccreditationSerializer, \
    SliderSerializer
from files.services import FilesService, AccreditationService, SliderService


class GalleryListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = FilesService.filter_gallery()
        serializer = GallerySerializer(queryset, many=True)
        return Response(data={
            'message': "List of the images",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class GalleryAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = FilesService.get_gallery(id=kwargs.get('pk'))
        serializer = GallerySerializer(queryset, many=False)
        return Response(data={
            'message': "Image",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class GalleryTitleAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = FilesService.get_gallery_titles()
        print(queryset)
        serializer = TitleSerializer(queryset, many=True)
        return Response(data={
            'message': "Gallery titles",
            'gallery title': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class ScheduleListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = FilesService.filter_schedule()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the Schedule",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class ScheduleAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = FilesService.get_schedule(id=kwargs.get('pk'))
        serializer = ScheduleSerializer(queryset, many=False)
        return Response(data={
            'message': "Schedule",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class ScheduleTitleAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = FilesService.get_schedule_titles()
        serializer = TitleSerializer(queryset, many=True)
        return Response(data={
            'message': "Schedule titles",
            'class names': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class AccreditationListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = AccreditationService.filter()
        serializer = AccreditationSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the files",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class AccreditationAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = AccreditationService.filter(id=kwargs.get('pk'))
        serializer = AccreditationSerializer(queryset, many=False)
        return Response(data={
            'message': "Accreditation file",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class SliderListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = SliderService.filter()
        serializer = SliderSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the files",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)