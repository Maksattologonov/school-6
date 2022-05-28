from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils import get_instance_slice
from news.serializers import NewsListSerializer, NotificationSerializer
from news.services import NewsService, NotificationService


class NewsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = NewsService.filter()
        serializer = NewsListSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the news",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class NewsAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = NewsService.get(id=kwargs.get('pk'))
        serializer = NewsListSerializer(queryset, many=False)
        return Response(data={
            'message': "News",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class NotificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = NotificationService.filter()
        serializer = NotificationSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the Notification",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)


class NotificationDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = NotificationService.get(id=kwargs.get('pk'))
        serializer = NotificationSerializer(queryset, many=False)
        return Response(data={
            'message': "Notification",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
