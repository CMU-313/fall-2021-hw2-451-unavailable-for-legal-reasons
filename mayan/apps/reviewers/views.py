from django.shortcuts import render
from mayan.apps.views.generics import SingleObjectListView
from django.http import HttpResponse

from .models import Reviewers

# Create your views here.
class ReviewersView(SingleObjectListView):
    pass

def table(request):
    return render(request, "reviewers/reviewer_table.html")