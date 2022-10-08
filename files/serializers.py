from rest_framework import serializers

from files.models import Gallery, GalleryFiles, Schedule, ScheduleFiles


class GallerySerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = ('id', 'title', 'file')
        depth = 2

    def get_file(self, instance):
        return GalleryFiles.objects.filter(gallery_id=instance).values('id', 'gallery_id', 'file')

    def to_representation(self, instance):
        data = super(GallerySerializer, self).to_representation(instance)
        return {"Gallery": data}


class ScheduleSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ('id', 'class_no', 'file')
        depth = 2

    def get_file(self, instance):
        return ScheduleFiles.objects.filter(schedule_id=instance).values('id', 'schedule_id', 'file')

    def to_representation(self, instance):
        data = super(ScheduleSerializer, self).to_representation(instance)
        return {"Schedule": data}


class TitleSerializer(serializers.Serializer):
    class_no = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id', 'title', 'file')
