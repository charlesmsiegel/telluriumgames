from django.db import models
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile


# Create your models here.
class Character(PolymorphicModel):
    type = "character"

    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    concept = models.CharField(max_length=100)

    def has_concept(self):
        pass

    def set_concept(self, concept):
        pass

    def has_name(self):
        pass

    def set_name(self, name):
        pass

    def add_attribute(self, attribute):
        pass

    def total_physical_attributes(self):
        return 0

    def total_social_attributes(self):
        return 0

    def total_mental_attributes(self):
        return 0

    def filter_attributes(self, minimum=0, maximum=5):
        return []

    def total_talents(self):
        return 0

    def total_skills(self):
        return 0

    def total_knowledges(self):
        return 0


class Human(Character):
    type = "human"
