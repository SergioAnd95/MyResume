from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from ckeditor.fields import RichTextField

# Create your models here.


class ResumeBlock(models.Model):
    """
    Model to display resume block
    """

    title = models.CharField(_('Название'), max_length=100)
    text = RichTextField(_('Текст'), null=True)
    is_display = models.BooleanField(_('Отображать?'), default=True)
    update_date = models.DateTimeField(_('Дата обновления'), auto_now=True)
    display_order = models.IntegerField(_('Порядок отображения'), default=0)

    class Meta:
        verbose_name = _('Раздел резюме')
        verbose_name_plural = _('Разделы резюме')
        ordering = ['display_order',]

    def __str__(self):
        return self.title


class ChronologicalData(models.Model):
    """
    Model for chronological data in resume block
    """

    title = models.CharField(_('Название'), max_length=100)
    from_date = models.DateField(_('Дата начала'))
    to_date = models.DateField(_('Дата окончания'))
    text = RichTextField(_('Текст'))

    resume_block = models.ForeignKey(ResumeBlock, related_name='chrono_data', verbose_name=_('Раздел резюме'))

    class Meta:
        verbose_name = _('Хронологические данные')
        verbose_name_plural = verbose_name

        ordering = ['from_date', 'to_date']

    def __str__(self):
        return '%s' % (self.title)


class SkillsData(models.Model):
    """
    Model for skills datat in resume block
    """

    title = models.CharField(_('Название'), max_length=100)
    value = models.IntegerField(_('Значение'), validators=[MinValueValidator(0), MaxValueValidator(100)])

    resume_block = models.ForeignKey(ResumeBlock, related_name='skills_data', verbose_name=_('Раздел резюме'))

    class Meta:
        verbose_name = _('Размерные данные')
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % (self.title)