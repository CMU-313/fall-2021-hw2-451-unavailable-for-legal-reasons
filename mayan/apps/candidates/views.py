from django.shortcuts import render
from mayan.apps.views.generics import SingleObjectListView
from django.http import HttpResponse

from .models import Candidate

from django.http import HttpResponse

from mayan.apps.views.generics import (
    MultipleObjectFormActionView, SingleObjectCreateView,
    SingleObjectDeleteView, SingleObjectEditView, SingleObjectListView
)

class CandidatesView(SingleObjectListView):
    pass

def table(request):
    return render(request, "candidates/candidate_table.html")