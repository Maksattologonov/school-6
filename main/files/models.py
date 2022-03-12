from django.db import models
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


class Schedule(models.Model):
    class_no = models.CharField(max_length=255, verbose_name=_("Класстын расписаниеси"))
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Файл жүктөө"), null=True)

    class Meta:
        db_table = 'schedule'
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписание')

    def __str__(self):
        return self.class_no


class Gallery(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Сүрөттүн тематикасы"))

    class Meta:
        db_table = 'gallery'
        verbose_name = _('Сүрөт')
        verbose_name_plural = _('Галлерея')

    def __str__(self):
        return self.title


class GalleryFiles(models.Model):
    gallery_id = models.ForeignKey(Gallery, models.SET_NULL, related_name="gallery_files", blank=True, null=True,)
    file = models.ImageField(upload_to='files/%Y/%m', verbose_name=_("Сүрөт жүктөө"), null=True)

    class Meta:
        db_table = 'gallery_files'


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Сүрөттүн темасы"))
    sub_title = models.CharField(max_length=255, verbose_name=_("Сүрөттүн подтемасы"))
    file = models.ImageField(upload_to='files/%Y/%m', verbose_name=_("Сүрөт жүктөө"))

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150"" />' % self.file)

    image_tag.short_description = 'Image'

    class Meta:
        db_table = 'slider'
        verbose_name = _("Слайдер үчүн сүрөттөр")
        verbose_name_plural = _("Слайдерлер сүрөттөрү")

    def __str__(self):
        return self.title
