from django.db import models
from polymorphic.models import PolymorphicModel

from wod.models.character.human import Character


# Create your models here.
class Location(PolymorphicModel):
    type = "location"

    name = models.CharField(max_length=100, unique=True)


class City(Location):
    type = "city"

    population = models.IntegerField(default=0)
    characters = models.ManyToManyField(Character, blank=True)

    def add_character(self, character):
        pass
