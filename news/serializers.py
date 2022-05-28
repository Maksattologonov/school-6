from rest_framework import serializers
from news.models import News, NewsFiles, Notification


class NewsListSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'file', 'created_at')
        depth = 2

    def get_file(self, instance):
        return NewsFiles.objects.filter(news_id=instance).values('id', 'title', 'file')

    def to_representation(self, instance):
        data = super(NewsListSerializer, self).to_representation(instance)
        return {"News": data}


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'title', 'description', 'created_at', 'for_whom')
