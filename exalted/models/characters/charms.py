import random

from django.db import models
from django.urls import reverse

from core.models import Model
from core.utils import add_dot, weighted_choice
from exalted.models.characters.utils import ABILITIES


# Create your models here.
class Charm(Model):
    type = "charm"

    statistic = models.CharField(
        max_length=20,
        choices=zip(ABILITIES, [x.replace("_", " ").title() for x in ABILITIES]),
    )
    min_statistic = models.IntegerField(default=0)
    min_essence = models.IntegerField(default=0)
    mote_cost = models.IntegerField(default=0)
    initiative_cost = models.IntegerField(default=0)
    anima_cost = models.IntegerField(default=0)
    willpower_cost = models.IntegerField(default=0)
    silverxp_cost = models.IntegerField(default=0)
    goldxp_cost = models.IntegerField(default=0)
    whitexp_cost = models.IntegerField(default=0)
    xp_cost = models.IntegerField(default=0)
    lhl_cost = models.IntegerField(default=0)
    hl_cost = models.IntegerField(default=0)

    charm_type = models.CharField(max_length=20, default="")
    duration = models.CharField(max_length=20, default="")

    keywords = models.JSONField(default=list)
    prerequisites = models.ManyToManyField("self", blank=True, symmetrical=False)

    def get_absolute_url(self):
        return reverse("exalted:characters:solars:solarcharm", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse(
            "exalted:characters:solars:update_solarcharm", kwargs={"pk": self.pk}
        )

    def keyword_display(self):
        return ", ".join(self.keywords)

    def get_cost(self):
        costs = [
            (self.mote_cost, "motes"),
            (self.initiative_cost, "initiative"),
            (self.anima_cost, "anima"),
            (self.willpower_cost, "willpower"),
            (self.silverxp_cost, "silver xp"),
            (self.goldxp_cost, "gold xp"),
            (self.whitexp_cost, "white xp"),
            (self.xp_cost, "xp"),
            (self.lhl_cost, "lethal health levels"),
            (self.hl_cost, "health levels"),
        ]
        costs = [x for x in costs if x[0] != 0]
        costs = [f"{x[0]} {x[1]}" for x in costs]
        return ", ".join(costs)

    def check_essence(self, character):
        return getattr(character, "essence") >= self.min_essence

    def check_prerequisites(self, character):
        statistic = getattr(character, self.statistic) >= self.min_statistic
        essence = self.check_essence(character)
        prereq_charms = True
        for prereq_charm in self.prerequisites.all():
            if character.charms.filter(pk=prereq_charm.id).exists():
                prereq_charms = prereq_charms and True
            else:
                prereq_charms = False
        return statistic and essence and prereq_charms


class SolarCharm(Charm):
    type = "solar_charm"

    def check_essence(self, character):
        if self.statistic == character.supernal_ability:
            essence = 5 >= self.min_essence
        else:
            essence = getattr(character, "essence") >= self.min_essence
        return essence


class MartialArtsStyle(Model):
    type = "martial_arts_style"

    weapons = models.TextField(default="")
    armor = models.TextField(default="")


class MartialArtsCharm(Charm):
    type = "martial_arts_charm"

    style = models.ForeignKey(
        MartialArtsStyle, null=True, blank=True, on_delete=models.CASCADE
    )

    def check_essence(self, character):
        if hasattr(character, "supernal_ability"):
            if self.statistic == character.supernal_ability:
                essence = 5 >= self.min_essence
            else:
                essence = getattr(character, "essence") >= self.min_essence
        else:
            essence = getattr(character, "essence") >= self.min_essence
        return essence

    def check_prerequisites(self, character):
        return (
            super().check_prerequisites(character)
            and character.merits.filter(name="Martial Artist").exists()
        )


class DragonBloodedCharm(Charm):
    type = "dragon_blooded_charm"
