from django.db import models
from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mptt.models import MPTTModel

class Dashboard(ExtraDataModelMixin, MPTTModel):
    pass

class Candidate(ExtraDataModelMixin, MPTTModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    DOB = models.DateField()
    dashboard = models.ForeignKey(Dashboard,on_delete=models.CASCADE)

class Reviewers(ExtraDataModelMixin, MPTTModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    DOB = models.DateField()
    dashboard = models.ForeignKey(Dashboard,on_delete=models.CASCADE)
# Create your models here.

class ModelReviewer: 
    def __init__(self, **reviewer_input): 
        try:
            self.name = reviewer_input["name"] 
        except: 
            raise Exception("Reviewer name is required.")
        self.position = reviewer_input.get("position", "graduate_student")
        self.employment_time = reviewer_input.get("employment_time", "undecided")
        self.assigned_candidates = reviewer_input.get("assigned_candidates", [])

class ModelReviewer_django(models.Model): 
        name = models.CharField(max_length = 50)
        POSITIONS = (
            ('JN', 'Junior'),
            ('SN', 'Senior'),
        )
        position = models.CharField(max_length=2, choices=POSITIONS)
        EMPLOYMENT_TIME = (
            ('PT', 'Part time'),
            ('FT', 'Full time'),
        )
        employment_time = models.CharField(max_length=2, choices=EMPLOYMENT_TIME)
        assigned_candidates = models.ManyToManyField('apps.candidates.CandidateModel_django')
        # ISSUE: ModelReviewer and ModelCandidate classes depend on eachother,
        # and need to reference eachother lazily. However, b/c of nested directories,
        # the function that resolves names can't handle more than one "."
        # and gets overloaded, therefore it can't resolve the path to the model : (

        # get
        # ValueError: Invalid model reference 'apps.re
        #  app_1 | app_label, model_name = model.split(".")
        #  app_1 | ValueError: too many values to unpack (expected 2)
