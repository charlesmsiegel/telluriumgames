from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel
from core.models import Model


# Create your models here.
class Item(Model):
    type = "item"
    durability = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    structure = models.IntegerField(default=0)
    availability = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("cod:items:item", kwargs={"pk": self.pk})


class Equipment(Item):
    type = "equipment"
    fragile_condition = models.BooleanField(default=True)
    volatile_condition = models.BooleanField(default=True)
    die_bonus = models.IntegerField(default=0)
