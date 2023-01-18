import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Forum(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Заголовок"))
    text = models.TextField(verbose_name=_('Текст'))
    images = models.ForeignKey()
    created_date = models.DateField(default=datetime.datetime.now(), verbose_name=_('Дата создания'))
    updated_date = models.DateField(default=datetime.datetime.now(), verbose_name=_('Дата обновления'))
    status = models.BooleanField(default=True, verbose_name=_('Статус'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'forum'
        verbose_name = _('Жаңылык')
        verbose_name_plural = _('Жаңылыктар')
