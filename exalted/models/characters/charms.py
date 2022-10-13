import random

from django.db import models
from django.urls import reverse

from core.models import Model, ModelWithPrereqs
from core.utils import add_dot, weighted_choice
from exalted.models.characters.utils import ABILITIES


# Create your models here.
class Charm(ModelWithPrereqs):
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
    ahl_cost = models.IntegerField(default=0)
    lhl_cost = models.IntegerField(default=0)
    hl_cost = models.IntegerField(default=0)

    charm_type = models.CharField(max_length=20, default="")
    duration = models.CharField(max_length=20, default="")

    keywords = models.JSONField(default=list)

    class Meta:
        verbose_name = "Charm"
        verbose_name_plural = "Charms"

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
        if hasattr(character, "supernal_ability"):
            if self.statistic == character.supernal_ability:
                return 5 >= self.min_essence
        return getattr(character, "essence") >= self.min_essence

    def check_ability(self, character):
        if self.statistic == "martial_arts":
            return (
                getattr(character, self.statistic) >= self.min_statistic
            ) and character.merits.filter(name="Martial Artist").count() > 0
        return getattr(character, self.statistic) >= self.min_statistic

    def prereq_satisfied(self, prereq, character):
        if character.charms.filter(name=prereq[0]).count() >= 1:
            return True
        return False

    def check_prereqs(self, character):
        if len(self.prereqs) == 0:
            return self.check_essence(character) and self.check_ability(character)
        for prereq_set in self.prereqs:
            prereq_set = [self.prereq_satisfied(x, character) for x in prereq_set]
            if all(prereq_set):
                return self.check_essence(character) and self.check_ability(character)
        return False

    def prereq_display(self):
        tmp_prereqs = [x for x in self.prereqs]
        for i, prereq_set in enumerate(tmp_prereqs):
            for j, prereq in enumerate(prereq_set):
                if Charm.objects.filter(name=prereq[0]).count() != 0:
                    c = Charm.objects.get(name=prereq[0])
                    prereq_set[j] = f'<a href="{c.get_absolute_url()}">{c.name}</a>'
            tmp_prereqs[i] = prereq_set
        tmp_prereqs = [", ".join(x) for x in tmp_prereqs]
        return " or ".join(tmp_prereqs)


class SolarCharm(Charm):
    type = "solar_charm"

    class Meta:
        verbose_name = "Solar Charm"
        verbose_name_plural = "Solar Charms"


class MartialArtsStyle(Model):
    type = "martial_arts_style"

    weapons = models.TextField(default="")
    armor = models.TextField(default="")

    class Meta:
        verbose_name = "Martial Arts Style"
        verbose_name_plural = "Martial Arts Styles"


class MartialArtsCharm(Charm):
    type = "martial_arts_charm"

    style = models.ForeignKey(
        MartialArtsStyle, null=True, blank=True, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Martial Arts Charm"
        verbose_name_plural = "Martial Arts Charms"


class DragonBloodedCharm(Charm):
    type = "dragon_blooded_charm"

    class Meta:
        verbose_name = "Dragon Blooded Charm"
        verbose_name_plural = "Dragon Blooded Charm"
