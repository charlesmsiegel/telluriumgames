from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import LocationModel
from wod.models.characters.human import Character


# Create your models here.
class ExLocation(LocationModel):
    type = "location"

    def get_absolute_url(self):
        return reverse("exalted:locations:location", args=[str(self.id)])

    def get_update_url(self):
        return reverse("exalted:locations:mortals:update_location", args=[str(self.id)])

    def get_heading(self):
        return "exalted_heading"
