import random

from django.db import models
from django.urls import reverse

from .wtahuman import WtAHuman


class FomoriPower(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("wod:characters:werewolf:fomoripower", kwargs={"pk": self.pk})


class Fomor(WtAHuman):
    type = "fomor"
    rage = models.IntegerField(default=0)
    gnosis = models.IntegerField(default=0)
    powers = models.ManyToManyField(FomoriPower, blank=True)

    background_points = 3

    # def __init__(self, *args, **kwargs):
    #     kwargs["willpower"] = kwargs.get("willpower") or 3
    #     super().__init__(*args, **kwargs)

    def get_backgrounds(self):
        return {
            "allies": self.allies,
            "contacts": self.contacts,
            "resources": self.resources,
        }

    def add_power(self, power):
        self.powers.add(power)
        return True

    def filter_powers(self):
        return FomoriPower.objects.exclude(pk__in=self.powers.all())

    def random_power(self):
        options = self.filter_powers()
        return self.add_power(random.choice(options))

    def random_powers(self, num_powers=2):
        while self.powers.count() < num_powers:
            self.random_power()
        choice = (
            FomoriPower.objects.filter(
                name__in=["Armored Skin", "Berserker", "Gifted Fomor"]
            )
            .exclude(pk__in=self.powers.all())
            .order_by("?")
            .first()
        )
        self.add_power(choice)
        self.add_power(FomoriPower.objects.get(name="Immunity to the Delirium"))

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.willpower = 3
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_attributes(primary=6, secondary=4, tertiary=3)
        self.random_abilities(primary=11, secondary=7, tertiary=3)
        self.random_backgrounds()
        self.random_powers(num_powers=random.randint(1, 3))
        self.random_history()
        self.random_finishing_touches()
        self.random_freebies()
        self.mf_based_corrections()
        self.random_xp()
        self.random_specialties()
        self.save()
