from django import template

from social_link.models import SocialLink
register = template.Library()


@register.inclusion_tag('social_link/social_link_list.html')
def draw_social_links():
    return {'social_links': SocialLink.objects.all()}