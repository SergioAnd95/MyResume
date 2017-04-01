from django.db import models
from django.utils.translation import ugettext_lazy as _

from solo.models import SingletonModel
from ckeditor.fields import RichTextField
# Create your models here.


class SiteConfiguration(SingletonModel):
    avatar = models.ImageField(_('Аватар'), upload_to='avatar')
    hello_text = RichTextField(_('Приветственный текст'))

    class Meta:
        verbose_name = _('Настройки сайта')
