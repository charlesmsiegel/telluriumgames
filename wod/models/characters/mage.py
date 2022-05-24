from django.db import models

from core.models import Language, Material, Medium
from wod.models.characters.human import Human


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
    founded = models.IntegerField(default=-5000)


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


class Mage(Human):
    type = "mage"

    def get_abilities(self):
        return {
            "alertness": 0,
            "awareness": 0,
            "art": 0,
            "athletics": 0,
            "brawl": 0,
            "empathy": 0,
            "intimidation": 0,
            "leadership": 0,
            "expression": 0,
            "streetwise": 0,
            "subterfuge": 0,
            "animal_kinship": 0,
            "blatancy": 0,
            "carousing": 0,
            "do": 0,
            "flying": 0,
            "high_ritual": 0,
            "lucid_dreaming": 0,
            "search": 0,
            "seduction": 0,
            "crafts": 0,
            "drive": 0,
            "etiquette": 0,
            "firearms": 0,
            "martial_arts": 0,
            "meditation": 0,
            "melee": 0,
            "research": 0,
            "stealth": 0,
            "survival": 0,
            "technology": 0,
            "acrobatics": 0,
            "archery": 0,
            "biotech": 0,
            "energy_weapons": 0,
            "hypertech": 0,
            "jetpack": 0,
            "riding": 0,
            "torture": 0,
            "academics": 0,
            "computer": 0,
            "cosmology": 0,
            "enigmas": 0,
            "esoterica": 0,
            "investigation": 0,
            "law": 0,
            "medicine": 0,
            "occult": 0,
            "politics": 0,
            "science": 0,
            "area_knowledge": 0,
            "belief_systems": 0,
            "cryptography": 0,
            "demolitions": 0,
            "finance": 0,
            "lore": 0,
            "media": 0,
            "pharmacopeia": 0,
        }

    def get_spheres(self):
        return {
            "correspondence": 0,
            "time": 0,
            "spirit": 0,
            "mind": 0,
            "entropy": 0,
            "prime": 0,
            "forces": 0,
            "matter": 0,
            "life": 0,
        }
