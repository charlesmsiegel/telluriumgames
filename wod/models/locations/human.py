from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import LocationModel
from wod.models.characters.human import Character


# Create your models here.
class Location(LocationModel):
    type = "location"

    gauntlet = models.IntegerField(default=7)
    shroud = models.IntegerField(default=7)
    dimension_barrier = models.IntegerField(default=6)
    reality_zone = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def get_absolute_url(self):
        return reverse("wod:locations:location", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:locations:human:update_location", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"


class City(Location):
    type = "city"

    population = models.IntegerField(default=0)
    characters = models.ManyToManyField(Character, blank=True)
    mood = models.TextField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    media = models.TextField(blank=True, null=True)
    politicians = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def add_character(self, character):
        self.characters.add(character)
        self.save()

    def get_update_url(self):
        return reverse("wod:locations:human:update_city", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"
