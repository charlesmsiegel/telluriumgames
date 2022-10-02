from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import ItemModel


# Create your models here.
class Item(ItemModel):
    type = "item"
    durability = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    structure = models.IntegerField(default=0)
    availability = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def get_absolute_url(self):
        return reverse("cod:items:item", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("cod:items:mortal:update_item", kwargs={"pk": self.pk})


class Equipment(Item):
    type = "equipment"
    fragile_condition = models.BooleanField(default=True)
    volatile_condition = models.BooleanField(default=True)
    die_bonus = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"

    def get_update_url(self):
        return reverse("cod:items:mortal:update_equipment", kwargs={"pk": self.pk})
