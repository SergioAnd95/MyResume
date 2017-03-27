from django.contrib import admin

from .models import Proposal
# Register your models here.


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'when_created')

admin.site.register(Proposal, ProposalAdmin)