from django.db import models
from django.core.validators import RegexValidator, URLValidator
# Create your models here.


class MenuItem(models.Model):
    name = models.CharField('Название', max_length=30)
    href = models.CharField('Ссылка', max_length=100)

    def __str__(self):
        return self.name
