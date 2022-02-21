from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from aboutUs.serializers import MainAboutUsSerializer
from aboutUs.services import AboutUsService
from common.utils import get_instance_slice


class MainAboutUsListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        page = int(request.query_params.get('page', '0'))
        count = int(request.query_params.get('count', '9'))
        instance_slice = get_instance_slice(page=page, count=count)
        queryset = AboutUsService.filter()[instance_slice]
        serializer = MainAboutUsSerializer(queryset, many=True)
        return Response(data={
            'message': "List of the main information's",
            'data': serializer.data,
            'status': status.HTTP_200_OK
        }, status=status.HTTP_200_OK)
