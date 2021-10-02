from django.shortcuts import render
from mayan.apps.views.generics import SingleObjectListView
from django.http import HttpResponse

from .models import ModelCandidate_django, ModelCandidateManager_django

from django.http import HttpResponse

from mayan.apps.views.generics import (
    MultipleObjectFormActionView, SingleObjectCreateView,
    SingleObjectDeleteView, SingleObjectEditView, SingleObjectListView
)

class CandidatesView(SingleObjectListView):
    pass

def table(request):
    basic_info = {
        "name":"foof",
        "email":"foof@troof.oof",
        "phone_number":"6786786789",
        "DOB":"none",
        "undergrad_experience":"none"
    }
    # heh = ModelCandidate_django.objects.create_candidate(basic_information=basic_info)
    # heh.save()

    # Getting all the stuff from database
    # query_results = ModelCandidate_django.objects.all()

    # Creating a dictionary to pass as an argument
    # context = { 'query_results' : query_results }

    return render(request, "candidates/candidate_table.html")