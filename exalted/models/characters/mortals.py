from django.db import models
from django.urls import reverse
from accounts.models import ExaltedProfile
from polymorphic.models import PolymorphicModel

# Create your models here.
class Mortal(PolymorphicModel):
    type = "mortal"
    
    bonus_points = 21
    num_merits = 7
    
    name = models.CharField(max_length=100, unique=True)
    concept = models.CharField(max_length=100)
    player = models.ForeignKey(
        ExaltedProfile, on_delete=models.CASCADE, related_name="characters"
    )
    
    archery = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    awareness = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    bureaucracy = models.IntegerField(default=0)
    craft = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)
    integrity = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    linguistics = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)
    ride = models.IntegerField(default=0)
    sail = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    thrown = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    
    specialties = models.ManyToManyField("Specialty", blank=True)
    intimacies = models.ManyToManyField("Intimacy", blank=True)
    merits = models.ManyToManyField("Merit", blank=True)
    
    def get_absolute_url(self):
        return reverse("exalted:character", args=[str(self.id)])
    
    def has_name(self):
        return self.name != ""
    
    def set_name(self, name):
        self.name = name
        return True
    
    def random_name(self):
        pass
    
    def has_concept(self):
        return self.concept != ""
    
    def set_concept(self, concept):
        self.concept = concept
        return True
    
    def random_concept(self):
        pass
    
    def has_attributes(self):
        pass
    
    def add_attribute(self, attribute):
        pass
    
    def get_attributes(self):
        return {}
    
    def total_attributes(self):
        return sum(k for k in self.get_attributes())
 
    def filter_attributes(self, minimum=0, maximum=5):
        return []
    
    def get_mental_attributes(self):
        return {}
    
    def total_mental_attributes(self):
        return sum(k for k in self.get_mental_attributes())
    
    def get_physical_attributes(self):
        return {}
    
    def total_physical_attributes(self):
        return sum(k for k in self.get_physical_attributes())
    
    def get_social_attributes(self):
        return {}
    
    def total_social_attributes(self):
        return sum(k for k in self.get_social_attributes())
    
    def random_attribute(self):
        pass
    
    def random_attributes(self):
        pass
    
    def add_ability(self, ability):
        pass
    
    def get_abilities(self):
        return {
        "archery": self.archery,
        "athletics": self.athletics,
        "awareness": self.awareness,
        "brawl": self.brawl,
        "bureaucracy": self.bureaucracy,
        "craft": self.craft,
        "dodge": self.dodge,
        "integrity": self.integrity,
        "investigation": self.investigation,
        "larceny": self.larceny,
        "linguistics": self.linguistics,
        "lore": self.lore,
        "martial_arts": self.martial_arts,
        "medicine": self.medicine,
        "melee": self.melee,
        "occult": self.occult,
        "performance": self.performance,
        "presence": self.presence,
        "resistance": self.resistance,
        "ride": self.ride,
        "sail": self.sail,
        "socialize": self.socialize,
        "stealth": self.stealth,
        "survival": self.survival,
        "thrown": self.thrown,
        "war": self.war,
        }
    
    def has_abilities(self):
        pass
    
    def total_abilities(self):
        return sum(v for k, v in self.get_abilities().items())
    
    def filter_abilities(self, minimum=0, maximum=5):
        return []
    
    def random_ability(self):
        pass
    
    def random_abilities(self):
        pass
    
    def has_specialties(self):
        pass
    
    def filter_specialties(self):
        return []
    
    def add_specialty(self, specialty):
        if self.get_abilities()[specialty.ability] > 0 and specialty not in self.specialties.all():
            self.specialties.add(specialty)
            self.save()
            return True
        return False
    
    def random_specialty(self):
        pass
    
    def random_specialties(self):
        pass
    
    def has_intimacies(self):
        pass
    
    def add_intimacy(self, intimacy):
        self.intimacies.add(intimacy)
        return True
    
    def random_intimacy(self):
        pass
    
    def random_intimacies(self):
        pass
    
    def has_merits(self):
        pass
    
    def add_merit(self, merit):
        pass
    
    def filter_merits(self, dots=1000):
        return []
    
    def random_merit(self):
        pass
    
    def random_merits(self):
        pass
     
    def has_finishing_touches(self):
        pass
    
    def apply_finishing_touches(self):
        pass
    
    def bonus_cost(self, trait_type):
        pass
    
    def spend_bonus_points(self, trait):
        pass
    
    def random_spend_bonus_points(self):
        pass
    
    def xp_cost(self, trait_type):
        pass
    
    def spend_xp(self, trait):
        pass
    
    def random_spend_xp(self):
        pass
    
    def random(self, xp=0):
        pass

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ability = models.CharField(max_length=20)

class Intimacy(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=[
        ("tie", "Tie"),
        ("principle", "Principle"),
    ])
    strength = models.CharField(max_length=20, choices=[
        ("minor", "Minor"),
        ("major", "Major"),
        ("defining", "Defining"),
    ])
    is_negative = models.BooleanField(default=False)

class Merit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=20, choices=[
        ("innate", "Innate"),
        ("purchased", "Purchased"),
        ("story", "Story"),
    ])
    ratings = models.JSONField(default=list)
