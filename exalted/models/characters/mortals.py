from django.db import models
from django.urls import reverse
from accounts.models import ExaltedProfile
from polymorphic.models import PolymorphicModel
from core.utils import add_dot, weighted_choice

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
    
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)
    
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
        return self.set_concept(f"Mortal {Mortal.objects.count()}")
    
    def has_concept(self):
        return self.concept != ""
    
    def set_concept(self, concept):
        self.concept = concept
        return True
    
    def random_concept(self):
        return self.set_concept("Random")
    
    def has_attributes(self, primary=6, secondary=4, tertiary=3):
        triple = [primary + 3, secondary + 3, tertiary + 3]
        other_triple = [self.total_physical_attributes(), self.total_mental_attributes(), self.total_social_attributes()]
        triple.sort()
        other_triple.sort()
        return triple == other_triple
    
    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum=maximum)
    
    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_social_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_physical_attributes())
        return tmp
    
    def total_attributes(self):
        return sum(v for k, v in self.get_attributes().items())
 
    def filter_attributes(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum}
    
    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits,
        }
    
    def total_mental_attributes(self):
        return sum(v for k, v in self.get_mental_attributes().items())
    
    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina
        }
    
    def total_physical_attributes(self):
        return sum(v for k, v in self.get_physical_attributes().items())
    
    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }
    
    def total_social_attributes(self):
        return sum(v for k, v in self.get_social_attributes().items())
    
    def random_attribute(self):
        d = self.get_attributes()
        choice = weighted_choice(d)
        return self.add_attribute(choice)
    
    def random_attributes(self):
        pass
    
    def add_ability(self, ability, maximum=5):
        return add_dot(self, ability, maximum=maximum)
    
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
        return {k: v for k, v in self.get_abilities().items() if minimum <= v <= maximum}
    
    def random_ability(self):
        d = self.get_abilities()
        choice = weighted_choice(d)
        return self.add_ability(choice)
    
    def random_abilities(self):
        pass
    
    def has_specialties(self):
        return self.specialties.count() == 4
    
    def filter_specialties(self):
        possible_abilities = self.filter_abilities(minimum=1)
        return Specialty.objects.filter(ability__in=possible_abilities).exclude(pk__in=self.specialties.all())
    
    def add_specialty(self, specialty):
        if self.get_abilities()[specialty.ability] > 0 and specialty not in self.specialties.all():
            self.specialties.add(specialty)
            self.save()
            return True
        return False
    
    def random_specialty(self, ability=None):
        specialties = self.filter_specialties()
        if ability is not None:
            specialties = specialties.filter(ability=ability)
        return self.add_specialty(specialties.order_by("?").first())
    
    def random_specialties(self):
        while self.specialties.count() < 4:
            self.random_specialty()
    
    def has_intimacies(self):
        has_four = self.intimacies.count() >= 4
        one_defining = self.intimacies.filter(strength="defining").exists()
        one_major = self.intimacies.filter(strength="major").exists()
        one_negative = self.intimacies.filter(is_negative=True).exists()
        return has_four and one_defining and one_major and one_negative
    
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
