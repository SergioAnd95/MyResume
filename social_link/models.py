from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class SocialLink(models.Model):
    """
    Model to represent social link
    """

    GITHUB = 'github'
    BITBUCKET = 'bitbucket'
    VKONTAKTE = 'vk'
    FACEBOOK = 'facebook'
    LINKEDIN = 'linkedin'
    TWITTER = 'tw'
    EMAIL = 'envelope-o'

    SOCIAL_NETWORK_CHOICES = (
        (GITHUB, 'Github'),
        (BITBUCKET, 'Bitbucket'),
        (VKONTAKTE, 'Vkontakte'),
        (FACEBOOK, 'Facebook'),
        (LINKEDIN, 'Linkedin'),
        (TWITTER, 'Twitter'),
        (EMAIL, 'Email')
    )

    social_network = models.CharField(_('Социальная сеть'), max_length=20, choices=SOCIAL_NETWORK_CHOICES)
    url = models.CharField(verbose_name='URL', max_length=50)

    class Meta:
        verbose_name = _('Социальные ссылка')
        verbose_name_plural = _('Социальные ссылки')
