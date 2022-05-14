import random
from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import CoDProfile
from core.utils import add_dot


# Create your models here.
class Mortal(PolymorphicModel):
    type = "mortal"
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        CoDProfile, on_delete=models.CASCADE, related_name="characters"
    )

    concept = models.CharField(max_length=300)

    virtue = models.CharField(max_length=100)
    vice = models.CharField(max_length=100)

    merits = models.ManyToManyField("Merit", through="MeritRating")

    specialties = models.ManyToManyField("Specialty", blank=True)

    def add_name(self, name):
        self.name = name
        
    def has_name(self):
        pass

    def add_concept(self, concept):
        self.concept = concept

    def has_concept(self):
        return self.concept != ""

    def has_virtue(self):
        return self.virtue != ""

    def filter_virtues(self, virtue_list=None):
        pass

    def random_virtue(self):
        virtues = ["Competitive", "Generous", "Just", "Loyal"]
        self.add_virtue(random.choice(virtues))

    def add_virtue(self, virtue):
        if virtue not in self.virtue.split(", "):
            virtues = self.virtue.split(", ")
            virtues.append(virtue)
            virtues = [x for x in virtues if x]
            self.virtue = ", ".join(virtues)
            return True
        return False

    def has_vice(self):
        return self.vice != ""

    def filter_vices(self, vice_list=None):
        pass

    def random_vice(self):
        vices = ["Competitive", "Generous", "Just", "Loyal"]
        self.add_vice(random.choice(vices))

    def add_vice(self, vice):
        if vice not in self.vice.split(", "):
            vices = self.vice.split(", ")
            vices.append(vice)
            vices = [x for x in vices if x]
            self.vice = ", ".join(vices)
            return True
        return False

    def add_attribute(self, attribute):
        add_dot(self, attribute, 5)

    def get_physical_attributes(self):
        pass

    def get_mental_attributes(self):
        pass
    
    def get_social_attributes(self):
        pass

    def total_attributes(self):
        pass

    def has_attributes(self):
        pass

    def filter_attributes(self, max=5):
        pass

    def random_attribute(self):
        pass

    def random_attributes(self):
        pass

    def get_physical_skills(self):
        pass

    def get_mental_skills(self):
        pass
    
    def get_social_skills(self):
        pass

    def has_skills(self):
        pass

    def total_skills(self):
        pass

    def filter_skills(self, min=0, max=5):
        pass

    def random_skill(self):
        pass

    def random_skills(self):
        pass

    def has_specialties(self):
        pass

    def add_specialty(self, specialty):
        pass

    def random_specialties(self):
        pass

    def random_specialty(self):
        pass

    def add_merit(self):
        pass

    def total_merits(self):
        pass

    def has_merits(self):
        pass

    def filter_merits(self, dots=None):
        pass

    def random_merit(self):
        pass

    def random_merits(self):
        pass


class Merit(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(default=list)


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)


class MeritRating(models.Model):
    character = models.ForeignKey(
        "Mortal", null=False, blank=False, on_delete=models.CASCADE
    )
    merit = models.ForeignKey(
        "Merit", null=False, blank=False, on_delete=models.CASCADE
    )
