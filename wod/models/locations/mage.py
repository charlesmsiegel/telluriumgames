import random

from django.db import models
from django.db.models import F, Q

from core.utils import add_dot, weighted_choice
from wod.models.characters.human import Human
from wod.models.characters.mage.faction import MageFaction
from wod.models.characters.mage.resonance import Resonance
from wod.models.characters.mage.utils import SPHERE_LIST
from wod.models.items.mage import Library
from wod.models.locations.human import Location


# Create your models here.
class SizeChoices(models.IntegerChoices):
    TINY = -2, "Household Object"
    SMALL = -1, "Small Room"
    NORMAL = 0, "Average Room"
    LARGE = 1, "Small Building"
    HUGE = 2, "Large Building"


class RatioChoices(models.IntegerChoices):
    TINY = -2, "0.0"
    SMALL = -1, "0.25"
    NORMAL = 0, "0.5"
    LARGE = 1, "0.75"
    HUGE = 2, "1.0"


class Node(Location):
    type = "node"

    rank = models.IntegerField(default=0)

    size = models.IntegerField(default=SizeChoices.NORMAL, choices=SizeChoices.choices)
    ratio = models.IntegerField(
        default=RatioChoices.NORMAL, choices=RatioChoices.choices
    )

    points = models.IntegerField(default=0)
    merits_and_flaws = models.ManyToManyField(
        "NodeMeritFlaw", blank=True, through="NodeMeritFlawRating"
    )
    resonance = models.ManyToManyField(
        Resonance, blank=True, through="NodeResonanceRating"
    )

    quintessence_per_week = models.IntegerField(default=0)
    tass_per_week = models.IntegerField(default=0)
    tass_form = models.CharField(default="", max_length=100)
    quintessence_form = models.CharField(default="", max_length=100)

    def __init__(self, *args, **kwargs):
        kwargs["gauntlet"] = 3
        super().__init__(*args, **kwargs)

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        self.set_rank(rank)

    def set_rank(self, rank):
        self.rank = rank
        self.points = 3 * self.rank
        return True

    def add_mf(self, mf, rating):
        if rating not in mf.ratings:
            return False
        if mf in self.merits_and_flaws.all():
            current_rating = NodeMeritFlawRating.objects.get(node=self, mf=mf).rating
            if 0 < current_rating < rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            if 0 > current_rating > rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            return False
        NodeMeritFlawRating.objects.create(node=self, mf=mf, rating=rating)
        return True

    def total_mf(self):
        return sum(x.rating for x in NodeMeritFlawRating.objects.filter(node=self))

    def filter_mf(self, minimum=-10, maximum=10):
        new_mfs = NodeMeritFlaw.objects.exclude(pk__in=self.merits_and_flaws.all())
        had_mf_ratings = NodeMeritFlawRating.objects.all()
        had_mf_ratings = had_mf_ratings.filter(rating__lt=F("mf__max_rating"))

        had_mfs = NodeMeritFlaw.objects.filter(
            pk__in=had_mf_ratings.values_list("mf", flat=True)
        )
        q = new_mfs | had_mfs
        return q

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return NodeMeritFlawRating.objects.get(node=self, mf=mf).rating

    def random_mf(self, minimum=-10, maximum=10):
        possibility = self.filter_mf(minimum=minimum, maximum=maximum)
        choice = random.choice(possibility)
        possible_ratings = choice.ratings
        possible_ratings = [x for x in possible_ratings if minimum <= x <= maximum]
        r = 0
        if self.mf_rating(choice) < 0:
            possible_ratings = [
                x for x in possible_ratings if x < self.mf_rating(choice)
            ]
        if self.mf_rating(choice) > 0:
            possible_ratings = [
                x for x in possible_ratings if x > self.mf_rating(choice)
            ]
        if len(possible_ratings) == 0:
            return False
        r = random.choice(possible_ratings)
        return self.add_mf(choice, r)

    def add_resonance(self, resonance):
        r, _ = NodeResonanceRating.objects.get_or_create(resonance=resonance, node=self)
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def resonance_rating(self, resonance):
        if resonance in self.resonance.all():
            return NodeResonanceRating.objects.get(
                node=self, resonance=resonance
            ).rating
        return 0

    def filter_resonance(self, minimum=0, maximum=5, sphere=None):
        all_res = Resonance.objects.all()
        if sphere is None:
            q = Q()
        else:
            q = Q(**{sphere: True})
        all_res = all_res.filter(q)

        maxed_resonance = [
            x.id
            for x in NodeResonanceRating.objects.filter(node=self, rating__gt=maximum)
        ]
        mined_resonance = [
            x.id
            for x in NodeResonanceRating.objects.filter(node=self, rating__lt=minimum)
        ]
        all_res = all_res.exclude(pk__in=maxed_resonance)
        all_res = all_res.exclude(pk__in=mined_resonance)
        return all_res

    def total_resonance(self):
        return sum(x.rating for x in NodeResonanceRating.objects.filter(node=self))

    def random_resonance(self, sphere=None, favored_list=None):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4, sphere=sphere)
            if len(possible) > 0:
                choice = random.choice(possible)
                if self.add_resonance(choice):
                    return True
        while True:
            if favored_list is not None:
                choices = {i: 1 for i in range(1, Resonance.objects.last().id + 1)}
                for resonance in favored_list:
                    choices[resonance.id] += 100
            else:
                choices = {i: 1 for i in range(1, Resonance.objects.last().id + 1)}
            index = weighted_choice(choices, floor=1, ceiling=1000000)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.check_resonance(choice, sphere=sphere):
                    if self.add_resonance(choice):
                        return True

    def check_resonance(self, resonance, sphere=None):
        if self.resonance_rating(resonance) < 5:
            if sphere is None:
                return True
            return getattr(resonance, sphere)
        return False

    def resonance_postprocessing(self):
        if "Corrupted" in [x.name for x in self.merits_and_flaws.all()]:
            res, _ = Resonance.objects.get_or_create(name="Corrupted")
            self.add_resonance(res)
            self.add_resonance(res)
        if "Sphere Attuned" in [x.name for x in self.merits_and_flaws.all()]:
            sphere = random.choice(SPHERE_LIST)
            self.random_resonance(sphere=sphere)

    def has_resonance(self):
        return self.total_resonance() >= self.rank

    def has_output_forms(self):
        return self.quintessence_form != "" and self.tass_form != ""

    def set_output_forms(self, quint_form, tass_form):
        self.quintessence_form = quint_form
        self.tass_form = tass_form
        return True

    def random_forms(self):
        self.set_output_forms("Quintessence", "Tass")

    def has_output(self):
        return self.quintessence_per_week != 0 or self.tass_per_week != 0

    def random_ratio(self):
        choice = random.choice([-2, -1, -1, 0, 0, 0, 1, 1, 2])
        self.set_ratio(choice)
        self.points -= self.ratio

    def random_size(self):
        choice = random.choice([-2, -1, -1, 0, 0, 0, 1, 1, 2])
        self.set_size(choice)
        self.points -= self.size

    def set_ratio(self, ratio):
        self.ratio = ratio
        return True

    def set_size(self, size):
        self.size = size
        return True

    def update_output(self):
        self.quintessence_per_week = int(self.points * float(self.get_ratio_display()))
        self.tass_per_week = self.points - self.quintessence_per_week
        return True

    def random(self, rank=None, favored_list=None):
        self.random_rank(rank=rank)
        while not self.has_resonance():
            self.random_resonance(favored_list=favored_list)
        self.random_ratio()
        self.random_size()
        self.random_forms()
        while random.random() < 0.2 and self.points > 1:
            self.random_resonance(favored_list=favored_list)
        while random.random() < 0.4 and self.points > 1:
            current = self.total_mf()
            self.random_mf(maximum=(self.points - 1))
            new = self.total_mf()
            self.points -= new - current
        self.resonance_postprocessing()
        self.update_output()
        self.points = 0


