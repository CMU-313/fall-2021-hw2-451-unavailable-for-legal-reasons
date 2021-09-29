from django.shortcuts import render
from mayan.apps.views.generics import SingleObjectListView
from django.http import HttpResponse

from .models import Reviewers

from django.http import HttpResponse

from mayan.apps.views.generics import (
    MultipleObjectFormActionView, SingleObjectCreateView,
    SingleObjectDeleteView, SingleObjectEditView, SingleObjectListView
)

# Create your views here.
class ReviewersView(SingleObjectListView):
    pass

def table(request):
    return render(request, "reviewers/reviewer_table.html")
