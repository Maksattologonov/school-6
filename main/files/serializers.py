from rest_framework import serializers

from files.models import Gallery, GalleryFiles, Schedule, Slider, SchoolDocumentsFiles, SchoolDocuments, Accreditation


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
        return data


class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id', 'class_no', 'file')
        depth = 2


class TitleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    class_no = serializers.CharField(read_only=True)


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title', 'sub_title', 'file')


class SchoolDocumentsSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = SchoolDocuments
        fields = ('id', 'title', 'created_at', 'file')
        depth = 2

    def get_file(self, instance):
        return SchoolDocumentsFiles.objects.filter(doc_id=instance).values('id', 'doc_id', 'file')

    def to_representation(self, instance):
        data = super(SchoolDocumentsSerializer, self).to_representation(instance)
        return data


class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = ('id', 'title', 'file')
