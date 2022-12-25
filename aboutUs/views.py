from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from aboutUs.models import GloryBoard
from aboutUs.serializers import MainAboutUsSerializer, FileSerializer, TeachersSerializer, GloryBoardSerializer
from aboutUs.services import AboutUsService, TeachersService, GloryBoardService
from common.utils import get_instance_slice


class MainAboutUsListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = AboutUsService.filter()[instance_slice]
        serializer = MainAboutUsSerializer(queryset, many=True)
        return Response(serializer.data)


class AboutUsAPIView(APIView):

    def get(self, *args, **kwargs):
        queryset = AboutUsService.get(id=kwargs.get('pk'))
        serializer = MainAboutUsSerializer(queryset, many=False)
        return Response(serializer.data)


class GetTeachersAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = TeachersService.filter()
        serializer = TeachersSerializer(queryset, many=True)
        return Response(serializer.data)


class GloryBoardAPIView(APIView):
    def get(self, *args, **kwargs):
        queryset = GloryBoardService.filter()
        serializer = GloryBoardSerializer(queryset, many=True)
        return Response(serializer.data)