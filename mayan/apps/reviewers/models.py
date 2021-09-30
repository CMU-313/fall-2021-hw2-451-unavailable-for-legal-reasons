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

class ModelCandidate_django(models.Model): 
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50)
    DOB = models.CharField(max_length = 50)

    # assigned_candidates = models.ManyToManyField(ModelReviewer_django) Only one of the model candidates/reviewers needs this, but putting it here implicitly.
    associated_docs = models.ManyToManyField(DocumentFile)
    skills = models.CharField(max_length = 150)
    experience = models.CharField(max_length = 1000)

    undergrad_experience = models.CharField(max_length=1000, blank=True)
    undergrad_school = models.CharField(max_length=50, blank=True)
    GPA = models.CharField(max_length=5, blank=True)
    reviewer_notes =  models.CharField(max_length=10000, blank=True)

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
