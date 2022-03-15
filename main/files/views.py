from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils import get_instance_slice
from files.serializers import GallerySerializer, ScheduleSerializer, TitleSerializer, SlideSerializer, \
    SchoolDocumentsSerializer
from files.services import FilesService, SliderService, SchoolDocumentsService


class GalleryListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = FilesService.filter_gallery()[instance_slice]
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
        serializer = TitleSerializer(queryset, many=True)
        return Response(data={
            'message': "Gallery titles",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class ScheduleListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = FilesService.filter_schedule()[instance_slice]
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
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class SliderAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = SliderService.filter()
        serializer = SlideSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the sliders",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class SchoolDocumentsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = SchoolDocumentsService.filter()
        serializer = SchoolDocumentsSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the sliders",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)