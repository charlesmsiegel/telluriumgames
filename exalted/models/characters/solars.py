import random
from django.db import models
from django.db.models import F
from core.models import Model
from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.utils import ABILITIES

# Create your models here.
class Charm(Model):
    type = "charm"

    ability = models.CharField(
        max_length=20,
        choices=zip(ABILITIES, [x.replace("_", " ").title() for x in ABILITIES]),
    )
    min_ability = models.IntegerField(default=0)
    min_essence = models.IntegerField(default=0)


class Solar(ExMortal):
    type = "solar"

    caste_abilities = models.JSONField(default=list)
    favored_abilites = models.JSONField(default=list)

    charms = models.ManyToManyField(Charm, blank=True)

    def has_caste(self):
        return self.caste != ""

    def set_caste(self, caste):
        self.caste = caste
        if caste == "dawn":
            self.caste_abilities = [
                "archery",
                "awareness",
                "brawl",
                "martial arts",
                "dodge",
                "melee",
                "resistance",
                "thrown",
                "war",
            ]
        elif caste == "zenith":
            self.caste_abilities = [
                "athletics",
                "integrity",
                "performance",
                "lore",
                "presence",
                "resistance",
                "survival",
                "war",
            ]
        elif caste == "twilight":
            self.caste_abilities = [
                "bureaucracy",
                "craft",
                "integrity",
                "investigation",
                "linguistics",
                "lore",
                "medicine",
                "occult",
            ]
        elif caste == "night":
            self.caste_abilities = [
                "athletics",
                "awareness",
                "dodge",
                "investigation",
                "larceny",
                "ride",
                "stealth",
                "socialize",
            ]
        elif caste == "eclipse":
            self.caste_abilities = [
                "bureaucracy",
                "larceny",
                "linguistics",
                "occult",
                "presence",
                "ride",
                "sail",
                "socialize",
            ]
        return True

    def random_caste(self):
        return self.set_caste(random.choice(self.CASTE_CHOICES))

    def has_favored_abilities(self):
        return len(self.favored_abilites) == 5

    def add_favored_ability(self, ability):
        if ability in self.supernal_ability:
            return False
        elif ability in self.favored_abilites:
            return False
        self.favored_abilites.append(ability)
        return True

    def random_favored_ability(self):
        options = [x for x in ABILITIES if x not in self.supernal_ability]
        options = [x for x in options if x not in self.favored_abilites]
        choice = random.choice(options)
        return self.add_favored_ability(choice)
    
    def random_favored_abilities(self):
        while not self.has_favored_abilities():
            self.random_favored_ability()

    def has_supernal_ability(self):
        return self.supernal_ability != ""

    def set_supernal_ability(self, supernal_ability):
        if supernal_ability in self.caste_abilities:
            self.supernal_ability = supernal_ability
            return True
        return False

    def random_supernal_ability(self):
        ability = random.choice(self.caste_abilities)
        return self.set_supernal_ability(ability)

    def has_charms(self):
        return self.charms.count() == 15

    def filter_charms(self):
        filtered_charms = Charm.objects.filter(
            min_essence__lte=self.essence, min_ability__lte=getattr(self, F("ability"))
        )
        filtered_charms = filtered_charms.exclude(pk__in=self.charms.all())
        return filtered_charms

    def add_charm(self, charm):
        if self.essence < charm.min_essence:
            return False
        if getattr(self, charm.ability) < charm.min_ability:
            return False
        if charm not in self.charms.all():
            self.charms.add(charm)
            return True
        return False

    def random_charm(self):
        c = self.filter_charms().order_by("?").first()
        return self.add_charm(c)

    def random_charms(self):
        while not self.has_charms():
            self.random_charm()

    def has_limit_trigger(self):
        return self.limit_trigger != ""

    def set_limit_trigger(self, limit_trigger):
        self.limit_trigger = limit_trigger
        return True

    def random_limit_trigger(self):
        return self.set_limit_trigger("Random Limit Trigger")

    def bonus_cost(self, trait_type):
        c = super().bonus_cost(trait_type)
        if c != 10000:
            return c
        if trait_type in ['caste ability', 'favored ability']:
            return 1
        if trait_type in ['caste charm', 'favored charm']:
            return 4
        if trait_type == 'charm':
            return 5
        if trait_type == "spell":
            if "occult" in self.favored_abilites + self.caste_abilities:
                return 4
            return 5
        if trait_type == "evocation":
            return 4
        return 10000
