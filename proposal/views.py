from django.shortcuts import render
from django.views.generic import CreateView

from main.utils.mixins import AjaxFormMixin

from .forms import ProposalForm

# Create your views here.


class ProposalCreateView(AjaxFormMixin, CreateView):
    """
    View to display form and ajax validate and proccesing data
    """
    form_class = ProposalForm
    context_object_name = 'proposal_form'
    template_name = 'proposal/proposal.html'
    success_url = '/proposal/'

    def form_valid(self, form):
        form.save()
        return super(ProposalCreateView, self).form_valid(form)