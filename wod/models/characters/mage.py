from django.db import models

from core.models import Language, Material, Medium


# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Practice(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abilities = models.JSONField(default=list)
    instruments = models.ManyToManyField(Instrument, blank=True)


class Paradigm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    practices = models.ManyToManyField(Practice, blank=True)


class MageFaction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, blank=True)
    affinities = models.JSONField(default=list)
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    media = models.ManyToManyField(Medium, blank=True)


class Rote(models.Model):
    name = models.CharField(max_length=100, unique=True)
    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)


class Resonance(models.Model):
    name = models.CharField(max_length=100, unique=True)
    correspondence = models.BooleanField(default=False)
    time = models.BooleanField(default=False)
    spirit = models.BooleanField(default=False)
    matter = models.BooleanField(default=False)
    life = models.BooleanField(default=False)
    forces = models.BooleanField(default=False)
    entropy = models.BooleanField(default=False)
    mind = models.BooleanField(default=False)
    prime = models.BooleanField(default=False)
    data = models.BooleanField(default=False)
    dimensional_science = models.BooleanField(default=False)
    primal_utility = models.BooleanField(default=False)
