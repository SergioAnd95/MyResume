from django.contrib import admin

from .models import ResumeBlock, ChronologicalData, SkillsData
# Register your models here.


class ChronologicalDataInline(admin.StackedInline):
    model = ChronologicalData
    fields = ['title', 'from_date', 'to_date', 'text']
    extra = 1


class SkillsDataInline(admin.StackedInline):
    model = SkillsData
    extra = 3


@admin.register(ResumeBlock)
class ResumeBlockAdmin(admin.ModelAdmin):
    inlines = [ChronologicalDataInline, SkillsDataInline, ]
    list_display = ['title', 'is_display']
    list_filter = ['is_display',]

