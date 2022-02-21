from django.contrib import admin
from .models import MainAboutUs


@admin.register(MainAboutUs)
class MainAboutUsAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'description')

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True
