import random
from logging import StrFormatStyle

from django.contrib.auth.models import User
from django.db import models

from accounts.models import WoDProfile
from core.models import Language, Material, Medium
from core.utils import add_dot, weighted_choice
from wod.models.characters.human import Human


# Create your models here.
class Instrument(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Practice(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abilities = models.JSONField(default=list)
    instruments = models.ManyToManyField(Instrument, blank=True)

    def __str__(self):
        return self.name


class Paradigm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    practices = models.ManyToManyField(Practice, blank=True)

    def __str__(self):
        return self.name


class MageFaction(models.Model):
    name = models.CharField(max_length=100, unique=True)
    languages = models.ManyToManyField(Language, blank=True)
    affinities = models.JSONField(default=list)
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    media = models.ManyToManyField(Medium, blank=True)
    materials = models.ManyToManyField(Material, blank=True)
    founded = models.IntegerField(default=-5000)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_all_paradigms(self):
        factions = [self]
        while factions[-1].parent is not None:
            factions.append(factions[-1].parent)
        paradigms = Paradigm.objects.none()
        for faction in factions:
            paradigms |= faction.paradigms.all()
        return paradigms

    def get_all_practices(self):
        factions = [self]
        while factions[-1].parent is not None:
            factions.append(factions[-1].parent)
        practices = Practice.objects.none()
        for faction in factions:
            practices |= faction.practices.all()
        return practices


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

    affiliation = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="affiliations",
    )
    faction = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="factions",
    )
    subfaction = models.ForeignKey(
        MageFaction,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subfactions",
    )

    correspondence = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    entropy = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)

    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)

    arete = models.IntegerField(default=0)

    affinity_sphere = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=[
            ("correspondence", "Correspondence"),
            ("time", "Time"),
            ("spirit", "Spirit"),
            ("mind", "Mind"),
            ("entropy", "Entropy"),
            ("prime", "Prime"),
            ("forces", "Forces"),
            ("matter", "Matter"),
            ("life", "Life"),
        ],
    )

    corr_name = models.CharField(
        default="correspondence",
        choices=[("correspondence", "Correspondence"), ("data", "Data")],
        max_length=100,
    )
    prime_name = models.CharField(
        default="prime",
        choices=[("prime", "Prime"), ("primal_utility", "Primal Utility")],
        max_length=100,
    )
    spirit_name = models.CharField(
        default="spirit",
        choices=[("spirit", "Spirit"), ("dimensional_science", "Dimensional Science")],
        max_length=100,
    )

    awakening = models.TextField(default="")
    seekings = models.TextField(default="")
    quiets = models.TextField(default="")
    age_of_awakening = models.IntegerField(default=0)
    avatar_description = models.TextField(default="")

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
            "correspondence": self.correspondence,
            "time": self.time,
            "spirit": self.spirit,
            "mind": self.mind,
            "entropy": self.entropy,
            "prime": self.prime,
            "forces": self.forces,
            "matter": self.matter,
            "life": self.life,
        }

    def has_faction(self):
        return self.faction is not None

    def set_faction(self, faction, subfaction=None):
        self.faction = faction
        if self.faction.parent is not None:
            self.affiliation = self.faction.parent
        if self.subfaction is not None:
            if self.subfaction.parent == self.faction:
                self.subfaction = subfaction
        return True

    def random_faction(self):
        self.affiliation = MageFaction.objects.filter(parent=None).order_by("?").first()
        self.faction = (
            MageFaction.objects.filter(parent=self.affiliation).order_by("?").first()
        )
        if random.random() < 0.25:
            self.subfaction = (
                MageFaction.objects.filter(parent=self.faction).order_by("?").first()
            )

    def has_focus(self):
        return (
            self.paradigms.count() > 0
            and self.practices.count() > 0
            and self.instruments.count() >= 7
        )

    def set_focus(self):
        pass

    def random_focus(self):
        pass

    def add_sphere(self, sphere):
        return add_dot(self, sphere, self.arete)

    def filter_spheres(self, minimum=0, maximum=5):
        return {
            k: v
            for k, v in self.get_spheres().items()
            if minimum <= v <= min(maximum, self.arete - 1)
        }

    def total_spheres(self):
        return sum(self.get_spheres().values())

    def has_spheres(self):
        if self.affinity_sphere is not None:
            aff_flag = getattr(self, self.affinity_sphere) > 0
        else:
            aff_flag = False
        total = self.total_spheres() == 6
        return aff_flag and total

    def set_affinity_sphere(self, affinity):
        self.affinity_sphere = affinity
        self.add_sphere(affinity)
        return True

    def has_affinity_sphere(self):
        return self.affinity_sphere is not None

    def random_affinity_sphere(self):
        self.set_affinity_sphere(random.choice(list(self.get_spheres().keys())))

    def random_sphere(self):
        if self.affinity_sphere is None:
            self.random_affinity_sphere()
        if len(self.filter_spheres(maximum=self.arete - 1).keys()) != 0:
            choice = weighted_choice(self.filter_spheres(maximum=self.arete - 1))
            self.add_sphere(choice)

    def random_spheres(self):
        while self.total_spheres() < 6:
            self.random_sphere()

    def add_arete(self):
        if self.arete < 10:
            self.arete += 1
            return True
        return False

    def random_arete(self):
        self.arete = random.randint(1, 4)
        self.freebies -= (self.arete - 1) * 4

    def has_mage_history(self):
        return (
            self.awakening != ""
            and self.seekings != ""
            and self.quiets != ""
            and self.age_of_awakening != 0
            and self.avatar_description != ""
        )

    def random_xp_spend(self):
        pass

    def random_freebies(self):
        pass

    def random(self):
        pass


class Cabal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(Mage, blank=True)
    leader = models.ForeignKey(
        Mage, blank=True, related_name="leads", on_delete=models.CASCADE, null=True
    )

    def random(self, num_chars, new_characters=False):
        if not new_characters and Mage.objects.count() < num_chars:
            raise ValueError("Not enough Mages!")
        elif not new_characters:
            self.members.set(Mage.objects.order_by("?")[:num_chars])
        else:
            if WoDProfile.objects.filter(storyteller=True).count() > 0:
                user = (
                    WoDProfile.objects.filter(storyteller=True)
                    .order_by("?")
                    .first()
                    .user
                )
            else:
                user = User.objects.create_user(username="New User")
                user.wod_profile.storyteller = True
                user.save()
            for _ in range(num_chars):
                m = Mage.objects.create(
                    name=f"{self.name} {self.members.count() + 1}",
                    player=user.wod_profile,
                )
                m.random()
                self.members.add(m)
        self.leader = self.members.order_by("?").first()
        self.save()

    def __str__(self):
        return self.name
