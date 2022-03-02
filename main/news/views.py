from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils import get_instance_slice
from news.serializers import NewsListSerializer
from news.services import NewsService


class NewsListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = NewsService.filter()[instance_slice]
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
