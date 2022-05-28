from django.contrib import admin
from django.contrib.admin import display

from .models import MainAboutUs, AboutUsFiles, Teachers, GloryBoard, SchoolAdmissionFiles, SchoolAdmission


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
    list_display = ('name', 'lesson', 'position', 'contacts', 'image_tag')
    search_fields = ('name', 'lesson', 'position')


@admin.register(GloryBoard)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_no', 'glory_whom')
    search_fields = ('name', 'class_no',)


class SchoolAdmissionFilesAdmin(admin.TabularInline):
    model = SchoolAdmissionFiles
    extra = 1


@admin.register(SchoolAdmission)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    inlines = [SchoolAdmissionFilesAdmin]

    class Meta:
        model = SchoolAdmission

    def has_add_permission(self, request):
        if self.model.objects.filter().count() >= 1:
            return False
        else:
            return True
