from modeltranslation.translator import register, TranslationOptions

from .models import ResumeBlock, ChronologicalData, SkillsData

@register(ResumeBlock)
class ResumeBlockTranslationOptions(TranslationOptions):
    """
    Translation settings class for model ResumeBlock
    """

    fields = ('title', 'text',)


@register(ChronologicalData)
class ChronologicalDataTranslationOptions(TranslationOptions):
    """
    Translation settings class for model ChronologicalData
    """

    fields = ('title', 'text',)


@register(SkillsData)
class SkillsDataTranslationOptions(TranslationOptions):
    """
    Translation settings class for model SkillsData
    """

    fields = ('title',)
