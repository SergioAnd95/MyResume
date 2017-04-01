from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration

from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(SiteConfiguration)
class SiteConfigurationMode(TranslationAdmin, SingletonModelAdmin):
    pass