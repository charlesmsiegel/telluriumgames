from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile
from core.utils import add_dot, weighted_choice


# Create your models here.
class Archetype(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Character(PolymorphicModel):
    type = "character"

    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    concept = models.CharField(max_length=100)

    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True


class Human(Character):
    type = "human"

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    def has_archetypes(self):
        pass

    def set_archetypes(self, nature, demeanor):
        pass

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina
        }

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance
        }

    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def filter_attributes(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum}

    def total_talents(self):
        return 0

    def total_skills(self):
        return 0

    def total_knowledges(self):
        return 0
