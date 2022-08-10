import random
from ast import Num

from django.db import models

from core.utils import add_dot, weighted_choice


# Create your models here.
class Numina(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="")


class Ephemera(models.Model):
    RANK_TO_TRAIT_MAX = {
        1: 5,
        2: 7,
        3: 9,
        4: 12,
        5: 15,
    }

    TYPE_CHOICES = [
        ("spirit", "Spirit"),
        ("goetia", "Goetia"),
        ("ghost", "Ghost"),
        ("supernal being", "Supernal Being"),
    ]

    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=0)
    type = models.CharField(max_length=100, default="spirit", choices=TYPE_CHOICES)

    maximum_essence = models.IntegerField(default=0)

    power = models.IntegerField(default=1)
    finesse = models.IntegerField(default=1)
    resistance = models.IntegerField(default=1)

    corpus = models.IntegerField(default=0)
    willpower = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    numina = models.ManyToManyField(Numina, blank=True)

    def has_rank(self):
        return self.rank != 0

    def set_rank(self, rank):
        self.rank = rank
        return True

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        return self.set_rank(rank)

    def has_type(self):
        return self.type != ""

    def set_type(self, type):
        self.type = type
        return True

    def random_type(self, type=None):
        if type is None:
            type = random.choice(self.TYPE_CHOICES)[-1]
        return self.set_type(type)

    def compute_maximum_essence(self):
        rank_to_essence = {
            1: 10,
            2: 15,
            3: 20,
            4: 25,
            5: 50,
        }
        self.maximum_essence = rank_to_essence[self.rank]

    def get_attributes(self):
        return {
            "power": self.power,
            "finesse": self.finesse,
            "resistance": self.resistance,
        }

    def total_attributes(self):
        return sum(v for v in self.get_attributes().values())

    def random_attributes(self):
        RANK_TO_DOTS = {
            1: list(range(5, 8 + 1)),
            2: list(range(9, 14 + 1)),
            3: list(range(15, 25 + 1)),
            4: list(range(26, 35 + 1)),
            5: list(range(36, 45 + 1)),
        }

        total_dots = random.choice(RANK_TO_DOTS[self.rank])
        while self.total_attributes() < total_dots:
            choice = weighted_choice(self.get_attributes())
            add_dot(self, choice, self.RANK_TO_TRAIT_MAX[self.rank])
        return True

    def other_traits(self):
        self.compute_maximum_essence()
        self.corpus = self.resistance + self.size
        self.willpower = self.resistance + self.finesse
        self.initiative = self.finesse + self.resistance
        self.defense = min(self.power, self.finesse)
        self.speed = self.power + self.finesse
        self.size = 5

    def add_numina(self, numina):
        self.numina.add(numina)
        return True

    def filter_numina(self):
        return Numina.objects.exclude(pk__in=self.numina.all())

    def total_numina(self):
        return self.numina.count()

    def random_numina(self):
        total_numina = self.rank * 2 + random.choice([-1, 0, 1])
        while self.total_numina() < total_numina:
            options = self.filter_numina()
            choice = random.choice(options)
            self.add_numina(choice)

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True

    def random_name(self, name=None):
        if name is None:
            name = f"Ephemeral {Ephemera.objects.count()}"
        return self.set_name(name)

    def random(self, rank=None, name=None):
        self.random_name(name=name)
        self.random_rank(rank=rank)
        self.random_type()
        self.random_attributes()
        self.random_numina()
        self.other_traits()
