from rest_framework import serializers
from news.models import News, NewsFiles


class NewsListSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'file')
        depth = 2

    def get_file(self, instance):
        return NewsFiles.objects.filter(news_id=instance).values('id', 'title', 'file')

    def to_representation(self, instance):
        data = super(NewsListSerializer, self).to_representation(instance)
        return {"News": data}
