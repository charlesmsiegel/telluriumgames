from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import Model


# Create your models here.
class WoDItem(Model):
    type = "item"

    def get_absolute_url(self):
        return reverse("wod:items:item", args=[str(self.id)])

    def random_name(self, name=None):
        if self.has_name():
            return False
        if name is None:
            name = f"Random Item {WoDItem.objects.count()}"
        return self.set_name(name)


class Weapon(WoDItem):
    type = "weapon"

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


class MeleeWeapon(Weapon):
    type = "melee_weapon"


class ThrownWeapon(Weapon):
    type = "thrown_weapon"


class RangedWeapon(Weapon):
    type = "ranged_weapon"

    range = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    clip = models.IntegerField(default=0)
