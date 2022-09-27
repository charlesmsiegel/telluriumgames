import random

from django.db import models
from django.db.models import F, Q

from core.utils import add_dot
from exalted.models.characters.charms import DragonBloodedCharm, MartialArtsCharm
from exalted.models.characters.mortals import ExMortal
from exalted.models.characters.utils import ABILITIES


# Create your models here.
class DragonBlooded(ExMortal):
    type = "dragon-blooded"

    ASPECT_CHOICES = [
        ("fire", "Fire"),
        ("water", "Water"),
        ("air", "Air"),
        ("earth", "Earth"),
        ("wood", "Wood"),
    ]
    ORIGIN_CHOICES = [
        ("dynast", "Dynast"),
        ("dynast_outcaste", "Dynastic Outcaste"),
        ("cadet", "Cadet House"),
        ("prasadi", "Prasadi"),
        ("lookshyan", "Lookshyan"),
        ("foriegn_outcaste", "Foreign Outcaste"),
    ]
    HOUSE_CHOICES = [
        ("cathak", "Cathak"),
        ("cynis", "Cynis"),
        ("iselsi", "Iselsi"),
        ("ledaal", "Ledaal"),
        ("mnemon", "Mnemon"),
        ("nellens", "Nellens"),
        ("peleps", "Peleps"),
        ("ragara", "Ragara"),
        ("sesus", "Sesus"),
        ("tepet", "Tepet"),
        ("vneef", "V'neef"),
        ("ferem", "Ferem"),
        ("desai", "Desai"),
        ("burano", "Burano"),
        ("ophris", "Ophris"),
        ("yueh", "Yueh"),
        ("amilar", "Amilar"),
        ("karal", "Karal"),
        ("maheka", "Maheka"),
        ("teresu", "Teresu"),
        ("yushoto", "Yushoto"),
        ("kiriga", "Kiriga"),
        ("nefvarin", "Nefvarin"),
        ("nerigus", "Nerigus"),
        ("sirel", "Sirel"),
        ("taroketu", "Taroketu"),
        ("toriki", "Toriki"),
        ("yan_tu", "Yan Tu"),
        ("violet_fangs", "The Cult of the Violet Fang"),
        ("grass_spiders", "The Grass Spiders"),
        ("heavens_dragons", "Heaven's Dragons"),
        ("khamaseen_battalion", "The Khamaseen Battalion"),
        ("rogue_legion", "The Rogue Legion of Saloy Hin"),
        ("yatanis_children", "Yatani's Children"),
        ("forest_witches", "Forest Witches"),
    ]
    SCHOOL_CHOICES = [
        ("cloister", "The Cloister of Wisdom"),
        ("heptagram", "The Heptagram"),
        ("house_of_bells", "The House of Bells"),
        ("spiral_academy", "The Spiral Academy"),
        ("pasiaps_stair", "Pasiap's Stair"),
    ]

    aspect = models.CharField(max_length=50, choices=ASPECT_CHOICES)
    aspect_abilities = models.JSONField(default=list)
    favored_abilities = models.JSONField(default=list)
    origin = models.CharField(default="", max_length=100, choices=ORIGIN_CHOICES)
    house = models.CharField(default="", max_length=100, choices=HOUSE_CHOICES)
    school = models.CharField(default="", max_length=100, choices=SCHOOL_CHOICES)

    charms = models.ManyToManyField(DragonBloodedCharm, blank=True)
    martial_arts_charms = models.ManyToManyField(MartialArtsCharm, blank=True)

    def has_aspect(self):
        return self.aspect != ""

    def set_aspect(self, aspect):
        self.aspect = aspect
        if aspect == "air":
            self.aspect_abilities = [
                "linguistics",
                "lore",
                "occult",
                "stealth",
                "thrown",
            ]
        elif aspect == "earth":
            self.aspect_abilities = [
                "awareness",
                "craft",
                "integrity",
                "resistance",
                "war",
            ]
        elif aspect == "fire":
            self.aspect_abilities = [
                "athletics",
                "dodge",
                "melee",
                "presence",
                "socialize",
            ]
        elif aspect == "water":
            self.aspect_abilities = [
                "brawl",
                "martial_arts",
                "bureaucracy",
                "investigation",
                "larceny",
                "sail",
            ]
        elif aspect == "wood":
            self.aspect_abilities = [
                "archery",
                "medicine",
                "performance",
                "ride",
                "survival",
            ]
        return True

    def random_aspect(self):
        asp = random.choice(self.ASPECT_CHOICES)[0]
        return self.set_aspect(asp)

    def has_origin(self):
        return self.origin != ""

    def set_origin(self, origin):
        self.origin = origin
        return True

    def random_origin(self):
        origin = random.choice(self.ORIGIN_CHOICES)[0]
        origin_bool = self.set_origin(origin)
        if not origin_bool:
            return False
        if origin == "dynast":
            houses = [
                "cathak",
                "cynis",
                "iselsi",
                "ledaal",
                "mnemon",
                "nellens",
                "peleps",
                "ragara",
                "sesus",
                "tepet",
                "vneef",
            ]
        elif origin == "dynast_outcaste":
            houses = [
                "cathak",
                "cynis",
                "iselsi",
                "ledaal",
                "mnemon",
                "nellens",
                "peleps",
                "ragara",
                "sesus",
                "tepet",
                "vneef",
            ]
        elif origin == "cadet":
            houses = [
                "ferem",
                "desai",
                "yueh",
            ]
        elif origin == "prasadi":
            houses = [
                "burano",
                "ophris",
            ]
        elif origin == "lookshyan":
            houses = [
                "amilar",
                "karal",
                "maheka",
                "teresu",
                "yushoto",
                "kiriga",
                "nefvarin",
                "nerigus",
                "sirel",
                "taroketu",
                "toriki",
                "yan_tu",
            ]
        elif origin == "foriegn_outcaste":
            houses = [
                "violet_fangs",
                "grass_spiders",
                "heavens_dragons",
                "khamaseen_battalion",
                "rogue_legion",
                "yatanis_children",
                "forest_witches",
            ]
        else:
            return False
        house = random.choice(houses)
        if not self.set_house(house):
            return False
        if origin == "dynast":
            self.set_school(self.SCHOOL_CHOICES)
        return True

    def set_house(self, house):
        self.house = house
        return True

    def set_school(self, school):
        self.school = school
        return True

    def has_favored_abilities(self):
        return len(self.favored_abilities) == 5

    def add_favored_ability(self, ability):
        if ability in self.favored_abilities:
            return False
        self.favored_abilities.append(ability)
        add_dot(self, ability, maximum=1)
        return True

    def random_favored_ability(self):
        options = [
            x
            for x in ABILITIES
            if x not in self.favored_abilities + self.aspect_abilities
        ]
        choice = random.choice(options)
        return self.add_favored_ability(choice)

    def random_favored_abilities(self):
        while not self.has_favored_abilities():
            self.random_favored_ability()

    def random_name(self):
        return self.set_name(f"Dragon-Blooded {DragonBlooded.objects.count()}")

    def apply_finishing_touches(self):
        self.willpower = 5
        self.health_levels = 7
        self.essence = 2
        self.save()
        return True

    def total_charms(self):
        return self.charms.count() + self.martial_arts_charms.count()

    def total_excellencies(self):
        excellencies = [x for x in self.charms.all() if "excellency" in x.keywords]
        return len(excellencies)

    def has_excellencies(self):
        return self.total_excellencies() >= 5

    def has_charms(self):
        return self.total_charms() == 20 and self.has_excellencies()

    def filter_excellencies(self):
        charm_list = self.filter_charms()
        return [x for x in charm_list if "excellency" in x.keywords]

    def filter_charms(self):
        q = Q()
        for ability in ABILITIES:
            q |= Q(
                statistic=ability,
                min_statistic__lte=getattr(self, ability),
                min_essence__lte=self.essence,
            )

        filtered_charms = DragonBloodedCharm.objects.filter(q)
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
                if charm.type == "dragon_blooded_charm":
                    self.charms.add(charm)
                    return True
                if charm.type == "martial_arts_charm":
                    self.martial_arts_charms.add(charm)
                    return True
            return False
        return False

    def random_excellency(self):
        options = self.filter_excellencies()
        op = random.choice(options)
        return self.add_charm(op)

    def random_charm(self):
        c = random.choice(self.filter_charms())
        return self.add_charm(c)

    def random_excellencies(self):
        while not self.has_excellencies():
            self.random_excellency()

    def random_charms(self):
        self.random_excellencies()
        while not self.has_charms():
            self.random_charm()

    def has_specialties(self):
        return self.specialties.count() == 3

    def random_additional_specialties(self):
        if self.school is not None:
            num_specs = 2
            if self.school == "cloister":
                abilities = ["integrity", "lore", "martial_arts"]
            elif self.school == "heptagram":
                abilities = ["craft", "lore", "occult"]
            elif self.school == "house_of_bells":
                abilities = ["archery", "melee", "war"]
            elif self.school == "spiral_academy":
                abilities = ["bureaucracy", "presence", "socialize"]
            elif self.school == "pasiaps_stair":
                abilities = ["athletics", "resistance", "war"]
        elif self.house in ["burano", "ophris"]:
            num_specs = 2
            if self.house == "burano":
                abilities = ["bureaucracy", "integrity", "resistance"]
            elif self.house == "ophris":
                abilities = ["athletics", "performance", "socialize"]
        elif self.house == "forest_witches":
            abilities = ["integrity", "occult", "survival"]
            num_specs = 2
        else:
            abilities = ABILITIES
            num_specs = 1
        for _ in range(num_specs):
            abb = random.choice(abilities)
            self.random_specialty(self, ability=abb)

    def random(self, bonus_points=18, xp=0):
        self.update_status("Ran")
        self.bonus_points = bonus_points
        self.xp = xp
        self.essence = 2
        self.random_name()
        self.random_concept()
        self.random_aspect()
        self.random_favored_abilities()
        self.random_attributes(primary=8, secondary=6, tertiary=4)
        self.random_abilities()
        self.random_merits(
            num_dots=5,
            list_of_merits=[
                "Backing",
                "Command",
                "Contacts",
                "Followers",
                "Influence",
                "Language",
                "Resources",
                "Retainers",
            ],
        )
        self.random_merits(num_dots=18)
        self.random_excellencies()
        self.random_charms()
        self.random_specialties()
        self.random_additional_specialties()
        self.random_intimacies()
        self.random_spend_bonus_points()
        self.random_spend_xp()
        self.apply_finishing_touches()
