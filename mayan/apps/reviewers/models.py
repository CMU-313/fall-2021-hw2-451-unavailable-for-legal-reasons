from django.db import models
from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mptt.models import MPTTModel
from mayan.apps.documents.models.document_file_models import DocumentFile

class Dashboard(ExtraDataModelMixin, MPTTModel):
    pass


class Reviewers(ExtraDataModelMixin, MPTTModel):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    DOB = models.DateField()
    position = models.CharField(max_length=50)
    employment_time = models.CharField(max_length=50)
    assigned_candidates = models.CharField(max_length=50)
    dashboard = models.ForeignKey(Dashboard,on_delete=models.CASCADE)



# Create your models here.


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
        assigned_candidates = models.ManyToManyField('candidates.ModelCandidate_django')