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

    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    crafts = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    weaponry = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

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
        virtues = [x for x in self.virtue.split(", ") if x]
        return [x for x in virtue_list if x not in virtues]

    def random_virtue(self):
        virtues = ["Competitive", "Generous", "Just", "Loyal"]
        virtues = self.filter_virtues(virtues)
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
        vices = [x for x in self.vice.split(", ") if x]
        return [x for x in vice_list if x not in vices]

    def random_vice(self):
        vices = ["Competitive", "Generous", "Just", "Loyal"]
        vices = self.filter_vices(vices)
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

    def get_mental_attributes(self):
        return {
            "intelligence": self.intelligence,
            "wits": self.wits,
            "resolve": self.resolve,
        }

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "presence": self.presence,
            "manipulation": self.manipulation,
            "composure": self.composure,
        }

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

    def get_mental_skills(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "crafts": self.crafts,
            "investigation": self.investigation,
            "medicine": self.medicine,
            "occult": self.occult,
            "politics": self.politics,
            "science": self.science,
        }

    def get_physical_skills(self):
        return {
            "athletics": self.athletics,
            "brawl": self.brawl,
            "drive": self.drive,
            "firearms": self.firearms,
            "larceny": self.larceny,
            "stealth": self.stealth,
            "survival": self.survival,
            "weaponry": self.weaponry,
        }

    def get_social_skills(self):
        return {
            "animal_ken": self.animal_ken,
            "empathy": self.empathy,
            "expression": self.expression,
            "intimidation": self.intimidation,
            "persuasion": self.persuasion,
            "socialize": self.socialize,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
        }

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

    def filter_specialties(self):
        pass

    def add_specialty(self, specialty):
        pass

    def random_specialties(self):
        pass

    def random_specialty(self):
        pass

    def add_merit(self, merit):
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
