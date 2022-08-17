import random
from django.db import models
from django.db.models import F, Q
from core.models import Model
from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.utils import ABILITIES
from core.utils import add_dot, weighted_choice

# Create your models here.
class SolarCharm(Model):
    type = "solar_charm"

    ability = models.CharField(
        max_length=20,
        choices=zip(ABILITIES, [x.replace("_", " ").title() for x in ABILITIES]),
    )
    min_ability = models.IntegerField(default=0)
    min_essence = models.IntegerField(default=0)


class Solar(ExMortal):
    type = "solar"
    
    CASTE_CHOICES = [
        "dawn", "zenith", "twilight", "eclipse", "night"
    ]
    
    caste = models.CharField(max_length=15, choices=zip(CASTE_CHOICES, [x.title() for x in CASTE_CHOICES]))

    caste_abilities = models.JSONField(default=list)
    favored_abilites = models.JSONField(default=list)
    supernal_ability = models.CharField(
        max_length=20,
        choices=zip(ABILITIES, [x.replace("_", " ").title() for x in ABILITIES]),
    )

    charms = models.ManyToManyField(SolarCharm, blank=True)
    
    limit_trigger = models.CharField(max_length=100, default="")

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
        add_dot(self, ability, maximum=1)
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
        q = Q()
        for ability in ABILITIES:
            q |= Q(ability=ability, min_ability__lte=getattr(self, ability))
        
        q &= Q(min_essence__lte=self.essence)
        
        filtered_charms = SolarCharm.objects.filter(q)
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
    
    def bonus_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "specialty": 1,
            "merit": 1,
            "willpower": 1,
            "charm": 1,
        }
    
    def random_bonus_functions(self):
        d = super().random_bonus_functions()
        d.update({
            "charm": self.random_bonus_charm,
        })
        return d
    
    def random_bonus_charm(self):
        filtered_list = self.filter_charms()
        d = {k.name: max(k.min_essence, k.min_ability) for k in filtered_list}
        trait = weighted_choice(d)
        return self.spend_bonus_points(trait)
    
    def spend_bonus_points(self, trait):
        if trait in self.favored_abilites:
            cost = self.bonus_cost("favored ability")
            if cost <= self.bonus_points:
                if self.add_ability(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if trait in self.caste_abilities:
            cost = self.bonus_cost("caste ability")
            if cost <= self.bonus_points:
                if self.add_ability(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if SolarCharm.objects.filter(name=trait).exists():
            charm = SolarCharm.objects.get(name=trait)
            if charm.ability in self.favored_abilites:
                cost = self.bonus_cost("favored charm")
                if cost <= self.bonus_points:
                    if self.add_charm(charm):
                        self.bonus_points -= cost
                        return True
                    return False
                return False
            if charm.ability in self.caste_abilities:
                cost = self.bonus_cost("caste charm")
                if cost <= self.bonus_points:
                    if self.add_charm(charm):
                        self.bonus_points -= cost
                        return True
                    return False
                return False
            cost = self.bonus_cost("charm")
            if cost <= self.bonus_points:
                if self.add_charm(charm):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        return super().spend_bonus_points(trait)
    
    def xp_cost(self, trait_type):
        if trait_type == "evocation":
            return 10
        if trait_type == "spell" and "occult" in self.favored_abilites + self.caste_abilities:
            return 8
        if trait_type == "spell":
            return 10
        if trait_type == "martial arts charm" and "brawl" in self.favored_abilites + self.caste_abilities:
            return 8
        if trait_type == "martial arts charm":
            return 10
        if trait_type in ["caste charm", "favored charm"]:
            return 8
        if trait_type == "charm":
            return 10
        return super().xp_cost(trait_type)
    
    def xp_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "specialty": 1,
            "merit": 1,
            "willpower": 1,
            "charm": 1,
        }
    
    def random_xp_functions(self):
        d = super().random_xp_functions()
        d.update({
            "charm": self.random_xp_charm,
        })
        return d
    
    def random_xp_charm(self):
        filtered_list = self.filter_charms()
        d = {k.name: max(k.min_essence, k.min_ability) for k in filtered_list}
        trait = weighted_choice(d)
        return self.spend_xp(trait)
    
    def spend_xp(self, trait):
        if trait in self.favored_abilites:
            current_rating = self.get_abilities()[trait]
            cost = self.xp_cost("ability") * current_rating - 1
            if cost <= self.xp:
                if self.add_ability(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.caste_abilities:
            current_rating = self.get_abilities()[trait]
            cost = self.xp_cost("ability") * current_rating - 1
            if cost <= self.xp:
                if self.add_ability(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if SolarCharm.objects.filter(name=trait).exists():
            charm = SolarCharm.objects.get(name=trait)
            if charm.is_martial_arts:
                cost = self.xp_cost("martial arts charm")
                if cost <= self.xp:
                    if self.add_charm(charm):
                        self.xp -= cost
                        self.add_to_spend(trait, 1, cost)
                        return True
                    return False
                return False
            if charm.ability in self.favored_abilites:
                cost = self.xp_cost("favored charm")
                if cost <= self.xp:
                    if self.add_charm(charm):
                        self.xp -= cost
                        self.add_to_spend(trait, 1, cost)
                        return True
                    return False
                return False
            if charm.ability in self.caste_abilities:
                cost = self.xp_cost("caste charm")
                if cost <= self.xp:
                    if self.add_charm(charm):
                        self.xp -= cost
                        self.add_to_spend(trait, 1, cost)
                        return True
                    return False
                return False
            cost = self.xp_cost("charm")
            if cost <= self.xp:
                if self.add_charm(charm):
                    self.xp -= cost
                    self.add_to_spend(trait, 1, cost)
                    return True
                return False
            return False
        return super().spend_xp(trait)
    
    def random(self, bonus_points=21, xp=0):
        self.bonus_points = bonus_points
        self.xp = xp
        self.random_name()
        self.random_concept()
        self.random_caste()
        self.random_supernal_ability()
        self.random_favored_abilities()
        self.random_attributes()
        self.random_abilities()
        self.random_charms()
        self.random_specialties()
        self.random_merits()
        self.random_intimacies()
        self.random_limit_trigger()
        self.random_spend_bonus_points()
        self.random_spend_xp()
        self.apply_finishing_touches()
