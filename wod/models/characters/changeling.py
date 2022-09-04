from collections import defaultdict
import random
from django.db import models
from wod.models.characters.human import Human, Group
from core.models import Model
from core.utils import add_dot, weighted_choice


class Kith(Model):
    type = "kith"

    birthrights = models.JSONField(default=list)
    frailty = models.TextField(default="")


class House(Model):
    type = "house"

    court = models.CharField(
        max_length=20,
        choices=[("seelile", "Seelie"), ("unseelie", "Unseelie")],
        blank=True,
        null=True,
    )
    boon = models.TextField(default="")
    flaw = models.TextField(default="")
    factions = models.JSONField(default=list)


class CtDLegacy(Model):
    type = "legacy"

    court = models.CharField(
        max_length=20,
        choices=[("seelile", "Seelie"), ("unseelie", "Unseelie")],
        blank=True,
        null=True,
    )


class CtDHuman(Human):
    type = "ctd_human"

    kenning = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)

    enigmas = models.IntegerField(default=0)
    gremayre = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    chimera = models.IntegerField(default=0)
    dreamers = models.IntegerField(default=0)
    holdings = models.IntegerField(default=0)
    remembrance = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    retinue = models.IntegerField(default=0)
    title = models.IntegerField(default=0)
    treasure = models.IntegerField(default=0)

    def get_talents(self):
        d = super().get_talents()
        d.update(
            {"kenning": self.kenning, "leadership": self.leadership,}
        )
        return d

    def get_skills(self):
        d = super().get_skills()
        d.update(
            {
                "animal_ken": self.animal_ken,
                "larceny": self.larceny,
                "performance": self.performance,
                "survival": self.survival,
            }
        )
        return d

    def get_knowledges(self):
        d = super().get_knowledges()
        d.update(
            {
                "enigmas": self.enigmas,
                "gremayre": self.gremayre,
                "law": self.law,
                "politics": self.politics,
                "technology": self.technology,
            }
        )
        return d

    def get_backgrounds(self):
        d = super().get_backgrounds()
        d.update(
            {
                "chimera": self.chimera,
                "dreamers": self.dreamers,
                "holdings": self.holdings,
                "remembrance": self.remembrance,
                "resources": self.resources,
                "retinue": self.retinue,
                "title": self.title,
                "treasure": self.treasure,
            }
        )
        return d


