from django.db import models
from django.utils.translation import gettext as _


class MainAboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Мектеп жөнүндө маалыматтын темасы"))
    description = models.TextField(verbose_name=_("Мектеп жөнүндө маалымат"))

    class Meta:
        db_table = 'about_us'
        verbose_name = _('Башкы баракча маалыматы')
        verbose_name_plural = _('Башкы баракча маалыматтары')

    def __str__(self):
        return self.title


class AboutUsFiles(models.Model):
    about_us = models.ForeignKey(MainAboutUs, on_delete=models.CASCADE, related_name="about_us_files")
    title = models.CharField(max_length=255, verbose_name=_("Файл жөнүндө маалымат"))
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Файл жүктөө"), null=True)

    class Meta:
        db_table = 'files'
        verbose_name = _("Файл")
        verbose_name_plural = _("Файлдар")


class Teachers(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Аты-жөнү"))
    position = models.CharField(max_length=50, verbose_name=_("Позициясы"))
    lesson = models.CharField(max_length=50, verbose_name=_("Сабак"))
    timetable = models.TextField(verbose_name=_("График"))
    progress = models.TextField(verbose_name=_("Жетишкендиктери"))
    contacts = models.CharField(verbose_name=_("Байланышуу"), max_length=255)
    avatar = models.ImageField(upload_to="avatars")

    class Meta:
        db_table = 'teachers'
        verbose_name = _("Мугалим")
        verbose_name_plural = _("Мугалимдер")
