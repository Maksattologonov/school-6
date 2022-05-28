from django.contrib import admin
from news.models import News, NewsFiles, Notification


class NewsFileAdmin(admin.TabularInline):
    model = NewsFiles
    extra = 1


@admin.register(News)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at')
    inlines = [NewsFileAdmin]

    class Meta:
        model = News

    def file_count(self, obj):
        return NewsFiles.objects.filter(news_id__title=obj).count()
    file_count.short_description = "Файлдардын саны"


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'for_whom', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at', 'author')
