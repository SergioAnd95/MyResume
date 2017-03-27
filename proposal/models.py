from django.db import models

# Create your models here.


class Proposal(models.Model):

    when_created = models.DateTimeField('Дата создания', auto_now_add=True, editable=False)
    email = models.EmailField('E-mail')
    name = models.CharField('ФИО', max_length=100)
    company_name = models.CharField('Компания', max_length=30)
    text = models.TextField('Сообщение')

    def __str__(self):
        return '%s %s' % (self.name, self.company_name)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'