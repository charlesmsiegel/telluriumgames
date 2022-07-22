from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel


# Create your models here.
class Item(PolymorphicModel):
    type = "item"
    name = models.CharField(max_length=100, unique=True)
    durability = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    structure = models.IntegerField(default=0)
    availability = models.IntegerField(default=0)
    display = models.BooleanField(default=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cod:items:item", kwargs={"pk": self.pk})


class Equipment(Item):
    type = "equipment"
    fragile_condition = models.BooleanField(default=True)
    volatile_condition = models.BooleanField(default=True)
    die_bonus = models.IntegerField(default=0)
