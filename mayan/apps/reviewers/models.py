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

class ModelCandidate: 
    def __init__(self, **candidate_input): 
        try:
            self.basic_information = candidate_input["basic_information"]
            self.name = self.basic_information["name"]
            self.email = self.basic_information["email"]
            self.phone_number = self.basic_information["phone_number"]
            self.DOB = self.basic_information.get("DOB", "")
        except:
            raise Exception("Candidate name and contact information are required.")

        self.assigned_reviewers = candidate_input.get("assigned_reviewers", [])
        # dictionary mapping title of document to document
        self.associated_docs = candidate_input.get("associated_docs", dict()) 
        self.skills =  candidate_input.get("skills", [])
        # dictionary mapping title of experience to 
        # dictionary w/ keys for employer/organization, time, description
        self.experience = candidate_input.get("experience", dict())

        try: 
            self.undergrad_experience = candidate_input["undergraduate_experience"]
            self.undergrad_school = self.undergrad_experience.get("undergrad_school", "")
            self.GPA = self.undergrad_experience.get("GPA", None)
        except: 
            pass
        
        # dictionary mapping reviewer name to notes
        self.reviewer_notes = dict()
