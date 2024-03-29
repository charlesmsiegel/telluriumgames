from django.db import models
from django.urls import reverse

from core.models import Model


# Create your models here.
class Instrument(Model):
    type = "instrumnet"

    class Meta:
        verbose_name = "Instrument"
        verbose_name_plural = "Instruments"

    def get_absolute_url(self):
        return reverse("wod:characters:mage:instrument", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:mage:update_instrument", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"


class Practice(Model):
    type = "practice"

    abilities = models.JSONField(default=list)
    instruments = models.ManyToManyField(Instrument, blank=True)

    class Meta:
        verbose_name = "Practice"
        verbose_name_plural = "Practices"

    def get_absolute_url(self):
        return reverse("wod:characters:mage:practice", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:mage:update_practice", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"


class Paradigm(Model):
    type = "paradigm"

    practices = models.ManyToManyField(Practice, blank=True)

    class Meta:
        verbose_name = "Paradigm"
        verbose_name_plural = "Paradigms"

    def get_absolute_url(self):
        return reverse("wod:characters:mage:paradigm", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:mage:update_paradigm", kwargs={"pk": self.pk})

    def get_heading(self):
        return "mtas_heading"
