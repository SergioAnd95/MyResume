from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count

from .models import ResumeBlock, SkillsData
# Create your views here.

# TODO: Create View to display Resume blocks (ListView)


class ResumeBlockListView(ListView):
    template_name = 'index.html'
    model = ResumeBlock
    context_object_name = 'resume_blocks'

    def get_queryset(self):
        p = SkillsData.objects.values('title')
        a = [print(i['title']) for i in p ]
        print(a)
        print(p.query)
        print(p)
        return ResumeBlock.objects.all()