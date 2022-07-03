import random

from django.db import models
from django.db.models import F, Q

from cod.models.characters.mortal import Mortal
from core.utils import add_dot, weighted_choice

# Create your models here.
ARCANA = [
    "space",
    "time",
    "death",
    "fate",
    "life",
    "matter",
    "forces",
    "prime",
    "mind",
    "spirit",
]


class Path(models.Model):
    name = models.CharField(max_length=100)
    ruling_arcana = models.JSONField(default=list)
    inferior_arcanum = models.CharField(
        max_length=10,
        choices=[
            ("death", "Death"),
            ("matter", "Matter"),
            ("life", "Life"),
            ("spirit", "Spirit"),
            ("time", "Time"),
            ("fate", "Fate"),
            ("mind", "Mind"),
            ("space", "Space"),
            ("prime", "Prime"),
            ("forces", "Forces"),
        ],
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    rote_skills = models.JSONField(default=list)

    def __str__(self):
        return self.name


class Legacy(models.Model):
    name = models.CharField(max_length=100)
    path = models.ForeignKey(Path, null=True, blank=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    ruling_arcanum = models.CharField(
        max_length=10,
        choices=[
            ("death", "Death"),
            ("matter", "Matter"),
            ("life", "Life"),
            ("spirit", "Spirit"),
            ("time", "Time"),
            ("fate", "Fate"),
            ("mind", "Mind"),
            ("space", "Space"),
            ("prime", "Prime"),
            ("forces", "Forces"),
        ],
    )
    is_left_handed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Rote(models.Model):
    name = models.CharField(max_length=100)
    practice = models.CharField(
        max_length=40,
        choices=[
            ("compelling", "Compelling"),
            ("knowing", "Knowing"),
            ("unveiling", "Unveiling"),
            ("ruling", "Ruling"),
            ("shielding", "Shielding"),
            ("veiling", "Veiling"),
            ("fraying", "Fraying"),
            ("perfecting", "Perfecting"),
            ("weaving", "Weaving"),
            ("patterning", "Patterning"),
            ("unraveling", "Unraveling"),
            ("making", "Making"),
            ("unmaking", "Unmaking"),
        ],
    )
    arcanum = models.CharField(
        max_length=10,
        choices=[
            ("death", "Death"),
            ("matter", "Matter"),
            ("life", "Life"),
            ("spirit", "Spirit"),
            ("time", "Time"),
            ("fate", "Fate"),
            ("mind", "Mind"),
            ("space", "Space"),
            ("prime", "Prime"),
            ("forces", "Forces"),
        ],
    )
    level = models.IntegerField(default=0)
    suggested_rote_skills = models.JSONField(default=list)
    primary_factor = models.CharField(
        default="",
        max_length=20,
        choices=[("duration", "Duration"), ("potency", "Potency"),],
    )
    withstand = models.CharField(default="", max_length=20)
    mana_cost = models.IntegerField(default=0)


class Mage(Mortal):
    type = "mage"

    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, blank=True, null=True, on_delete=models.CASCADE)
    legacy = models.ForeignKey(Legacy, blank=True, null=True, on_delete=models.CASCADE)

    rote_skills = models.JSONField(default=list)

    gnosis = models.IntegerField(default=0)

    death = models.IntegerField(default=0)
    matter = models.IntegerField(default=0)
    life = models.IntegerField(default=0)
    spirit = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    fate = models.IntegerField(default=0)
    mind = models.IntegerField(default=0)
    space = models.IntegerField(default=0)
    prime = models.IntegerField(default=0)
    forces = models.IntegerField(default=0)

    rotes = models.ManyToManyField(Rote, blank=True, through="KnownRote")

    wisdom = models.IntegerField(default=7)

    nimbus = models.TextField(default="")
    mana = models.IntegerField(default=0)

    @staticmethod
    def allowed_merit_types():
        return ["Mental", "Physical", "Social", "Mage", "Fighting"]

    def has_path(self):
        return self.path is not None

    def set_path(self, path):
        self.path = path
        self.save()
        return True

    def random_path(self):
        path = Path.objects.order_by("?").first()
        return self.set_path(path)

    def has_order(self):
        return self.order is not None

    def set_order(self, order):
        self.order = order
        self.rote_skills = self.order.rote_skills
        self.save()
        return True

    def random_order(self):
        order = Order.objects.order_by("?").first()
        return self.set_order(order)

    def has_rote_skills(self):
        return len(self.rote_skills) == 3

    def set_rote_skills(self, rote_skills):
        self.rote_skills = rote_skills
        return True

    def add_wisdom(self):
        return add_dot(self, "wisdom", maximum=10)

    def add_gnosis(self):
        return add_dot(self, "gnosis", maximum=10)

    def has_gnosis(self):
        return self.gnosis > 0

    def set_gnosis(self, gnosis):
        if gnosis < 1:
            return False
        if gnosis > 10:
            return False
        self.gnosis = gnosis
        self.save()
        return True

    def filter_arcana(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_arcana().items() if minimum <= v <= maximum}

    def get_arcana(self):
        return {
            "death": self.death,
            "matter": self.matter,
            "life": self.life,
            "spirit": self.spirit,
            "time": self.time,
            "fate": self.fate,
            "mind": self.mind,
            "space": self.space,
            "prime": self.prime,
            "forces": self.forces,
        }

    def has_arcana(self):
        nonzero_values = [x for x in self.get_arcana().values() if x != 0]
        nonzero_values.sort()
        nonzero_values.reverse()
        if nonzero_values not in [
            [3, 2, 1],
            [3, 1, 1, 1],
            [2, 2, 2],
            [2, 2, 1, 1],
            [2, 1, 1, 1, 1],
        ]:
            return False
        for ruling in self.path.ruling_arcana:
            if self.get_arcana()[ruling] == 0:
                return False
        if self.get_arcana()[self.path.inferior_arcanum] != 0:
            return False
        return True

    def total_arcana(self):
        return sum(v for k, v in self.get_arcana().items())

    def add_arcanum(self, arcanum):
        return add_dot(self, arcanum, maximum=5)

    def random_arcanum(self):
        arcana = self.get_arcana()
        choice = weighted_choice(arcana)
        return self.add_arcanum(choice)

    def random_arcana(self):
        distributions = [
            [3, 2, 1],
            [3, 1, 1, 1],
            [2, 2, 2],
            [2, 2, 1, 1],
            [2, 1, 1, 1, 1],
        ]
        distribution = random.choice(distributions)
        arcana = self.path.ruling_arcana
        options = [
            x for x in ARCANA if x not in arcana and x != self.path.inferior_arcanum
        ]
        while len(arcana) < len(distribution):
            choice = random.choice(options)
            arcana.append(choice)
            options = [x for x in options if x != choice]
        random.shuffle(arcana)
        for stat, value in zip(arcana, distribution):
            setattr(self, stat, value)
        return True

    def has_legacy(self):
        return self.legacy is not None

    def set_legacy(self, legacy):
        self.legacy = legacy
        self.save()
        return True

    def random_legacy(self):
        options = self.filter_legacies()
        choice = random.choice(options)
        return self.set_legacy(choice)

    def filter_legacies(self):
        possiblities = Legacy.objects.all()
        has_path = possiblities.filter(path=self.path)
        has_order = possiblities.filter(order=self.order)
        either = has_path | has_order
        either = either.distinct()

        return [x for x in either if getattr(self, x.ruling_arcanum) >= 2]

    def has_mana(self):
        return self.mana != 0

    def set_mana(self, mana):
        gnosis_mana_limits = {
            1: 10,
            2: 11,
            3: 12,
            4: 13,
            5: 15,
            6: 20,
            7: 25,
            8: 30,
            9: 50,
            10: 75,
        }
        if mana > gnosis_mana_limits[self.gnosis]:
            mana = gnosis_mana_limits[self.gnosis]
        if mana < 0:
            mana = 0
        self.mana = mana
        self.save()
        return True

    def has_rotes(self):
        return self.total_rotes() == 3

    def add_rote(self, rote):
        if getattr(self, rote.arcanum) >= rote.level:
            k = KnownRote.objects.create(mage=self, rote=rote)
            if len(rote.suggested_rote_skills) != 0:
                k.rote_skill = random.choice(rote.suggested_rote_skills)
            k.save()
            return True
        return False

    def total_rotes(self):
        return self.rotes.count()

    def random_rote(self):
        options = self.filter_rotes()
        choice = random.choice(options)
        return self.add_rote(choice)

    def random_rotes(self):
        while self.total_rotes() < 3:
            self.random_rote()
        return True

    def filter_rotes(self):
        arcana_dict = self.get_arcana()
        q = Q()
        for arcana, level in arcana_dict.items():
            q |= Q(arcanum=arcana, level__lte=level)
        allowed_rotes = Rote.objects.filter(q)
        return allowed_rotes.exclude(pk__in=self.rotes.all())

    def has_nimbus(self):
        return self.nimbus != ""

    def set_nimbus(self, nimbus):
        self.nimbus = nimbus
        return True

    def random_nimbus(self):
        return self.set_nimbus("Random")

    @staticmethod
    def practice_level(practice):
        if practice in ["compelling", "knowing", "unveiling"]:
            return 1
        if practice in ["ruling", "shielding", "veiling"]:
            return 2
        if practice in ["fraying", "perfecting", "weaving"]:
            return 3
        if practice in ["patterning", "unraveling"]:
            return 4
        if practice in ["making", "unmaking"]:
            return 5
        return 0

    @staticmethod
    def practices_at_level(level):
        if level == 1:
            return ["compelling", "knowing", "unveiling"]
        if level == 2:
            return ["ruling", "shielding", "veiling"]
        if level == 3:
            return ["fraying", "perfecting", "weaving"]
        if level == 4:
            return ["patterning", "unraveling"]
        if level == 5:
            return ["making", "unmaking"]
        return []

    def xp_cost(self, trait_type):
        cost = super().xp_cost(trait_type)
        if cost != 10000:
            return cost
        if trait_type == "arcanum (to limit)":
            return 4
        if trait_type == "arcanum (above limit)":
            return 5
        if trait_type == "gnosis":
            return 5
        if trait_type == "rote":
            return 1
        if trait_type == "praxis":
            return 1
        if trait_type == "wisdom":
            return 2
        if trait_type == "willpower":
            return 1
        if trait_type == "legacy attainment (tutored)":
            return 1
        if trait_type == "legacy attainment (untutored)":
            return 1
        return 10000

    def spend_xp(self, trait):
        if super().spend_xp(trait):
            return True
        if trait in ARCANA:
            return self.spend_xp_arcana(trait)
        if trait == "gnosis":
            return self.spend_xp_gnosis()
        if trait == "wisdom":
            return self.spend_xp_wisdom()
        if Rote.objects.filter(name=trait).exists():
            return self.spend_xp_rote(trait)
        if trait == "willpower":
            return self.spend_xp_willpower()
        if Legacy.objects.filter(name=trait).exists():
            return self.spend_xp_legacy(trait)
        return False

    def xp_frequencies(self):
        return {
            "attribute": 1,
            "merit": 1,
            "specialty": 1,
            "skill": 1,
            "wisdom": 1,
            "arcanum": 1,
            "gnosis": 1,
            "rote": 1,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "merit": self.random_xp_merit,
            "specialty": self.random_xp_specialty,
            "skill": self.random_xp_skill,
            "wisdom": self.random_xp_wisdom,
            "arcanum": self.random_xp_arcanum,
            "gnosis": self.random_xp_gnosis,
            "rote": self.random_xp_rote,
        }

    def random_xp_wisdom(self):
        return self.spend_xp_wisdom()

    def random_xp_arcanum(self):
        trait = weighted_choice(self.filter_arcana(maximum=4))
        return self.spend_xp_arcana(trait)

    def random_xp_gnosis(self):
        return self.spend_xp_gnosis()

    def random_xp_rote(self):
        options = self.filter_rotes()
        trait = random.choice(options).name
        return self.spend_xp_rote(trait)

    def spend_xp_arcana(self, trait):
        arcana = self.get_arcana()
        if self.gnosis == 1:
            highest = 3
            other = 2
        if self.gnosis == 2:
            highest = 3
            other = 3
        if self.gnosis == 3:
            highest = 4
            other = 3
        if self.gnosis == 4:
            highest = 4
            other = 4
        if self.gnosis == 5:
            highest = 5
            other = 4
        if self.gnosis >= 6:
            highest = 5
            other = 5
        if arcana[trait] < other:
            cost = self.xp_cost("arcanum (to limit)")
        else:
            if (
                arcana[trait] < highest
                and arcana[trait] == max(v for v in arcana.values())
                and len([k for k, v in arcana.items() if v == arcana[trait]]) == 1
            ):
                cost = self.xp_cost("arcanum (to limit)")
            else:
                cost = self.xp_cost("arcanum (above limit)")
        if cost <= self.xp:
            if self.add_arcanum(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                return True
            return False
        return False

    def spend_xp_rote(self, trait):
        cost = self.xp_cost("rote")
        if cost <= self.xp:
            r = Rote.objects.get(name=trait)
            if self.add_rote(r):
                self.xp -= cost
                self.add_to_spend(trait, r.level, cost)
                return True
            return False
        return False

    def spend_xp_gnosis(self):
        cost = self.xp_cost("gnosis")
        if cost <= self.xp:
            if self.add_gnosis():
                self.xp -= cost
                self.add_to_spend("gnosis", self.gnosis, cost)
                return True
            return False
        return False

    def spend_xp_wisdom(self):
        cost = self.xp_cost("wisdom")
        if cost <= self.xp:
            if self.add_wisdom():
                self.xp -= cost
                self.add_to_spend("wisdom", self.wisdom, cost)
                return True
            return False
        return False

    def random(self, xp=0):
        self.xp = xp
        self.random_basis()
        self.random_attributes()
        self.random_skills()
        self.random_specialties()
        self.random_path()
        self.random_order()
        self.random_nimbus()
        self.random_arcana()
        self.random_rotes()
        self.gnosis = 1
        self.set_mana(100)
        options = ["stamina", "resolve", "composure"]
        options = [x for x in options if getattr(self, x) < 5]
        choice = random.choice(options)
        self.add_attribute(choice)
        self.random_merits()
        self.assign_advantages()
        self.random_spend_xp()
        self.save()


class KnownRote(models.Model):
    mage = models.ForeignKey(Mage, on_delete=models.CASCADE)
    rote = models.ForeignKey(Rote, on_delete=models.CASCADE)
    rote_skill = models.CharField(default="", max_length=20, blank=True, null=True)
