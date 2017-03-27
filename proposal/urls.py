from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('^$', views.ProposalCreateView.as_view(), name='proposal_create'),
]