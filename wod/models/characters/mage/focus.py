from django.db import models

from core.models import Model


# Create your models here.
class Instrument(Model):
    type = "instrumnet"


class Practice(Model):
    type = "practice"

    abilities = models.JSONField(default=list)
    instruments = models.ManyToManyField(Instrument, blank=True)


class Paradigm(Model):
    type = "paradigm"

    practices = models.ManyToManyField(Practice, blank=True)
