import random

from django.db import models
from django.db.models import F, Q
from django.urls import reverse

from core.models import Model
from core.utils import add_dot, weighted_choice
from exalted.models.characters.charms import MartialArtsCharm, SolarCharm
from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.utils import ABILITIES


# Create your models here.
class Solar(ExMortal):
    type = "solar"

    CASTE_CHOICES = ["dawn", "zenith", "twilight", "eclipse", "night"]

    caste_ability_dict = {
        "dawn": [
            "archery",
            "awareness",
            "brawl",
            "martial_arts",
            "dodge",
            "melee",
            "resistance",
            "thrown",
            "war",
        ],
        "zenith": [
            "athletics",
            "integrity",
            "performance",
            "lore",
            "presence",
            "resistance",
            "survival",
            "war",
        ],
        "twilight": [
            "bureaucracy",
            "craft",
            "integrity",
            "investigation",
            "linguistics",
            "lore",
            "medicine",
            "occult",
        ],
        "eclipse": [
            "bureaucracy",
            "larceny",
            "linguistics",
            "occult",
            "presence",
            "ride",
            "sail",
            "socialize",
        ],
        "night": [
            "athletics",
            "awareness",
            "dodge",
            "investigation",
            "larceny",
            "ride",
            "stealth",
            "socialize",
        ],
    }

    caste = models.CharField(
        max_length=15, choices=zip(CASTE_CHOICES, [x.title() for x in CASTE_CHOICES])
    )

    caste_abilities = models.JSONField(default=list)
    favored_abilities = models.JSONField(default=list)
    supernal_ability = models.CharField(
        max_length=20,
        choices=zip(ABILITIES, [x.replace("_", " ").title() for x in ABILITIES]),
    )

    charms = models.ManyToManyField(SolarCharm, blank=True)
    martial_arts_charms = models.ManyToManyField(MartialArtsCharm, blank=True)

    limit_trigger = models.CharField(
        max_length=100,
        default="",
        choices=[
            ("all_consuming_grief", "All-Consuming Grief"),
            ("berserk_anger", "Berserk Anger"),
            ("chains_of_honor", "Chains of Honor"),
            ("compassionate_martyrdom", "Compassionate Martyrdom"),
            ("contempt_of_the_virtuous", "Contempt of the Virtuous"),
            ("crushing_doubt", "Crushing Doubt"),
            ("deliberate_cruelty", "Deliberate Cruelty"),
            ("heart_of_flint", "Heart of Flint"),
            ("rampaging_avarice", "Rampaging Avarice"),
        ],
    )

    def get_update_url(self):
        return reverse("exalted:characters:solars:update_solar", kwargs={"pk": self.pk})

    def has_caste(self):
        return self.caste != ""

    def set_caste(self, caste):
        self.caste = caste
        return True

    def set_caste_abilities(self, caste_abilities):
        self.caste_abilities = caste_abilities
        self.save()
        return True

    def add_caste_abilites(self, ability):
        if ability not in self.caste_abilities:
            tmp = self.caste_abilities + [ability]
            return self.set_caste_abilities(tmp)
        return False

    def has_caste_abilities(self):
        return len(self.caste_abilities) == 5

    def random_caste_abilities(self):
        if self.caste not in self.caste_ability_dict.keys():
            return False
        options = self.caste_ability_dict[self.caste]
        while not self.has_caste_abilities():
            op = random.choice(options)
            self.add_caste_abilites(op)
            options = [x for x in options if x != op]
        return True

    def random_name(self):
        return self.set_name(f"Solar {Solar.objects.count()}")

    def random_caste(self):
        return self.set_caste(random.choice(self.CASTE_CHOICES))

    def has_favored_abilities(self):
        return len(self.favored_abilities) == 5

    def add_favored_ability(self, ability):
        if ability in self.caste_abilities + self.favored_abilities:
            return False
        self.favored_abilities.append(ability)
        add_dot(self, ability, maximum=1)
        return True

    def random_favored_ability(self):
        options = [x for x in ABILITIES if x not in self.caste_abilities]
        options = [x for x in options if x not in self.favored_abilities]
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

    def has_finishing_touches(self):
        return self.willpower == 5 and self.health_levels == 7 and self.essence == 1

    def total_charms(self):
        return self.charms.count() + self.martial_arts_charms.count()

    def has_charms(self):
        return self.total_charms() == 15

    def filter_charms(self):
        q = Q()
        for ability in ABILITIES:
            if ability == self.supernal_ability:
                essence = 5
            else:
                essence = self.essence
            q |= Q(
                statistic=ability,
                min_statistic__lte=getattr(self, ability),
                min_essence__lte=essence,
            )

        filtered_charms = SolarCharm.objects.filter(q)
        filtered_charms = filtered_charms.exclude(pk__in=self.charms.all())

        ma_charms = MartialArtsCharm.objects.filter(
            statistic="martial_arts",
            min_statistic__lte=getattr(self, "martial_arts"),
            min_essence__lte=self.essence,
        )
        full_list = list(filtered_charms) + list(ma_charms)
        return [x for x in full_list if x.check_prerequisites(self)]

    def add_charm(self, charm):
        if charm is not None:
            if charm.check_prerequisites(self):
                if charm.type == "solar_charm":
                    self.charms.add(charm)
                    return True
                if charm.type == "martial_arts_charm":
                    self.martial_arts_charms.add(charm)
                    return True
            return False
        return False

    def random_charm(self):
        c = random.choice(self.filter_charms())
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
        if trait_type in ["caste ability", "favored ability"]:
            return 1
        if trait_type in ["caste charm", "favored charm"]:
            return 4
        if trait_type == "charm":
            return 5
        if trait_type == "spell":
            if "occult" in self.favored_abilities + self.caste_abilities:
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
        d.update(
            {"charm": self.random_bonus_charm,}
        )
        return d

    def random_bonus_charm(self):
        filtered_list = self.filter_charms()
        d = {k.name: max(k.min_essence, k.min_statistic) for k in filtered_list}
        trait = weighted_choice(d)
        return self.spend_bonus_points(trait)

    def spend_bonus_points(self, trait):
        if trait in self.favored_abilities:
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
            if charm.statistic in self.favored_abilities:
                cost = self.bonus_cost("favored charm")
                if cost <= self.bonus_points:
                    if self.add_charm(charm):
                        self.bonus_points -= cost
                        return True
                    return False
                return False
            if charm.statistic in self.caste_abilities:
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
        if (
            trait_type == "spell"
            and "occult" in self.favored_abilities + self.caste_abilities
        ):
            return 8
        if trait_type == "spell":
            return 10
        if (
            trait_type == "martial arts charm"
            and "brawl" in self.favored_abilities + self.caste_abilities
        ):
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
        d.update(
            {"charm": self.random_xp_charm,}
        )
        return d

    def random_xp_charm(self):
        filtered_list = self.filter_charms()
        d = {k.name: max(k.min_essence, k.min_statistic) for k in filtered_list}
        trait = weighted_choice(d)
        return self.spend_xp(trait)

    def spend_xp(self, trait):
        if trait in self.favored_abilities:
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
            if charm.ability in self.favored_abilities:
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

    def apply_finishing_touches(self):
        self.willpower = 5
        self.health_levels = 7
        self.essence = 1
        self.save()
        return True

    def charm_dict(self):
        charms = {}
        available_charms = self.filter_charms()
        for ability in ABILITIES:
            charms[ability.replace("_", " ").title()] = [
                x for x in available_charms if x.statistic == ability
            ]
        charms = {k: v for k, v in charms.items() if len(v) != 0}
        return charms

    def random(self, bonus_points=15, xp=0):
        self.update_status("Ran")
        self.bonus_points = bonus_points
        self.xp = xp
        self.essence = 1
        self.random_name()
        self.random_concept()
        self.random_caste()
        self.random_caste_abilities()
        self.random_supernal_ability()
        self.random_favored_abilities()
        self.random_attributes(primary=8, secondary=6, tertiary=4)
        self.random_abilities()
        self.random_charms()
        self.random_specialties()
        self.random_merits(num_dots=10)
        self.random_intimacies()
        self.random_limit_trigger()
        self.random_spend_bonus_points()
        self.random_spend_xp()
        self.apply_finishing_touches()
