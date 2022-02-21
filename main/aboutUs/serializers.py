from rest_framework import serializers

from aboutUs.models import MainAboutUs


class MainAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainAboutUs
        fields = '__all__'
