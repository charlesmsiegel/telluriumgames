from django.db import models
from django.urls import reverse

from core.models import Model
from wod.models.characters.human import Character


class SpiritCharm(Model):
    type = "spirit_charm"

    class Meta:
        verbose_name = "Spirit Charm"
        verbose_name_plural = "Spirit Charms"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:charm", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_charm", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"


class SpiritCharacter(Character):
    type = "spirit_character"

    willpower = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)
    gnosis = models.IntegerField(default=0)
    essence = models.IntegerField(default=0)

    charms = models.ManyToManyField(SpiritCharm, blank=True)

    class Meta:
        verbose_name = "Spirit"
        verbose_name_plural = "Spirits"

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_spirit", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"


class Totem(Model):
    type = "totem"

    TYPES = [
        ("respect", "Respect"),
        ("war", "War"),
        ("wisdom", "Wisdom"),
        ("cunning", "Cunning"),
    ]

    cost = models.IntegerField(default=0)
    totem_type = models.CharField(max_length=20, choices=TYPES)
    individual_traits = models.TextField(default="")
    pack_traits = models.TextField(default="")
    ban = models.TextField(default="")

    class Meta:
        verbose_name = "Totem"
        verbose_name_plural = "Totems"

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:totem", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:werewolf:update_totem", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wta_heading"
