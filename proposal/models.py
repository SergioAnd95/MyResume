from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Proposal(models.Model):

    when_created = models.DateTimeField(_('Дата создания'), auto_now_add=True, editable=False)
    email = models.EmailField(_('E-mail'))
    name = models.CharField(_('ФИО'), max_length=100)
    company_name = models.CharField(_('Компания'), max_length=30)
    text = models.TextField(_('Сообщение'))

    def __str__(self):
        return '%s %s' % (self.name, self.company_name)

    class Meta:
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')