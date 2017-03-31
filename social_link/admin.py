from django.contrib import admin

from .models import SocialLink

# Register your models here.


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('social_network', 'url')