class NodeMeritFlaw(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)
    max_rating = models.IntegerField(default=0)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        super().save(*args, **kwargs)


class NodeMeritFlawRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    mf = models.ForeignKey(NodeMeritFlaw, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class NodeResonanceRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Chantry(Location):
    type = "chantry"

    faction = models.ForeignKey(
        MageFaction, blank=True, null=True, on_delete=models.CASCADE
    )

    LEADERSHIP_CHOICES = [
        ("panel", "Panel of Cabal Leaders"),
        ("teachers", "Teachers"),
        ("triumvirate", "Triumvirate"),
        ("democracy", "Democracy"),
        ("anarchy", "Anarchy"),
    ]

    leadership_type = models.CharField(
        max_length=20, null=True, choices=LEADERSHIP_CHOICES
    )

    SEASONS = [
        ("spring", "Spring"),
        ("winter", "Winter"),
        ("summer", "Summer"),
        ("autumn", "Autumn"),
    ]

    season = models.CharField(max_length=100, null=True, choices=SEASONS,)

    CHANTRY_TYPES = [
        ("exploration", "Exploration"),
        ("ancestral", "Ancestral"),
        ("hereditary", "Hereditary"),
        ("college", "College"),
        ("squatter", "Squatter"),
        ("war", "War"),
    ]

    chantry_type = models.CharField(max_length=100, null=True, choices=CHANTRY_TYPES,)

    rank = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    allies = models.IntegerField(default=0)
    arcane = models.IntegerField(default=0)
    backup = models.IntegerField(default=0)
    cult = models.IntegerField(default=0)
    elders = models.IntegerField(default=0)
    integrated_effects = models.IntegerField(default=0)
    retainers = models.IntegerField(default=0)
    spies = models.IntegerField(default=0)
    resources = models.IntegerField(default=0)
    enhancement = models.IntegerField(default=0)
    requisitions = models.IntegerField(default=0)
    reality_zone_rating = models.IntegerField(default=0)
    node_rating = models.IntegerField(default=0)
    library_rating = models.IntegerField(default=0)

    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, blank=True, null=True
    )
    nodes = models.ManyToManyField(Node, blank=True)

    members = models.ManyToManyField(Human, blank=True, related_name="member_of")
    ambassador = models.ForeignKey(
        Human,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="ambassador_from",
    )
    node_tender = models.ForeignKey(
        Human,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="tends_node_at",
    )
    investigator = models.ManyToManyField(
        Human, blank=True, related_name="investigator_at"
    )
    guardian = models.ManyToManyField(Human, blank=True, related_name="guardian_of")
    teacher = models.ManyToManyField(Human, blank=True, related_name="teacher_at")

    factional_names = {
        "Akashayana": [
            "Monastery",
            "Torii",
            "Pagoda",
            "Bodhimandala",
            "Tao Chang",
            "Dojo",
            "Dojang",
            "Xiudaoyuan",
        ],
        "Celestial Chorus": ["Chapel", "Covenant", "Sanctuary", "Adytum", "Temple"],
        "Cult of Ecstasy": ["Pleasuredome"],
        "Dreamspeakers": ["Lodge"],
        "Euthanatos": ["Marabout"],
        "Order of Hermes": ["Covenant", "Chantry"],
        "Hollow Ones": ["Hideout", "Hole", "Crashspace", "Haunt"],
        "Society of Ether": ["Laboratory"],
        "Verbena": ["Covenhouse", "Circle", "Great Hall"],
        "Virtual Adepts": ["Epicenter", "Fortress", "Net"],
        "Traditions": ["Chantry"],
        "Technocratic Union": ["Construct"],
        "Kopa Loei": ["He'iau"],
    }

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        self.save()
        return True

    def random_name(self):
        options = []
        current = self.faction
        while current is not None:
            if current.name in self.factional_names:
                options.extend(self.factional_names[current.name])
            current = current.parent
        if len(options) == 0:
            choice = "Chantry"
        else:
            choice = random.choice(options)
        adjective = Resonance.objects.order_by("?").first().name
        adjective = adjective.title()
        return self.set_name(f"{adjective} {choice}")

    def has_season(self):
        return self.season is not None

    def set_season(self, season):
        self.season = season
        self.save()
        return True

    def random_season(self):
        return self.set_season(random.choice(self.SEASONS)[0])

    def has_chantry_type(self):
        return self.chantry_type is not None

    def set_chantry_type(self, chantry_type):
        self.chantry_type = chantry_type
        self.save()
        return True

    def random_chantry_type(self):
        return self.set_chantry_type(random.choice(self.CHANTRY_TYPES)[0])

    def trait_cost(self, trait):
        if trait in [
            "allies",
            "arcane",
            "backup",
            "cult",
            "elders",
            "integrated_effects",
            "library_rating",
            "retainers",
            "spies",
        ]:
            return 2
        if trait in ["node_rating", "resources"]:
            return 3
        if trait in ["enhancement", "requisitions"]:
            return 4
        if trait in ["reality_zone_rating"]:
            return 5
        return 1000

    def points_spent(self):
        return (
            2
            * (
                self.allies
                + self.arcane
                + self.backup
                + self.cult
                + self.elders
                + self.integrated_effects
                + self.library_rating
                + self.retainers
                + self.spies
            )
            + 3 * (self.node_rating + self.resources)
            + 4 * (self.enhancement + self.requisitions)
            + 5 * (self.reality_zone_rating)
        )

    def has_node(self):
        return self.total_node() == self.node_rating

    def add_node(self, node):
        self.nodes.add(node)
        self.save()

    def create_nodes(self):
        node_ranks = []
        while sum(node_ranks) < self.node_rating:
            x = random.randint(1, min(5, self.node_rating - sum(node_ranks)))
            node_ranks.append(x)

        for i, rank in enumerate(node_ranks):
            n = Node.objects.create(name=f"{self.name}'s Node {i}", parent=self)
            n.random(rank=rank)
            n.save()
            self.add_node(n)

    def total_node(self):
        return sum(x.rank for x in self.nodes.all())

    def has_library(self):
        if self.library is not None:
            return self.library.rank == self.library.num_books()
        return False

    def set_library(self, library):
        self.library = library
        return True

    def create_library(self):
        l, _ = Library.objects.get_or_create(name=f"{self.name} Library")
        l.rank = self.library_rating
        while l.num_books() < l.rank:
            l.random_book()
        self.set_library(l)

    def random_points(self, rank=None):
        if rank is None:
            rank = self.rank
        if rank == 1:
            self.points = random.randint(10, 20)
        if rank == 2:
            self.points = random.randint(21, 30)
        if rank == 3:
            self.points = random.randint(31, 70)
        if rank == 4:
            self.points = random.randint(71, 100)
        if rank == 5:
            self.points = random.randint(101, 200)

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        self.set_rank(rank)

    def set_rank(self, rank):
        self.rank = rank
        self.random_points(rank=rank)
        return True

    def random(self, rank=None):
        self.random_faction()
        self.random_name()
        self.random_season()
        self.random_chantry_type()
        self.random_rank(rank=rank)
        while self.points - self.points_spent() > 1:
            choice = weighted_choice(self.get_traits())
            if self.trait_cost(choice) <= self.points - self.points_spent():
                if choice != "node_rating":
                    add_dot(self, choice, maximum=10)
                else:
                    add_dot(self, choice, maximum=100)
        self.create_nodes()
        self.create_library()

    def get_traits(self):
        return {
            "allies": self.allies,
            "arcane": self.arcane,
            "backup": self.backup,
            "cult": self.cult,
            "elders": self.elders,
            "integrated_effects": self.integrated_effects,
            "retainers": self.retainers,
            "spies": self.spies,
            "resources": self.resources,
            "enhancement": self.enhancement,
            "requisitions": self.requisitions,
            "reality_zone": self.reality_zone_rating,
            "node_rating": self.node_rating,
            "library_rating": self.library_rating,
        }

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def random_faction(self):
        return self.set_faction(MageFaction.objects.order_by("?").first())


class Sector(Location):
    type = "sector"
    
    SECTOR_CLASS = [
        ("virgin", "Virgin Web"),
        ("grid", "Grid"),
        ("formatted", "Formatted Web"),
        ("corrupted", "Corrupted Web"),
        ("junklands", "Junklands"),
        ("haunts", "Haunts"),
        ("trash", "Trash"),
        ("streamland", "Streamland"),
    ]

    sector_class = models.CharField(max_length=10, choices=SECTOR_CLASS, default="")
    constraints = models.TextField(default="")
