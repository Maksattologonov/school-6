from django.db import models
from django.utils.translation import gettext_lazy as _


class Schedule(models.Model):
    class_no = models.CharField(max_length=255, verbose_name=_("Класстын расписаниеси"))

    class Meta:
        db_table = 'schedule'
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписание')

    def __str__(self):
        return self.class_no


class ScheduleFiles(models.Model):
    schedule_id = models.ForeignKey(Schedule, models.SET_NULL, related_name="schedule_files", blank=True, null=True,)
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Файл жүктөө"), null=True)

    class Meta:
        db_table = 'schedule_files'


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


class Accreditation(models.Model):
    types = [
    ('1', 'Программалык'),
    ('2', 'Институтционалдык')]
    title = models.CharField(max_length=255, verbose_name=_("Аккредитация документтери"))
    file_type = models.CharField(choices=types, verbose_name=_("Документтин түрү"), max_length=30)
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Файл жүктөө"), null=True)

    class Meta:
        db_table = 'accreditation'
        verbose_name = _('Аккредитация')
        verbose_name_plural = _('Аккредитация')

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Слайдердин аталышы"))
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Сүрөт жүктөө"), null=True)

    class Meta:
        db_table = 'slider'
        verbose_name = _('Слайдер')
        verbose_name_plural = _('Слайдер')

    def __str__(self):
        return self.title