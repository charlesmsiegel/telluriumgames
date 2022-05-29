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

    essence = models.CharField(
        default="",
        max_length=100,
        choices=[
            ("dynamic", "Dynamic"),
            ("pattern", "Pattern"),
            ("primordial", "Primordial"),
            ("questing", "Questing"),
        ],
    )

    awareness = models.IntegerField(default=0)
    art = models.IntegerField(default=0)
    leadership = models.IntegerField(default=0)
    animal_kinship = models.IntegerField(default=0)
    blatancy = models.IntegerField(default=0)
    carousing = models.IntegerField(default=0)
    do = models.IntegerField(default=0)
    flying = models.IntegerField(default=0)
    high_ritual = models.IntegerField(default=0)
    lucid_dreaming = models.IntegerField(default=0)
    search = models.IntegerField(default=0)
    seduction = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    meditation = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)
    acrobatics = models.IntegerField(default=0)
    archery = models.IntegerField(default=0)
    biotech = models.IntegerField(default=0)
    energy_weapons = models.IntegerField(default=0)
    hypertech = models.IntegerField(default=0)
    jetpack = models.IntegerField(default=0)
    riding = models.IntegerField(default=0)
    torture = models.IntegerField(default=0)
    cosmology = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    esoterica = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    area_knowledge = models.IntegerField(default=0)
    belief_systems = models.IntegerField(default=0)
    cryptography = models.IntegerField(default=0)
    demolitions = models.IntegerField(default=0)
    finance = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    media = models.IntegerField(default=0)
    pharmacopeia = models.IntegerField(default=0)

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

    background_points = 7

    def __init__(self, *args, **kwargs):
        kwargs["willpower"] = kwargs.get("willpower") or 5
        super().__init__(*args, **kwargs)

    def get_talents(self):
        tmp = super().get_talents()
        tmp.update(
            {
                "awareness": self.awareness,
                "art": self.art,
                "leadership": self.leadership,
                "animal_kinship": self.animal_kinship,
                "blatancy": self.blatancy,
                "carousing": self.carousing,
                "do": self.do,
                "flying": self.flying,
                "high_ritual": self.high_ritual,
                "lucid_dreaming": self.lucid_dreaming,
                "search": self.search,
                "seduction": self.seduction,
            }
        )
        return tmp

    def get_skills(self):
        tmp = super().get_skills()
        tmp.update(
            {
                "martial_arts": self.martial_arts,
                "meditation": self.meditation,
                "research": self.research,
                "survival": self.survival,
                "technology": self.technology,
                "acrobatics": self.acrobatics,
                "archery": self.archery,
                "biotech": self.biotech,
                "energy_weapons": self.energy_weapons,
                "hypertech": self.hypertech,
                "jetpack": self.jetpack,
                "riding": self.riding,
                "torture": self.torture,
            }
        )
        return tmp

    def get_knowledges(self):
        tmp = super().get_knowledges()
        tmp.update(
            {
                "cosmology": self.cosmology,
                "enigmas": self.enigmas,
                "esoterica": self.esoterica,
                "law": self.law,
                "occult": self.occult,
                "politics": self.politics,
                "area_knowledge": self.area_knowledge,
                "belief_systems": self.belief_systems,
                "cryptography": self.cryptography,
                "demolitions": self.demolitions,
                "finance": self.finance,
                "lore": self.lore,
                "media": self.media,
                "pharmacopeia": self.pharmacopeia,
            }
        )
        return tmp

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

    def set_focus(self, paradigms, practices, instruments):
        self.paradigms.set(paradigms)
        self.practices.set(practices)
        self.instruments.set(instruments)
        return True

    def random_focus(self):
        paradigms = {x: 1 for x in Paradigm.objects.all()}
        practices = {x: 1 for x in Practice.objects.all()}
        instruments = {x: 1 for x in Instrument.objects.all()}
        if self.affiliation:
            for paradigm in self.affiliation.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.affiliation.practices.all():
                practices[practice] += 1
        if self.faction:
            for paradigm in self.faction.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.faction.practices.all():
                practices[practice] += 1
        if self.subfaction:
            for paradigm in self.subfaction.paradigms.all():
                paradigms[paradigm] += 1
            for practice in self.subfaction.practices.all():
                practices[practice] += 1
        self.paradigms.add(weighted_choice(paradigms))
        while random.random() < 0.1:
            self.paradigms.add(
                weighted_choice(
                    {
                        k: v
                        for k, v in paradigms.items()
                        if k not in self.paradigms.all()
                    }
                )
            )
        for paradigm in self.paradigms.all():
            for practice in paradigm.practices.all():
                practices[practice] += 1

        self.practices.add(weighted_choice(practices))
        while random.random() < 0.1:
            self.practices.add(
                weighted_choice(
                    {
                        k: v
                        for k, v in practices.items()
                        if k not in self.practices.all()
                    }
                )
            )

        for practice in self.practices.all():
            for instrument in practice.instruments.all():
                instruments[instrument] += 1
        while self.instruments.count() < 7:
            self.instruments.add(weighted_choice(instruments))

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

    def has_essence(self):
        return self.essence != ""

    def set_essence(self, essence):
        self.essence = essence
        return True

    def random_essence(self):
        options = ["Dynamic", "Pattern", "Primordial", "Questing"]
        choice = random.choice(options)
        self.set_essence(choice)

    def total_resonance(self):
        pass

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

# # Backgrounds
# Allies
# Alternate Identity
# Arcane
# Avatar
# Backup
# Blessing
# Certification
# Chantry
# Cult
# Demesne
# Destiny
# Dream
# Enhancement
# Fame
# Familiar
# Influence
# Legend
# Library
# Node
# Past Lives
# Patron
# Rank
# Requisitions
# Resources
# Retainers
# Sanctum
# Secret Weapons
# Spies
# Status
# Totem
# Wonder
