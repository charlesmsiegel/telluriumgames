from django.db import models
from polymorphic.models import PolymorphicModel
from accounts.models import TCProfile

# Create your models here.
class Human(PolymorphicModel):
    type = "human"
    
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        TCProfile, on_delete=models.CASCADE, related_name="characters"
    )

    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)
    
    concept = models.CharField(max_length=100)
    
    paths = models.ManyToManyField("Path", blank=True)
    
    def add_name(self, name):
        self.name = name
        return True

    def has_name(self):
        return self.name != ""

    def add_concept(self, concept):
        self.concept = concept
        return True

    def has_concept(self):
        return self.concept != ""
    
    def has_skills(self):
        pass
    
    def filter_skills(self, minimum=0, maximum=5):
        pass
    
    def add_specialty(self, specialty):
        pass
    
    def filter_specialties(self):
        return []
    
    def add_attribute(self, attribute):
        pass
    
    def has_attributes(self):
        pass
    
    def filter_attributes(self, minimum=0, maximum=5):
        pass
    
    def add_path(self, path):
        pass
    
    def has_paths(self):
        pass

class Path(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=[("origin", "origin"), ("role", "role"), ("society", "society")], blank=True)

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
