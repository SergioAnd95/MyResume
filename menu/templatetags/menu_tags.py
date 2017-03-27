from django import template

from menu.models import MenuItem
register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu():
    return {'menu': MenuItem.objects.all()}