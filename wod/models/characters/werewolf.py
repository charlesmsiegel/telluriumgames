import random

from django.db import models

from core.utils import add_dot
from wod.models.characters.human import Human


class Totem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Tribe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    willpower = models.IntegerField(default=3)

    def __str__(self):
        return self.name


class Camp(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gift(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=0)
    allowed = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class Rite(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Werewolf(Human):
    type = "garou"

    rank = models.IntegerField(default=1)
    auspice = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("ragabash", "Ragabash"),
            ("theurge", "Theurge"),
            ("philodox", "Philodox"),
            ("galliard", "Galliard"),
            ("ahroun", "Ahroun"),
        ],
    )
    breed = models.CharField(
        default="",
        max_length=100,
        choices=[("homid", "Homid"), ("metis", "Metis"), ("lupus", "Lupus"),],
    )
    tribe = models.ForeignKey(Tribe, blank=True, null=True, on_delete=models.CASCADE)
    camp = models.ForeignKey(Camp, blank=True, null=True, on_delete=models.CASCADE)

    rites = models.IntegerField(default=0)

    gnosis = models.IntegerField(default=0)
    rage = models.IntegerField(default=0)

    glory = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    honor = models.IntegerField(default=0)

    gifts = models.ManyToManyField(Gift, blank=True)
    rites_known = models.ManyToManyField(Rite, blank=True)

    first_change = models.TextField(default="")
    battle_scars = models.TextField(default="")
    age_of_first_change = models.IntegerField(default=0)

    def has_breed(self):
        return self.breed is not None

    def set_breed(self, breed):
        self.breed = breed
        return True

    def random_breed(self):
        return self.set_breed(random.choice(["homid", "metis", "lupus"]))

    def has_auspice(self):
        return self.auspice is not None

    def set_auspice(self, auspice):
        self.auspice = auspice
        return True

    def random_auspice(self):
        return self.set_auspice(
            random.choice(["ragabash", "theurge", "philodox", "galliard", "ahroun"])
        )

    def has_tribe(self):
        return self.tribe is not None

    def set_tribe(self, tribe):
        self.tribe = tribe
        return True

    def random_tribe(self):
        return self.set_tribe(Tribe.objects.order_by("?").first())

    def has_camp(self):
        return self.camp is not None

    def set_camp(self, camp):
        self.camp = camp
        return True

    def random_camp(self):
        return self.set_tribe(
            Camp.objects.filter(tribe=self.tribe).order_by("?").first()
        )

    def add_gift(self, gift):
        pass

    def filter_gifts(self):
        return []

    def has_gifts(self):
        pass

    def random_gift(self):
        pass

    def random_gifts(self):
        pass

    def add_rite(self, rite):
        pass

    def filter_rites(self):
        return []

    def has_rites(self):
        return self.rites == self.total_rites()

    def total_rites(self):
        return (
            sum([x.level for x in self.rites_known.all()])
            + self.rites_known.filter(level=0).count() // 2
        )

    def random_rites(self):
        pass

    def set_glory(self, glory):
        self.glory = glory
        return True

    def set_honor(self, honor):
        self.honor = honor
        return True

    def set_wisdom(self, wisdom):
        self.wisdom = wisdom
        return True

    def has_renown(self):
        pass

    def add_gnosis(self):
        return add_dot(self, "gnosis", 10)

    def add_rage(self):
        return add_dot(self, "rage", 10)

    def set_rank(self, rank):
        self.rank = rank
        return True

    def increase_rank(self):
        pass

    def has_werewolf_history(self):
        return (
            (self.first_change != "")
            and (self.battle_scars != "")
            and (self.age_of_first_change != 0)
        )


# Create your models here.
# # Talents
# Leadership
# Primal Urge

# # Skills
# Animal Ken
# Larceny
# Performance
# Survival

# # Knowledges
# Enigmas
# Law
# Occult
# Rituals
# Technology

# # Backgrounds
# Allies
# Ancestors
# Fate
# Fetish
# Kinfolk
# Pure Breed
# Resources
# Rites
# Spirit Heritage
# Totem


class Pack(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Werewolf, blank=True)

    def random(self, num_chars, new_characters=False):
        pass

    def set_totem(self, totem):
        pass

    def has_totem(self):
        pass

    def random_totem(self):
        pass

    def total_totem(self):
        pass
