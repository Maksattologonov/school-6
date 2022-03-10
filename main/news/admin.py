from django.contrib import admin
from news.models import News, NewsFiles, Notification, ForWhom


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


class NotificationForWhom(admin.TabularInline):
    model = ForWhom
    extra = 1


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'created_at', 'author')
    inlines = [NotificationForWhom]
