from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import ResumeBlock, ChronologicalData, SkillsData
# Register your models here.


class ChronologicalDataInline(TranslationStackedInline):
    model = ChronologicalData
    fields = ['title', 'from_date', 'to_date', 'text']
    extra = 1


class SkillsDataInline(TranslationStackedInline):
    model = SkillsData
    extra = 3


@admin.register(ResumeBlock)
class ResumeBlockAdmin(TranslationAdmin):
    inlines = [ChronologicalDataInline, SkillsDataInline, ]
    list_display = ['title', 'is_display']
    list_filter = ['is_display',]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }