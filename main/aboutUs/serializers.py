from abc import ABC

from rest_framework import serializers

from aboutUs.models import MainAboutUs, AboutUsFiles, Teachers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsFiles
        fields = "__all__"
        depth = 2


class MainAboutUsSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = MainAboutUs
        fields = ('id', 'title', 'description', 'file')
        depth = 2

    def get_file(self, instance):
        return AboutUsFiles.objects.filter(about_us=instance).values('id', 'title', 'file')


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'