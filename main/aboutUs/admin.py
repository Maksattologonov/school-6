from django.contrib import admin
from django.contrib.admin import display

from .models import MainAboutUs, AboutUsFiles, Teachers


class AboutUsFileAdmin(admin.TabularInline):
    model = AboutUsFiles
    extra = 1


@admin.register(MainAboutUs)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_count', 'description')
    search_fields = ('title',)
    inlines = [AboutUsFileAdmin]

    class Meta:
        model = MainAboutUs

    def file_count(self, obj):
        return AboutUsFiles.objects.filter(about_us__title=obj).count()
    file_count.short_description = "Файлдардын саны"


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'lesson', 'position', 'contacts')
    search_fields = ('name', 'lesson', 'position')


