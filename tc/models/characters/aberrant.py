import random

from django.db import models
from django.db.models import F, Q
from django.shortcuts import reverse

from core.models import Model
from core.utils import add_dot, weighted_choice
from tc.models.characters.human import Edge, EnhancedEdge, Human, PathRating, TCPath


# Create your models here.
class Aberrant(Human):
    type = "aberrant"

    mega_intellect = models.IntegerField(default=0)
    mega_cunning = models.IntegerField(default=0)
    mega_resolve = models.IntegerField(default=0)
    mega_might = models.IntegerField(default=0)
    mega_dexterity = models.IntegerField(default=0)
    mega_stamina = models.IntegerField(default=0)
    mega_presence = models.IntegerField(default=0)
    mega_manipulation = models.IntegerField(default=0)
    mega_composure = models.IntegerField(default=0)

    mega_composure_flag = models.BooleanField(default=False)

    powers = models.ManyToManyField("Power", blank=True, through="PowerRating")
    mega_edges = models.ManyToManyField(
        "MegaEdge", blank=True, through="MegaEdgeRating"
    )

    transcendence = models.IntegerField(default=0)
    transformations = models.ManyToManyField("Transformation", blank=True)

    quantum = models.IntegerField(default=1)
    quantum_points = models.IntegerField(default=5)
    flux = models.IntegerField(default=0)

    transformations_for_xp = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Aberrant"
        verbose_name_plural = "Aberrants"

    def get_update_url(self):
        return reverse("tc:characters:aberrant:update_aberrant", kwargs={"pk": self.pk})

    def get_heading(self):
        return "tc_aberrant_heading"

    def add_mega_attribute(self, attribute):
        if not attribute.startswith("mega_"):
            mega_attribute = "mega_" + attribute
        else:
            mega_attribute = attribute
            attribute = attribute[5:]
        if getattr(self, attribute) < 5:
            limit = min(getattr(self, attribute), self.quantum)
        else:
            limit = self.quantum

        if add_dot(self, mega_attribute, limit):
            if attribute == "intellect":
                self.random_edge(
                    dots=1,
                    sublist=[
                        Edge.objects.get(name=x)
                        for x in [
                            "Iron Will",
                            "Lightning Calculator",
                            "Photographic Memory",
                            "Speed Reading",
                        ]
                    ],
                )
            if attribute == "cunning":
                edges = Edge.objects.filter(name__icontains="Keen Sense")
                for edge in edges:
                    if edge not in self.edges.all():
                        self.add_edge(edge)
            if attribute == "manipulation":
                self.random_edge(
                    dots=1,
                    sublist=[
                        Edge.objects.get(name=x)
                        for x in ["Animal Ken", "Skilled Liar", "Striking", "Wealth"]
                    ],
                )
            if attribute == "composure":
                if self.edge_rating("Iron Will") == 3:
                    if self.mega_composure_flag:
                        self.enhanced_edges.add(
                            EnhancedEdge.objects.get(name="Indomitable")
                        )
                    else:
                        self.mega_composure_flag = True
                else:
                    self.random_edge(
                        dots=1,
                        sublist=[
                            Edge.objects.get(name=x)
                            for x in [
                                "Always Prepared",
                                "Covert",
                                "Danger Sense",
                                "Iron Will",
                            ]
                        ],
                    )
            return True
        return False

    def filter_mega_attributes(self):
        attributes = self.get_attributes()
        mega_attributes = self.get_mega_attributes()
        limits = {}
        for att in attributes:
            if getattr(self, att) < 5:
                limit = min(getattr(self, att), self.quantum)
            else:
                limit = self.quantum
            limits[att] = limit
        return {k: v for k, v in mega_attributes.items() if v < limits[k[5:]]}

    def get_mega_attributes(self):
        return {
            "mega_intellect": self.mega_intellect,
            "mega_cunning": self.mega_cunning,
            "mega_resolve": self.mega_resolve,
            "mega_might": self.mega_might,
            "mega_dexterity": self.mega_dexterity,
            "mega_stamina": self.mega_stamina,
            "mega_presence": self.mega_presence,
            "mega_manipulation": self.mega_manipulation,
            "mega_composure": self.mega_composure,
        }

    def random_mega_attribute(self):
        return add_dot(
            self, weighted_choice(self.filter_mega_attributes()), self.quantum
        )

    def total_mega_attributes(self):
        return sum(self.get_mega_attributes().values())

    def add_mega_edge(self, mega_edge):
        if mega_edge.check_prereqs(self):
            if mega_edge in self.mega_edges.all():
                mega_edge_rating = MegaEdgeRating.objects.get(
                    character=self, mega_edge=mega_edge
                )
                current_rating = mega_edge_rating.rating
                values = [x for x in mega_edge.ratings if x > current_rating]
                if len(values) != 0:
                    mega_edge_rating.rating = min(values)
                    mega_edge_rating.save()
                    return True
                return False
            MegaEdgeRating.objects.create(
                character=self, mega_edge=mega_edge, rating=min(mega_edge.ratings)
            )
            return True
        return False

    def total_mega_edges(self):
        return sum(x.rating for x in MegaEdgeRating.objects.filter(character=self))

    def filter_mega_edges(self, dots=100):
        mega_edges = MegaEdge.objects.all()
        mega_edges = [x for x in mega_edges if x.check_prereqs(self)]
        mega_edges = [
            x for x in mega_edges if len([y for y in x.ratings if y <= dots]) != 0
        ]
        output = []
        for me in mega_edges:
            if me in self.mega_edges.all():
                me_rating = MegaEdgeRating.objects.get(character=self, mega_edge=me)
                if me_rating.rating < me.max_rating:
                    if (
                        min(x for x in me.ratings if x > me_rating.rating)
                        - me_rating.rating
                        <= dots
                    ):
                        output.append(me)
            else:
                output.append(me)
        return output

    def mega_edge_rating(self, m):
        if m not in self.mega_edges.all():
            return 0
        mr = MegaEdgeRating.objects.get(character=self, mega_edge=m)
        return mr.rating

    def random_mega_edge(self, dots=100):
        possible_mes = self.filter_mega_edges(dots=dots)
        me = random.choice(possible_mes)
        return self.add_mega_edge(me)

    def add_power(self, power):
        p, _ = PowerRating.objects.get_or_create(character=self, power=power)
        if self.quantum >= p.minimum_quantum_for_next_dot():
            p.rating += 1
            if power.name == "Cloak" and p.rating > 1:
                possible_tags = power.tag_set.exclude(pk__in=p.tags.all())
                possible_tags = [x for x in possible_tags if x.ratings == [1]]
                tag = random.choice(possible_tags)
                self.add_tag(power, tag)
            if power.name == "Quantum Construct" and p.rating > 1:
                possible_tags = Tag.objects.filter(
                    name__in=[
                        "Durability",
                        "Invisibility",
                        "Multiple",
                        "Ranged",
                        "Selective",
                        "Size",
                    ]
                ).exclude(pk__in=p.tags.all())
                tag = random.choice(possible_tags)
                self.add_tag(power, tag)
            p.save()
            return True
        return False

    def total_powers(self):
        return sum(x.rating for x in PowerRating.objects.filter(character=self))

    def random_power(self):
        powers = Power.objects.filter(quantum_minimum__lte=self.quantum)
        if random.random() < 0.7 and self.powers.count() != 0:
            powers = self.powers.all()
        else:
            powers = powers.exclude(pk__in=self.powers.all())
        choice = random.choice(powers)
        return self.add_power(choice)

    def power_rating(self, p):
        if p not in self.powers.all():
            return 0
        return PowerRating.objects.get(character=self, power=p).rating

    def get_tags(self, power):
        if power in self.powers.all():
            p = PowerRating.objects.get(power=power, character=self)
            return p.tags.all()
        return []

    def add_tag(self, power, tag):
        if tag.name == "Multiple":
            if self.tag_rating(power, tag) >= self.power_rating(power):
                return False
        if power not in self.powers.all():
            return False
        if power not in tag.permitted_powers.all():
            return False
        if self.power_cost(power) == 0 and tag.name == "Reduced Cost":
            return False
        p = PowerRating.objects.get(character=self, power=power)
        t, _ = TagRating.objects.get_or_create(power_rating=p, tag=tag)
        r = t.rating
        if r == tag.max_rating:
            return False
        new_rating = min(x for x in tag.ratings if x > r)
        t.rating = new_rating
        t.save()
        return True

    def random_tag(self, power):
        if power not in self.powers.all():
            return False
        possible_tags = self.filter_tags(power)
        return self.add_tag(power, random.choice(possible_tags))

    def tag_rating(self, power, tag):
        if power not in self.powers.all():
            return 0
        p = PowerRating.objects.get(power=power, character=self)
        if tag not in p.tags.all():
            return 0
        t = TagRating.objects.get(power_rating=p, tag=tag)
        return t.rating

    def filter_tags(self, power):
        if power not in self.powers.all():
            return []
        tags = Tag.objects.filter(permitted_powers__id=power.id)

        p = PowerRating.objects.get(character=self, power=power)

        had_tags = (
            TagRating.objects.filter(power_rating=p)
            .exclude(rating=F("tag__max_rating"))
            .values_list("tag", flat=True)
        )
        had_tags = Tag.objects.filter(pk__in=had_tags)
        new_tags = tags.exclude(pk__in=p.tags.all())
        return had_tags | new_tags

    def add_transformation(self, transformation, transcendence=False):
        if transformation not in self.transformations.all():
            self.transformations.add(transformation)
            return True
        return False

    def random_transformation(self, level=None):
        t = self.filter_transformations(level=level).order_by("?").first()
        return self.add_transformation(t)

    def filter_transformations(self, level=None):
        transforms = Transformation.objects.exclude(pk__in=self.transformations.all())
        if level is not None:
            transforms = transforms.filter(level=level)
        return transforms

    def add_transcendence(self, transformation=None):
        if transformation is None:
            out = add_dot(self, "transcendence", 10)
            if out:
                if self.transcendence in [4, 5]:
                    self.random_transformation(level="low")
                if self.transcendence in [6, 7]:
                    self.random_transformation(level="medium")
                if self.transcendence in [8, 9]:
                    self.random_transformation(level="high")
                return True
            return False
        if add_dot(self, "transcendence", 10):
            self.add_transformation(transformation)
            return True
        return False

    def add_quantum(
        self, start=True, transformation=None, transcendence_transformation=None
    ):
        if start:
            output = add_dot(self, "quantum", 5)
        else:
            output = add_dot(self, "quantum", 10)
        if self.quantum >= 4 and output:
            self.add_transcendence(transformation=transcendence_transformation)
        if transformation is not None:
            self.transformations.add(transformation)
        self.update_quantum_points()
        return output

    def update_quantum_points(self):
        self.quantum_points = 10 + 5 * self.quantum

    def add_flux(self):
        return add_dot(self, "flux", maximum=10)

    def reset_flux(self):
        self.flux = 0
        return True

    def power_cost(self, power):
        if Tag.objects.filter(name="Reduced Cost").exists():
            return max(
                0,
                power.cost
                - self.tag_rating(power, Tag.objects.get(name="Reduced Cost")),
            )
        return power.cost

    def apply_random_template(self):
        self.quantum = 1

        approaches = {
            "FOR": self.get_force_attributes(),
            "FIN": self.get_finesse_attributes(),
            "RES": self.get_resilience_attributes(),
        }

        total = self.total_attributes()
        while self.total_attributes() < total + 1:
            self.add_attribute(weighted_choice(approaches[self.approach]), 5)

        if random.random() < 0.5:
            e = Edge.objects.get(name="Fame")
        else:
            e = Edge.objects.get(name="Alternate Identity")
        self.add_edge(e)
        self.xp = 150

    def has_template(self, xp=150):
        attributes_flag = self.total_attributes() == 25
        edges_flag = ("Fame" in [x.name for x in self.edges.all()]) or (
            "Alternate Identity" in [x.name for x in self.edges.all()]
        )
        xp_flag = self.xp == xp
        quantum_flag = self.quantum == 1
        return attributes_flag and edges_flag and xp_flag and quantum_flag

    def random_spend_xp(self):
        while self.xp > 10:
            options = {
                "attributes": 1,
                "edges": 1,
                "enhanced_edges": 1,
                "skills": 1,
                "tricks": 1,
                "specialties": 1,
                "paths": 1,
                "approach": 1,
                "mega attribute": 1,
                "mega edge": 1,
                "quantum power": 1,
                "power tag": 1,
                "quantum": 1,
            }
            trait_type = weighted_choice(options)
            p = None
            if trait_type == "attributes":
                trait = weighted_choice(self.filter_attributes(maximum=4))
            elif trait_type == "edges":
                trait = random.choice(self.filter_edges()).name
            elif trait_type == "enhanced_edges":
                ees = self.filter_enhanced_edges()
                if len(ees) > 0:
                    trait = random.choice(ees).name
                else:
                    trait = None
            elif trait_type == "skills":
                trait = weighted_choice(self.filter_skills(maximum=4))
            elif trait_type == "tricks":
                trait = random.choice(self.filter_tricks()).name
            elif trait_type == "specialties":
                trait = random.choice(self.filter_specialties()).name
            elif trait_type == "paths":
                trait = weighted_choice(
                    {p.name: self.path_rating(p) for p in TCPath.objects.all()}
                )
            elif trait_type == "approach":
                trait = random.choice(["Favor FIN", "Favor FOR", "Favor RES"])
            elif trait_type == "mega attribute":
                trait = weighted_choice(self.filter_mega_attributes())
            elif trait_type == "mega edge":
                trait = random.choice(self.filter_mega_edges()).name
            elif trait_type == "power tag":
                if self.powers.all().exists():
                    p = self.powers.order_by("?").first()
                    trait = random.choice(self.filter_tags(power=p))
                else:
                    trait = None
            elif trait_type == "quantum":
                trait = "quantum"
            elif trait_type == "quantum power":
                trait = weighted_choice(
                    {power: self.power_rating(power) for power in Power.objects.all()}
                ).name
            else:
                trait = None
            self.spend_xp(trait, power=p)

    def xp_cost(self, trait_type, transcendence=False, transformation=None):
        cost = super().xp_cost(trait_type)
        if cost == 10000:
            if trait_type == "mega attribute":
                cost = 12
            elif trait_type == "mega edge":
                cost = 12
            elif trait_type == "power tag":
                cost = 12
            elif trait_type == "quantum<=5":
                cost = 16
            elif trait_type == "quantum>5":
                cost = 32
            elif trait_type == "quantum power":
                cost = 12
        if transcendence and trait_type in [
            "mega attribute",
            "mega edge",
            "quantum power",
        ]:
            cost -= 6
        if (
            trait_type
            in [
                "mega attribute",
                "mega edge",
                "power tag",
                "quantum<=5",
                "quantum>5",
                "quantum power",
            ]
            and self.transformations_for_xp < self.quantum * 2
        ):
            if transformation == "low":
                cost -= 3
            if transformation == "medium":
                cost -= 6
        return cost

    def spend_xp_mega_attribute(self, trait, transcendence, transformation):
        cost = self.xp_cost(
            "mega attribute", transcendence=transcendence, transformation=transformation
        )
        if self.xp >= cost:
            if self.add_mega_attribute(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                if (
                    transformation is not None
                    and self.transformations_for_xp < self.quantum * 2
                ):
                    self.transformations_for_xp += 1
                    self.random_transformation(level=transformation)
                if transcendence:
                    self.add_transcendence()
                return True
            return False
        return False

    def spend_xp_mega_edge(self, trait, transcendence, transformation):
        e = MegaEdge.objects.get(name=trait)
        new_rating = min(x for x in e.ratings if x > self.mega_edge_rating(e))
        cost = self.xp_cost(
            "mega edge", transcendence=transcendence, transformation=transformation
        ) * (new_rating - self.mega_edge_rating(e))
        if self.xp >= cost:
            if self.add_mega_edge(e):
                self.xp -= cost
                self.add_to_spend(trait, self.mega_edge_rating(e), cost)
                if (
                    transformation is not None
                    and self.transformations_for_xp < self.quantum * 2
                ):
                    self.transformations_for_xp += 1
                    self.random_transformation(level=transformation)
                if transcendence:
                    self.add_transcendence()
                return True
            return False
        return False

    def spend_xp_power(self, trait, transcendence, transformation):
        e = Power.objects.get(name=trait)
        cost = self.xp_cost(
            "quantum power", transcendence=transcendence, transformation=transformation
        )
        if self.xp >= cost:
            if self.add_power(e):
                self.xp -= cost
                self.add_to_spend(trait, self.power_rating(e), cost)
                if (
                    transformation is not None
                    and self.transformations_for_xp < self.quantum * 2
                ):
                    self.transformations_for_xp += 1
                    self.random_transformation(level=transformation)
                if transcendence:
                    self.add_transcendence()
                return True
            return False
        return False

    def spend_xp_tag(self, trait, power, transcendence, transformation):
        if power is None:
            return False
        if not isinstance(power, Power):
            power = Power.objects.get(name=power)
        if power not in self.powers.all():
            return False
        t = Tag.objects.get(name=trait)
        if power not in t.permitted_powers.all():
            return False
        new_rating = min(x for x in t.ratings if x > self.tag_rating(power, t))
        cost = self.xp_cost(
            "power tag", transcendence=transcendence, transformation=transformation
        ) * (new_rating - self.tag_rating(power, t))
        if self.xp >= cost:
            if self.add_tag(power, t):
                self.xp -= cost
                self.add_to_spend(trait, self.tag_rating(power, t), cost)
                if (
                    transformation is not None
                    and self.transformations_for_xp < self.quantum * 2
                ):
                    self.transformations_for_xp += 1
                    self.random_transformation(level=transformation)
                return True
            return False
        return False

    def spend_xp_quantum(self, trait, transcendence, transformation, creation):
        if self.quantum <= 4:
            cost = self.xp_cost(
                "quantum<=5", transcendence=transcendence, transformation=transformation
            )
        else:
            cost = self.xp_cost(
                "quantum>5", transcendence=transcendence, transformation=transformation
            )
        if self.xp >= cost:
            if self.add_quantum(start=creation):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                if (
                    transformation is not None
                    and self.transformations_for_xp < self.quantum * 2
                ):
                    self.transformations_for_xp += 1
                    self.random_transformation(level=transformation)
                return True
            return False
        return False

    def spend_xp(
        self,
        trait,
        power=None,
        creation=False,
        transcendence=False,
        transformation=None,
    ):
        if trait in self.get_mega_attributes():
            return self.spend_xp_mega_attribute(trait, transcendence, transformation)
        if trait in [x.name for x in MegaEdge.objects.all()]:
            return self.spend_xp_mega_edge(trait, transcendence, transformation)
        if trait in [x.name for x in Power.objects.all()]:
            return self.spend_xp_power(trait, transcendence, transformation)
        if trait in [x.name for x in Tag.objects.all()]:
            return self.spend_xp_tag(trait, power, transcendence, transformation)
        if trait == "quantum":
            return self.spend_xp_quantum(trait, transcendence, transformation, creation)
        if super().spend_xp(trait):
            return True
        self.save()
        return False


class MegaEdge(Edge):
    type = "mega_edge"

    class Meta:
        verbose_name = "Mega Edge"
        verbose_name_plural = "Mega Edges"

    def get_update_url(self):
        return reverse(
            "tc:characters:aberrant:update_mega_edge", kwargs={"pk": self.pk}
        )

    def prereq_satisfied(self, prereq, character):
        if prereq[0] in character.get_attributes().keys():
            return getattr(character, prereq[0]) >= prereq[1]
        if prereq[0] in character.get_skills().keys():
            return getattr(character, prereq[0]) >= prereq[1]
        if Edge.objects.filter(name=prereq[0]).exists():
            edge_prereq = Edge.objects.get(name=prereq[0])
            if edge_prereq.type == "edge":
                return character.edge_rating(edge_prereq) >= prereq[1]
        if MegaEdge.objects.filter(name=prereq[0]).exists():
            edge_prereq = MegaEdge.objects.get(name=prereq[0])
            if edge_prereq.type == "mega_edge":
                return character.mega_edge_rating(edge_prereq) >= prereq[1]
        if prereq[0] == "path":
            if self in Edge.objects.all():
                any(
                    x.rating > prereq[1]
                    for x in PathRating.objects.filter(character=character)
                    if self in x.path.edges.all()
                )
        if prereq[0] == "quantum":
            if prereq[1] == "dots":
                if self in MegaEdge.objects.all():
                    r = character.mega_edge_rating(self)
                    req = min(x for x in self.ratings if x > r)
                    return character.quantum >= req
                return character.quantum >= prereq[1]
        if prereq[0] in character.get_mega_attributes().keys():
            return getattr(character, prereq[0]) >= prereq[1]
        return False


class MegaEdgeRating(models.Model):
    mega_edge = models.ForeignKey(
        MegaEdge, on_delete=models.CASCADE, blank=True, null=True
    )
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Mega Edge Rating"
        verbose_name_plural = "Mega Edge Ratings"


class Power(Model):
    type = "power"

    quantum_minimum = models.IntegerField(default=0)
    quantum_offset = models.IntegerField(default=0)
    action_type = models.CharField(
        max_length=100, choices=[("reflexive", "Reflexive"), ("ordinary", "Ordinary"),],
    )
    cost = models.IntegerField(default=0)
    dicepool = models.CharField(default="", max_length=100)
    range = models.CharField(
        max_length=100,
        choices=[
            ("personal", "Personal"),
            ("close", "Close"),
            ("short", "Short"),
            ("medium", "Medium"),
            ("long", "Long"),
            ("extreme", "Extreme"),
            ("visual", "Visual"),
        ],
    )
    duration = models.CharField(
        max_length=100,
        choices=[
            ("instantaneous", "Instantaneous"),
            ("concentration", "Concentration"),
            ("maintained", "Maintained"),
            ("continuous", "Continuous"),
        ],
    )

    class Meta:
        verbose_name = "Power"
        verbose_name_plural = "Powers"

    def get_absolute_url(self):
        return reverse("tc:characters:aberrant:power", args=[str(self.id)])

    def get_update_url(self):
        return reverse("tc:characters:aberrant:update_power", kwargs={"pk": self.pk})

    def set_dicepool(self, dicepool):
        self.dicepool = dicepool
        return True

    def set_duration(self, duration):
        self.duration = duration
        return True

    def set_range(self, range):
        self.range = range
        return True

    def set_action_type(self, action_type):
        self.action_type = action_type
        return True

    def dicepool_traits(self):
        return self.dicepool.split("+")

    def num_dice(self, char):
        return sum(getattr(char, x) for x in self.dicepool_traits())

    def add_to_dicepool(self, trait):
        if self.dicepool != "":
            self.dicepool += "+"
        self.dicepool += trait
        return True


class PowerRating(models.Model):
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    power = models.ForeignKey(Power, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, through="TagRating")
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Power Rating"
        verbose_name_plural = "Power Ratings"

    def __str__(self):
        return f"{self.power.name}: {self.rating}"

    def minimum_quantum_for_next_dot(self):
        if self.power.quantum_minimum != -1:
            return self.power.quantum_minimum
        return self.rating + self.power.quantum_offset


class Tag(Model):
    type = "tag"

    ratings = models.JSONField(default=list)
    max_rating = models.IntegerField(default=0)
    permitted_powers = models.ManyToManyField(Power, blank=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def get_absolute_url(self):
        return reverse("tc:characters:tag", args=[str(self.id)])

    def get_update_url(self):
        return reverse("tc:characters:aberrant:update_tag", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        super().save(*args, **kwargs)


class TagRating(models.Model):
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE)
    power_rating = models.ForeignKey(
        PowerRating, blank=True, null=True, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Tag Rating"
        verbose_name_plural = "Tag Ratings"


class Transformation(Model):
    type = "transformation"

    level = models.CharField(
        max_length=10,
        choices=[("low", "low"), ("medium", "medium"), ("high", "high"),],
    )

    class Meta:
        verbose_name = "Transformation"
        verbose_name_plural = "Transformations"

    def get_absolute_url(self):
        return reverse("tc:characters:transformation", args=[str(self.id)])

    def get_update_url(self):
        return reverse(
            "tc:characters:aberrant:update_transformation", kwargs={"pk": self.pk}
        )

    def __str__(self):
        return f"{self.name} ({self.level})"
