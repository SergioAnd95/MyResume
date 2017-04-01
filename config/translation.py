from modeltranslation.translator import register, TranslationOptions

from .models import SiteConfiguration


@register(SiteConfiguration)
class SiteConfigurationTranslationOptions(TranslationOptions):
    """
    Translation settings class for model ResumeBlock
    """
    fields = ('hello_text', 'proposal_succes_msg')