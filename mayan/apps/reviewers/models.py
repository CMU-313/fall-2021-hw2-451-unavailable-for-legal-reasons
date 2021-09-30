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

# previous python class for reviewer for reference
class Reviewer(): 
    def __init__(self, **reviewer_input): 
        try:
            self.name = reviewer_input["name"]
        except:
            raise Exception("Reviewer name is required.")
        self.position = reviewer_input.get("position", "graduate_student")
        self.employment_time = reviewer_input.get("employment_time", "undecided")
        self.assigned_candidates = reviewer_input.get("assigned_candidates", [])

# reference doc: https://docs.djangoproject.com/en/3.2/ref/models/instances/ 
class ModelReviewerManager_django(models.Manager): 
    def create_reviewer(self, **reviewer_input): 
        try: 
            name = reviewer_input["name"]
        except:
            raise Exception("Reviewer name is required.")
        position = reviewer_input.get("position", "graduate_student")
        employment_time = reviewer_input.get("employment_time", "undecided")
        assigned_candidates = reviewer_input.get("assigned_candidates", [])    

        reviewer = self.create(name=name, position=position, 
                               employment_time=employment_time,
                               assigned_candidates=assigned_candidates) 
        return reviewer

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
        
        objects = ModelReviewerManager_django()
        
# create new reviewer object as
# reviewer = ModelReviewer_django.objects.create_reviewer(< pass in inputs here>) 
