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


class Human(Character):
    type = "human"
