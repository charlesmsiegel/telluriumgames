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
    gauntlet = models.IntegerField(default=7)
    shroud = models.IntegerField(default=7)
    dimension_barrier = models.IntegerField(default=6)
    reality_zone = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:location", args=[str(self.id)])


class City(Location):
    type = "city"

    population = models.IntegerField(default=0)
    characters = models.ManyToManyField(Character, blank=True)
    mood = models.TextField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    politicians = models.TextField(blank=True, null=True)

    def add_character(self, character):
        self.characters.add(character)
        self.save()
