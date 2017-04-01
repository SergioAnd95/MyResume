from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count

from .models import ResumeBlock, SkillsData
# Create your views here.


class ResumeBlockListView(ListView):
    template_name = 'index.html'
    model = ResumeBlock
    context_object_name = 'resume_blocks'

    def get_queryset(self):
        qs = super(ResumeBlockListView, self).get_queryset()
        return self.model.objects.displayble()