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
