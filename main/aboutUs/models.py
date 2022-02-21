from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class MainAboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Мектеп жөнүндө маалыматтын темасы"))
    image = models.ImageField(verbose_name=_("Сүрөт жүктөө"), upload_to='images/%Y/%m')
    description = models.TextField(verbose_name=_("Мектеп жөнүндө маалымат"))

    class Meta:
        db_table = 'about_us'
        verbose_name = _('Башкы баракча маалыматы')
        verbose_name_plural = _('Башкы баракча маалыматтары')

    def __str__(self):
        return self.title
