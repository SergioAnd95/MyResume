from django.conf.urls import url, include
from . import views


urlpatterns = [
    url('^$', views.ResumeBlockListView.as_view(), name='resume'),
]