from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import ItemModel


# Create your models here.
class WoDItem(ItemModel):
    type = "item"
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def get_absolute_url(self):
        return reverse("wod:items:item", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:items:human:update_item", args=[str(self.id)])

    def get_heading(self):
        return "wod_heading"

    def random_name(self, name=None):
        if self.has_name():
            return False
        if name is None:
            name = f"Random Item {WoDItem.objects.count()}"
        return self.set_name(name)


class Weapon(WoDItem):
    type = "weapon"
    
    class Meta:
        verbose_name = "Weapon"
        verbose_name_plural = "Weapons"

    difficulty = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    damage_type = models.CharField(
        max_length=1,
        default="L",
        choices=[("B", "Bashing"), ("L", "Lethal"), ("A", "Aggravated")],
    )
    conceal = models.CharField(
        max_length=1,
        default="P",
        choices=[
            ("P", "Pocket"),
            ("J", "Jacket"),
            ("T", "Trenchcoat"),
            ("N", "Not Applicable"),
        ],
    )

    def get_update_url(self):
        return reverse("wod:items:human:update_weapon", args=[str(self.id)])


class MeleeWeapon(Weapon):
    type = "melee_weapon"

    class Meta:
        verbose_name = "Melee Weapon"
        verbose_name_plural = "Melee Weapons"

    def get_update_url(self):
        return reverse("wod:items:human:update_meleeweapon", args=[str(self.id)])


class ThrownWeapon(Weapon):
    type = "thrown_weapon"

    class Meta:
        verbose_name = "Thrown Weapon"
        verbose_name_plural = "Thrown Weapons"

    def get_update_url(self):
        return reverse("wod:items:human:update_thrownweapon", args=[str(self.id)])


class RangedWeapon(Weapon):
    type = "ranged_weapon"

    range = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    clip = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Ranged Weapon"
        verbose_name_plural = "Ranged Weapons"

    def get_update_url(self):
        return reverse("wod:items:human:update_rangedweapon", args=[str(self.id)])
