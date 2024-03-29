from django.db import models
from django.urls import reverse

from core.models import Language, Material, Medium, Model

from .focus import Paradigm, Practice


# Create your models here.
class MageFaction(Model):
    type = "mage_faction"

    languages = models.ManyToManyField(Language, blank=True)
    affinities = models.JSONField(default=list)
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    media = models.ManyToManyField(Medium, blank=True)
    materials = models.ManyToManyField(Material, blank=True)
    founded = models.IntegerField(default=-5000)
    ended = models.IntegerField(default=5000)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Mage Faction"
        verbose_name_plural = "Mage Factions"

    def get_absolute_url(self):
        return reverse("wod:characters:mage:magefaction", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:mage:update_magefaction", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"

    def get_all_paradigms(self):
        factions = [self]
        while factions[-1].parent is not None:
            factions.append(factions[-1].parent)
        paradigms = Paradigm.objects.none()
        for faction in factions:
            paradigms |= faction.paradigms.all()
        return paradigms.distinct()

    def get_all_practices(self):
        factions = [self]
        while factions[-1].parent is not None:
            factions.append(factions[-1].parent)
        practices = Practice.objects.none()
        for faction in factions:
            practices |= faction.practices.all()
        return Practice.objects.filter(pk__in=practices.distinct())
