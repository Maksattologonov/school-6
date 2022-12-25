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
        return Response(serializer.data)


class NewsAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = NewsService.get(id=kwargs.get('pk'))
        serializer = NewsListSerializer(queryset, many=False)
        return Response(serializer.data)


class NotificationAPIView(APIView):
    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = NotificationService.filter()[instance_slice]
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)


class NotificationDetailAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = NotificationService.get(id=kwargs.get('pk'))
        serializer = NotificationSerializer(queryset, many=False)
        return Response(serializer.data)
