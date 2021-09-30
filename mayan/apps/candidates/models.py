
from django.db import models

class Candidate: 
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

# reference doc: https://docs.djangoproject.com/en/3.2/ref/models/instances/ 
class ModelCandidateManager_django(models.Manager): 
    def create_candidate(self, **candidate_input): 
        basic_information = candidate_input["basic_information"]
        name = self.basic_information["name"]
        email = self.basic_information["email"]
        phone_number = self.basic_information["phone_number"]
        DOB = self.basic_information.get("DOB", "")
        
        assigned_reviewers = candidate_input.get("assigned_reviewers", [])
        # dictionary mapping title of document to document
        associated_docs = candidate_input.get("associated_docs", dict()) 
        skills =  candidate_input.get("skills", [])
        # dictionary mapping title of experience to 
        # dictionary w/ keys for employer/organization, time, description
        experience = candidate_input.get("experience", dict())

        try: 
            undergrad_experience = candidate_input["undergraduate_experience"]
            undergrad_school = self.undergrad_experience.get("undergrad_school", "")
            GPA = self.undergrad_experience.get("GPA", None)
        except: 
            pass
        
        # dictionary mapping reviewer name to notes
        reviewer_notes = dict()
        
        candidate = self.create(name=name, email=email, phone_number=phone_number, 
                                DOB=DOB, assigned_reviewers=assigned_reviewers, 
                                associated_docs=associated_docs, skills=skills, 
                                experience=experience, undergrad_experience=undergrad_experience,
                                undergrad_school=undergrad_school, GPA=GPA, 
                                reviewer_notes=reviewer_notes)
        return candidate
        
class ModelCandidate_django(models.Model): 
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 50)
    DOB = models.CharField(max_length = 50)
    
    assigned_reviewers = models.ManyToManyField('reviewers.ModelReviewer_django')
    associated_docs = models.ManyToManyField('documents.DocumentFile')
    skills = models.CharField(max_length = 150)
    experience = models.CharField(max_length = 1000)
    
    undergrad_experience = models.CharField(max_length=1000, blank=True)
    undergrad_school = models.CharField(max_length=50, blank=True)
    GPA = models.CharField(max_length=5, blank=True)
    reviewer_notes =  models.CharField(max_length=10000, blank=True)
    
    objects = ModelCandidateManager_django()
 
# create new candidate object as
# candidate = ModelCandidate_django.objects.create_candidate(< pass in inputs here>) 
        
