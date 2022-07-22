from django.db import models
from django.urls import reverse

from wod.models.characters.human import Character


class Charm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:charm", kwargs={"pk": self.pk})


class SpiritCharacter(Character):
    type = "spirit_character"

    willpower = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)
    gnosis = models.IntegerField(default=0)
    essence = models.IntegerField(default=0)

    charms = models.ManyToManyField(Charm, blank=True)


class Totem(models.Model):
    TYPES = [
        ("respect", "Respect"),
        ("war", "War"),
        ("wisdom", "Wisdom"),
        ("cunning", "Cunning"),
    ]

    name = models.CharField(max_length=100, unique=True)
    cost = models.IntegerField(default=0)
    totem_type = models.CharField(max_length=20, choices=TYPES)
    individual_traits = models.TextField(default="")
    pack_traits = models.TextField(default="")
    ban = models.TextField(default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:totem", kwargs={"pk": self.pk})
