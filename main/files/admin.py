from django.contrib import admin
from files.models import Schedule, Gallery, GalleryFiles, Slider, SchoolDocumentsFiles, SchoolDocuments


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


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'image_tag')
    search_fields = ('title',)
    list_filter = ['title']

    class Meta:
        model = Slider


class SchoolDocumentsFilesAdmin(admin.TabularInline):
    model = SchoolDocumentsFiles
    extra = 1


@admin.register(SchoolDocuments)
class SchoolDocumentsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ['title', 'created_at']
    inlines = [SchoolDocumentsFilesAdmin]

    class Meta:
        model = SchoolDocuments
