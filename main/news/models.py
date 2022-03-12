from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Жаңылыктын темасы"))
    description = models.TextField(verbose_name=_("Жаңылыктын маалыматы"))
    created_at = models.DateField(verbose_name=_('Жазылган дата'), editable=False, default=timezone.now)

    class Meta:
        db_table = 'news'
        verbose_name = _('Жаңылык')
        verbose_name_plural = _('Жаңылыктар')

    def __str__(self):
        return self.title


class NewsFiles(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_("Жаңылыктар үчүн файл жүктөө"),
                                null=True)
    title = models.CharField(max_length=255, verbose_name=_("Файл жөнүндө маалымат"))
    file = models.FileField(upload_to='files/%Y/%m', verbose_name=_("Файл жүктөө"), null=True)

    class Meta:
        verbose_name = _('Файл')
        verbose_name_plural = _('Файлдар')
        db_table = 'news_files'


class Notification(models.Model):
    SELECT_FOR_WHOM = [
        ('M', 'Мугалим'), ('O', 'Окуучу'), ('P', 'Ата-эне')
    ]
    TEACHER = 'Мугалим'
    STUDENT = 'Окуучу'
    PARENT = 'Ата-эне'
    title = models.CharField(max_length=255, verbose_name=_("Файл жөнүндө маалымат"))
    description = models.TextField(verbose_name=_("Жаңылыктын маалыматы"))
    created_at = models.DateField(verbose_name=_('Жазылган дата'), editable=False, default=timezone.now)
    author = models.CharField(verbose_name=_("Автор"), max_length=255)
    human = models.CharField(choices=SELECT_FOR_WHOM, default=STUDENT, max_length=50, verbose_name=_("Ким үчүн"))

    class Meta:
        verbose_name = _('Кулактандыруу')
        verbose_name_plural = _('Кулактандыруулар')
        db_table = 'notifications'