class Changeling(CtDHuman):
    type = "changeling"

    court = models.CharField(
        default="",
        max_length=20,
        choices=[("seelie", "Seelie"), ("unseelie", "Unseelie")],
    )
    seelie_legacy = models.ForeignKey(
        CtDLegacy,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="seelie_legacy_of",
    )
    unseelie_legacy = models.ForeignKey(
        CtDLegacy,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="unseelie_legacy_of",
    )

    kith = models.ForeignKey(Kith, null=True, blank=True, on_delete=models.CASCADE)
    seeming = models.CharField(
        default="",
        max_length=15,
        choices=[("childling", "Childling"), ("wilder", "Wilder"), ("grump", "Grump")],
    )

    autumn = models.IntegerField(default=0)
    chicanery = models.IntegerField(default=0)
    chronos = models.IntegerField(default=0)
    contract = models.IntegerField(default=0)
    dragons_ire = models.IntegerField(default=0)
    legerdemain = models.IntegerField(default=0)
    metamorphosis = models.IntegerField(default=0)
    naming = models.IntegerField(default=0)
    oneiromancy = models.IntegerField(default=0)
    primal = models.IntegerField(default=0)
    pyretics = models.IntegerField(default=0)
    skycraft = models.IntegerField(default=0)
    soothsay = models.IntegerField(default=0)
    sovereign = models.IntegerField(default=0)
    spring = models.IntegerField(default=0)
    summer = models.IntegerField(default=0)
    wayfare = models.IntegerField(default=0)
    winter = models.IntegerField(default=0)

    actor = models.IntegerField(default=0)
    fae = models.IntegerField(default=0)
    nature_realm = models.IntegerField(default=0)
    prop = models.IntegerField(default=0)
    scene = models.IntegerField(default=0)
    time = models.IntegerField(default=0)

    banality = models.IntegerField(default=3)
    glamour = models.IntegerField(default=4)

    MUSING_THRESHOLDS = [
        ("inspire_creativity", "Inspire Creativity"),
        ("create_hope", "Create Hope"),
        ("create_love", "Create Love"),
        ("create_calm", "Create Calm"),
        ("foster_trust", "Foster Trust"),
        ("help_those_in_need", "Help Those In Need"),
        ("foster_dreams", "Foster Dreams"),
    ]

    RAVAGING_THRESHOLDS = [
        ("exhaust_creativity", "Exhaust Creativity"),
        ("destroy_hope", "Destroy Hope"),
        ("destroy_love", "Destroy Love"),
        ("create_anger", "Create Anger"),
        ("break_trust", "Break Trust"),
        ("exploit_dependence", "Exploit Dependence"),
        ("destroy_illusions", "Destroy Illusions"),
    ]

    musing_threshold = models.CharField(
        default="", max_length=20, choices=MUSING_THRESHOLDS,
    )
    ravaging_threshold = models.CharField(
        default="", max_length=20, choices=RAVAGING_THRESHOLDS,
    )

    antithesis = models.TextField(default="")

    true_name = models.TextField(default="")
    data_ennobled = models.TextField(default="")
    crysalis = models.TextField(default="")
    date_of_crysalis = models.TextField(default="")
    fae_mien = models.TextField(default="")

    # def __init__(self, *args, **kwargs):
    #     kwargs["willpower"] = kwargs.get("willpower") or 4
    #     super().__init__(*args, **kwargs)

    def has_court(self):
        return self.court != ""

    def set_court(self, court):
        self.court = court
        return True

    def random_court(self):
        return self.set_court(random.choice(["seelie", "unseelie"]))

    def has_seelie_legacy(self):
        return self.seelie_legacy is not None

    def set_seelie_legacy(self, legacy):
        if legacy.court == "seelie":
            self.seelie_legacy = legacy
            return True
        return False

    def random_seelie_legacy(self):
        legacy = CtDLegacy.objects.filter(court="seelie").order_by("?").first()
        return self.set_seelie_legacy(legacy)

    def has_unseelie_legacy(self):
        return self.unseelie_legacy is not None

    def set_unseelie_legacy(self, legacy):
        if legacy.court == "unseelie":
            self.unseelie_legacy = legacy
            return True
        return False

    def random_unseelie_legacy(self):
        legacy = CtDLegacy.objects.filter(court="unseelie").order_by("?").first()
        return self.set_unseelie_legacy(legacy)

    def has_seeming(self):
        return self.seeming != ""

    def set_seeming(self, seeming):
        self.willpower = 4
        self.seeming = seeming
        if self.seeming == "childling":
            self.add_glamour()
        if self.seeming == "wilder":
            random.choice([self.add_glamour, self.add_willpower])()
        if self.seeming == "grump":
            self.add_willpower()
        return True

    def random_seeming(self):
        return self.set_seeming(random.choice(["childling", "wilder", "grump"]))

    def add_art(self, art):
        return add_dot(self, art, 5)

    def get_arts(self):
        return {
            "autumn": self.autumn,
            "chicanery": self.chicanery,
            "chronos": self.chronos,
            "contract": self.contract,
            "dragons_ire": self.dragons_ire,
            "legerdemain": self.legerdemain,
            "metamorphosis": self.metamorphosis,
            "naming": self.naming,
            "oneiromancy": self.oneiromancy,
            "primal": self.primal,
            "pyretics": self.pyretics,
            "skycraft": self.skycraft,
            "soothsay": self.soothsay,
            "sovereign": self.sovereign,
            "spring": self.spring,
            "summer": self.summer,
            "wayfare": self.wayfare,
            "winter": self.winter,
        }

    def filter_arts(self, minimum=0, maximum=5):
        return [k for k, v in self.get_arts().items() if minimum <= v <= maximum]

    def has_arts(self):
        return self.total_arts() == 3

    def total_arts(self):
        return sum(v for v in self.get_arts().values())

    def random_art(self):
        art = weighted_choice(self.get_arts())
        return self.add_art(art)

    def random_arts(self):
        while not self.has_arts():
            self.random_art()

    def add_realm(self, realm):
        return add_dot(self, realm, 5)

    def get_realms(self):
        return {
            "actor": self.actor,
            "fae": self.fae,
            "nature_realm": self.nature_realm,
            "prop": self.prop,
            "scene": self.scene,
            "time": self.time,
        }

    def filter_realms(self, minimum=0, maximum=5):
        return [k for k, v in self.get_realms().items() if minimum <= v <= maximum]

    def has_realms(self):
        return self.total_realms() == 5

    def total_realms(self):
        return sum(v for v in self.get_realms().values())

    def random_realm(self):
        realm = weighted_choice(self.get_realms())
        return self.add_art(realm)

    def random_realms(self):
        while not self.has_realms():
            self.random_realm()

    def add_banality(self):
        return add_dot(self, "banality", 10)

    def add_glamour(self):
        return add_dot(self, "glamour", 10)

    def has_musing_threshold(self):
        return self.musing_threshold != ""

    def set_musing_threshold(self, threshold):
        self.musing_threshold = threshold
        return True

    def random_musing_threshold(self):
        threshold = random.choice(self.MUSING_THRESHOLDS)[0]
        return self.set_musing_threshold(threshold)

    def has_ravaging_threshold(self):
        return self.ravaging_threshold != ""

    def set_ravaging_threshold(self, threshold):
        self.ravaging_threshold = threshold
        return True

    def random_ravaging_threshold(self):
        threshold = random.choice(self.RAVAGING_THRESHOLDS)[0]
        return self.set_ravaging_threshold(threshold)

    def set_antithesis(self, antithesis):
        self.antithesis = antithesis
        return True

    def has_antithesis(self):
        return self.antithesis != ""

    def random_antithesis(self):
        return self.set_antithesis("Antithesis")

    def has_changeling_history(self):
        b = True
        b = b and (self.true_name != "")
        b = b and (self.data_ennobled != "")
        b = b and (self.crysalis != "")
        b = b and (self.date_of_crysalis != "")
        return b

    def has_changeling_appearance(self):
        return self.fae_mien != ""

    def freebie_frequencies(self):
        return {
            "attribute": 15,
            "ability": 8,
            "background": 10,
            "willpower": 1,
            "meritflaw": 50,
            "art": 20,
            "realm": 20,
            "glamour": 10,
        }

    def random_freebie_functions(self):
        return {
            "attribute": self.random_freebies_attributes,
            "ability": self.random_freebies_abilities,
            "background": self.random_freebies_background,
            "willpower": self.random_freebies_willpower,
            "meritflaw": self.random_freebies_meritflaw,
            "art": self.random_freebies_art,
            "realm": self.random_freebies_realm,
            "glamour": self.random_freebies_glamour,
        }

    def random_freebies_art(self):
        trait = weighted_choice(self.get_arts())
        self.spend_freebies(trait)

    def random_freebies_realm(self):
        trait = weighted_choice(self.get_realms())
        self.spend_freebies(trait)

    def random_freebies_glamour(self):
        self.spend_freebies("glamour")

    def freebie_cost(self, trait):
        cost = super().freebie_cost(trait)
        if cost != 10000:
            return cost
        costs = defaultdict(lambda: 10000, {"art": 5, "realm": 2, "glamour": 3,},)
        return costs[trait]

    def spend_freebies(self, trait):
        output = super().spend_freebies(trait)
        if output in [True, False]:
            return output
        if trait in self.get_arts():
            cost = self.freebie_cost("art")
            if cost <= self.freebies:
                if self.add_art(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait in self.get_realms():
            cost = self.freebie_cost("realm")
            if cost <= self.freebies:
                if self.add_realm(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        if trait == "glamour":
            cost = self.freebie_cost("glamour")
            if cost <= self.freebies:
                if self.add_glamour():
                    self.freebies -= cost
                    return True
                return False
            return False

    def birthright_correction(self):
        if self.kith.name == "Troll":
            self.add_attribute("strength", maximum=10)
        if self.kith.name == "Satyr":
            self.add_attribute("stamina", maximum=10)
        if self.kith.name == "Piskey":
            self.add_attribute("dexterity", maximum=10)
        if "Sidhe" in self.kith.name:
            self.add_attribute("appearance", maximum=10)
            self.add_attribute("appearance", maximum=10)


class Motley(Group):
    type = "motley"
