from django.db import models
from polymorphic.models import PolymorphicModel

from wod.models.characters.human import Character


# Create your models here.
class Location(PolymorphicModel):
    type = "location"

    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        "Location",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="children",
    )


class City(Location):
    type = "city"

    population = models.IntegerField(default=0)
    characters = models.ManyToManyField(Character, blank=True)

    def add_character(self, character):
        self.characters.add(character)
        self.save()
