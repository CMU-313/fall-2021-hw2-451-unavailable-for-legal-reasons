from django.conf.urls import url
from django.shortcuts import redirect
from django.views.generic.base import RedirectView

# from .views import table

urlpatterns_reviewers = [
    url(
        r'^reviewers/$', 
        RedirectView.as_view(url='candidates/candidates', permanent=False),
        name='reviewers'
    ),
    
]

urlpatterns = []
urlpatterns.extend(urlpatterns_reviewers)
