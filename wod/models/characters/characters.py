import random

from accounts.models import WoDProfile
from core.models import Language
from core.utils import add_dot, weighted_choice
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now
from polymorphic.models import PolymorphicModel


# Create your models here.
class Character(PolymorphicModel):
    """Base Character class"""

    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    name = models.CharField(max_length=100, unique=True)
    concept = models.CharField(max_length=300)
    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)
    type = "character"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:character", args=[str(self.id)])

    def has_name(self):
        if self.name != "":
            return True
        return False

    def has_concept(self):
        if self.concept != "":
            return True
        return False

    def mark_complete(self):
        self.status = "Sub"

    def mark_approved(self):
        self.status = "App"

    def mark_retired(self):
        self.status = "Ret"

    def mark_deceased(self):
        self.status = "Dec"


class HumanCharacter(Character):
    """Human Character class"""

    archetype_keys = [
        "ACT",
        "BEN",
        "CON",
        "CRU",
        "HAC",
        "IDE",
        "INN",
        "KID",
        "LON",
        "MAC",
        "MAD",
        "MAR",
        "MON",
        "PRO",
        "ROG",
        "SEN",
        "SUR",
        "TRA",
        "TRI",
        "VIS",
    ]
    archetypes = [
        "Activist",
        "Benefactor",
        "Contrary",
        "Crusader",
        "Hacker",
        "Idealist",
        "Innovator",
        "Kid",
        "Loner",
        "Machine",
        "Mad Scientist",
        "Martyr",
        "Monster",
        "Prophet",
        "Rogue",
        "Sensualist",
        "Survivor",
        "Traditionalist",
        "Trickster",
        "Visionary",
    ]
    nature = models.CharField(max_length=3, choices=zip(archetype_keys, archetypes))
    demeanor = models.CharField(max_length=3, choices=zip(archetype_keys, archetypes))

    strength = models.IntegerField(default=1)
    strength_specialty = models.CharField(max_length=100, blank=True, null=True)
    dexterity = models.IntegerField(default=1)
    dexterity_specialty = models.CharField(max_length=100, blank=True, null=True)
    stamina = models.IntegerField(default=1)
    stamina_specialty = models.CharField(max_length=100, blank=True, null=True)

    perception = models.IntegerField(default=1)
    perception_specialty = models.CharField(max_length=100, blank=True, null=True)
    intelligence = models.IntegerField(default=1)
    intelligence_specialty = models.CharField(max_length=100, blank=True, null=True)
    wits = models.IntegerField(default=1)
    wits_specialty = models.CharField(max_length=100, blank=True, null=True)

    charisma = models.IntegerField(default=1)
    charisma_specialty = models.CharField(max_length=100, blank=True, null=True)
    manipulation = models.IntegerField(default=1)
    manipulation_specialty = models.CharField(max_length=100, blank=True, null=True)
    appearance = models.IntegerField(default=1)
    appearance_specialty = models.CharField(max_length=100, blank=True, null=True)

    current_health_levels = models.CharField(default="", max_length=100, blank=True)

    merits_and_flaws = models.ManyToManyField("MeritFlaw", blank=True)
    languages = models.ManyToManyField(Language, blank=True)

    age = models.IntegerField(default=18)
    apparent_age = models.IntegerField(default=18)
    date_of_birth = models.DateField(default=now)
    hair = models.CharField(max_length=200, default="", blank=True, null=True)
    eyes = models.CharField(max_length=200, default="", blank=True, null=True)
    ethnicity = models.CharField(max_length=200, default="", blank=True, null=True)
    nationality = models.CharField(max_length=200, default="", blank=True, null=True)
    height = models.CharField(max_length=200, default="", blank=True, null=True)
    weight = models.CharField(max_length=200, default="", blank=True, null=True)
    sex = models.CharField(max_length=200, default="", blank=True, null=True)
    description = models.TextField(default="", blank=True, null=True)

    childhood = models.TextField(default="", blank=True, null=True)
    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)

    notes = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.TextField(default="", blank=True, null=True)

    background_points = 5
    freebies = 15
    type = "humancharacter"

    def get_mental_attributes(self):
        return {
            "intelligence": self.intelligence,
            "wits": self.wits,
            "perception": self.perception,
        }

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }

    def physical_attribute_sum(self):
        return sum(self.get_physical_attributes().values())

    def mental_attribute_sum(self):
        return sum(self.get_mental_attributes().values())

    def social_attribute_sum(self):
        return sum(self.get_social_attributes().values())

    def random_attributes(self, primary=7, secondary=5, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.physical_attribute_sum() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            add_dot(self, attribute_choice, 5)
        while self.social_attribute_sum() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(self.get_social_attributes())
            add_dot(self, attribute_choice, 5)
        while self.mental_attribute_sum() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            add_dot(self, attribute_choice, 5)

    def get_wound_penalty(self):
        health_levels = len(self.current_health_levels)
        if health_levels <= 1:
            return 0
        if health_levels <= 3:
            return -1
        if health_levels <= 5:
            return -2
        if health_levels <= 6:
            return -5
        return -1000

    def has_archetypes(self):
        if self.nature != "" and self.demeanor != "":
            return True
        return False

    def random_nature(self):
        self.nature = random.choice(self.archetype_keys)
        self.save()

    def random_demeanor(self):
        self.demeanor = random.choice(self.archetype_keys)
        self.save()

    def add_bashing(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "B"
        elif "B" in self.current_health_levels:
            self.current_health_levels = self.current_health_levels.replace("B", "L", 1)
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    @staticmethod
    def sort_damage(damage_type):
        if damage_type == "B":
            return 2
        if damage_type == "L":
            return 1
        # All other damage should be Aggravated
        return 0

    def add_aggravated(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "A"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def add_lethal(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "L"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def merit_cost(self):
        return sum([x.cost for x in self.merits_and_flaws.filter(cost__gt=0)])

    def flaw_cost(self):
        return sum([x.cost for x in self.merits_and_flaws.filter(cost__lt=0)])

    @staticmethod
    def attributes():
        return [
            "strength",
            "dexterity",
            "stamina",
            "perception",
            "intelligence",
            "wits",
            "charisma",
            "manipulation",
            "appearance",
        ]

    def has_finishing_touches(self):
        touches = True
        touches = touches and self.age
        touches = touches and self.apparent_age
        touches = touches and self.date_of_birth
        touches = touches and self.hair
        touches = touches and self.eyes
        touches = touches and self.ethnicity
        touches = touches and self.nationality
        touches = touches and self.height
        touches = touches and self.weight
        touches = touches and self.sex
        touches = touches and self.description
        return touches

    def has_history(self):
        history = True
        history = history and self.childhood
        history = history and self.history
        history = history and self.goals
        return history


class MeritFlaw(models.Model):
    """Class for Character based Merits and Flaws"""

    name = models.CharField(max_length=100)
    cost = models.IntegerField(default=0)
