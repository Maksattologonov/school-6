from django.contrib import admin
from files.models import Schedule, Gallery, GalleryFiles


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_no', 'file')
    search_fields = ['class_no']
    list_filter = ['class_no']

    class Meta:
        model = Schedule


class GalleryFileAdmin(admin.TabularInline):
    model = GalleryFiles
    extra = 3


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_count')
    search_fields = ('title',)
    list_filter = ['title']
    inlines = [GalleryFileAdmin]

    class Meta:
        model = Gallery

    def file_count(self, obj):
        return GalleryFiles.objects.filter(gallery_id__title=obj).count()

    file_count.short_description = "Сүрөттөрдүн саны"
