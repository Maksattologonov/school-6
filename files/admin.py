from django.contrib import admin

from files.models import Schedule, ScheduleFiles, Gallery, GalleryFiles, Accreditation


class ScheduleFileAdmin(admin.TabularInline):
    model = ScheduleFiles
    extra = 1


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('class_no', 'file_count')
    search_fields = ['class_no']
    list_filter = ['class_no']
    inlines = [ScheduleFileAdmin]

    class Meta:
        model = Schedule

    def file_count(self, obj):
        return ScheduleFiles.objects.filter(schedule_id__class_no=obj).count()
    file_count.short_description = "Файлдардын саны"


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


@admin.register(Accreditation)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
    search_fields = ('title',)
