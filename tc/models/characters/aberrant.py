import random

from django.db import models

from core.utils import add_dot, weighted_choice
from tc.models.characters.human import Edge, Human


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

    powers = models.ManyToManyField("Power", blank=True, through="PowerRating")
    mega_edges = models.ManyToManyField(
        "MegaEdge", blank=True, through="MegaEdgeRating"
    )

    transcendence = models.IntegerField(default=0)
    transformations = models.ManyToManyField("Transformation", blank=True)

    quantum = models.IntegerField(default=1)
    quantum_points = models.IntegerField(default=5)
    flux = models.IntegerField(default=0)

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
        return add_dot(self, mega_attribute, limit)

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
        return sum([x.rating for x in MegaEdgeRating.objects.filter(character=self)])

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
                if me_rating.rating < max(me.ratings):
                    if (
                        min([x for x in me.ratings if x > me_rating.rating])
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
        if self.quantum >= power.quantum_minimum:
            p.rating += 1
            p.save()
            return True
        return False

    def total_powers(self):
        return sum([x.rating for x in PowerRating.objects.filter(character=self)])

    def random_power(self):
        d = {x.name: self.power_rating(x) for x in Power.objects.all()}
        choice = weighted_choice(d)
        return self.add_power(Power.objects.get(name=choice))

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
        if power not in self.powers.all():
            return False
        if power not in tag.permitted_powers.all():
            return False
        if self.power_cost(power) == 0 and tag.name == "Reduced Cost":
            return False
        p = PowerRating.objects.get(character=self, power=power)
        t, _ = TagRating.objects.get_or_create(power_rating=p, tag=tag)
        r = t.rating
        if r == max(tag.ratings):
            return False
        new_rating = min([x for x in tag.ratings if x > r])
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
        tags = [x for x in Tag.objects.all() if power in x.permitted_powers.all()]
        p = PowerRating.objects.get(character=self, power=power)
        output = []
        for tag in tags:
            if tag not in p.tags.all():
                output.append(tag)
            else:
                if TagRating.objects.get(power_rating=p, tag=tag).rating != max(
                    tag.ratings
                ):
                    output.append(tag)
        return output

    def add_transformation(self, transformation, transcendence=False):
        # TODO: write a test to connect the transcedence KWARG to everything else
        if not transcendence:
            if self.transformations.count() == 2 * self.quantum:
                return False
        if transformation not in self.transformations.all():
            self.transformations.add(transformation)
            return True
        return False

    def random_transformation(self, level=None):
        transforms = self.filter_transformations(level=level)
        t = random.choice(transforms)
        return self.add_transformation(t)

    def filter_transformations(self, level=None):
        transforms = Transformation.objects.all()
        if level is not None:
            transforms = [x for x in transforms if x.level == level]
        return [x for x in transforms if x not in self.transformations.all()]

    def add_transcendence(self, transformation=None):
        if transformation is None:
            out = add_dot(self, "transcendence", 10)
            if out:
                if self.transcendence in [4, 5]:
                    self.random_transformation(level="low")
                if self.transcendence in [6, 7]:
                    self.random_transformation(level="med")
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
        # TODO: Random XP Spend extension
        pass

    def xp_cost(self, trait_type, transcendence=False):
        cost = super().xp_cost(trait_type)
        if cost != 10000:
            return cost
        if trait_type == "mega attribute":
            if transcendence:
                return 6
            return 12
        if trait_type == "mega edge":
            if transcendence:
                return 6
            return 12
        if trait_type == "power tag":
            return 12
        if trait_type == "quantum<=5":
            return 16
        if trait_type == "quantum>5":
            return 32
        if trait_type == "quantum power":
            if transcendence:
                return 6
            return 12
        return 10000

    def spend_xp(self, trait, power=None, creation=False, transcendence=False):
        if trait in self.get_mega_attributes():
            cost = self.xp_cost("mega attribute", transcendence=transcendence)
            if self.xp >= cost:
                if self.add_mega_attribute(trait):
                    self.xp -= cost
                    return True
        elif trait in [x.name for x in MegaEdge.objects.all()]:
            e = MegaEdge.objects.get(name=trait)
            new_rating = min([x for x in e.ratings if x > self.mega_edge_rating(e)])
            cost = self.xp_cost("mega edge", transcendence=transcendence) * (
                new_rating - self.mega_edge_rating(e)
            )
            if self.xp >= cost:
                if self.add_mega_edge(e):
                    self.xp -= cost
                    return True
        elif trait in [x.name for x in Power.objects.all()]:
            e = Power.objects.get(name=trait)
            cost = self.xp_cost("quantum power", transcendence=transcendence)
            if self.xp >= cost:
                if self.add_power(e):
                    self.xp -= cost
                    return True
        elif trait in [x.name for x in Tag.objects.all()]:
            if power is None:
                return False
            if not isinstance(power, Power):
                power = Power.objects.get(name=power)
            if power not in self.powers.all():
                return False
            t = Tag.objects.get(name=trait)
            if power not in t.permitted_powers.all():
                return False
            new_rating = min([x for x in t.ratings if x > self.tag_rating(power, t)])
            cost = self.xp_cost("power tag") * (new_rating - self.tag_rating(power, t))
            if self.xp >= cost:
                if self.add_tag(power, t):
                    self.xp -= cost
                    return True
        elif trait == "quantum":
            if self.quantum <= 4:
                cost = self.xp_cost("quantum<=5")
            else:
                cost = self.xp_cost("quantum>5")
            if self.xp >= cost:
                if self.add_quantum(start=creation):
                    self.xp -= cost
                    return True
        elif super().spend_xp(trait):
            return True
        self.save()
        return False


class MegaEdge(Edge):
    type = "mega_edge"

    def check_prereqs(self, character):
        satisfied = super().check_prereqs(character)
        for prereq in self.prereqs:
            if prereq[0] in [
                x.name for x in MegaEdge.objects.all() if x.type == "mega_edge"
            ]:
                mega_edge_prereq = MegaEdge.objects.get(name=prereq[0])
                if mega_edge_prereq in character.mega_edges.all():
                    x = MegaEdgeRating.objects.get(
                        character=character, mega_edge=mega_edge_prereq
                    )
                    satisfied = satisfied and (x.rating >= prereq[1])
                else:
                    satisfied = False
            elif prereq[0] == "quantum":
                if prereq[1] == "dots":
                    r = character.mega_edge_rating(self)
                    req = min([x for x in self.ratings if x > r])
                    satisfied = satisfied and (character.quantum >= req)
                else:
                    satisfied = satisfied and (character.quantum >= prereq[1])
            elif prereq[0] in character.get_mega_attributes().keys():
                satisfied = satisfied and (getattr(character, prereq[0]) >= prereq[1])
        return satisfied


class MegaEdgeRating(models.Model):
    mega_edge = models.ForeignKey(
        MegaEdge, on_delete=models.CASCADE, blank=True, null=True
    )
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)


class Power(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantum_minimum = models.IntegerField(default=0)
    action_type = models.CharField(
        max_length=100, choices=[("reflexive", "Reflexive"), ("ordinary", "Ordinary"),]
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

    def set_dicepool(self, dicepool):
        self.dicepool = dicepool
        return True

    def set_action_type(self, action_type):
        self.action_type = action_type
        return True

    def dicepool_traits(self):
        return self.dicepool.split("+")

    def num_dice(self, char):
        return sum([getattr(char, x) for x in self.dicepool_traits()])

    def add_to_dicepool(self, trait):
        if self.dicepool != "":
            self.dicepool += "+"
        self.dicepool += trait
        return True

    def __str__(self):
        return self.name


class PowerRating(models.Model):
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    power = models.ForeignKey(Power, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", blank=True, through="TagRating")
    rating = models.IntegerField(default=0)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)
    permitted_powers = models.ManyToManyField(Power, blank=True)

    def __str__(self):
        return self.name


class TagRating(models.Model):
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE)
    power_rating = models.ForeignKey(
        PowerRating, blank=True, null=True, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)


class Transformation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.CharField(
        max_length=4, choices=[("low", "low"), ("med", "medium"), ("high", "high"),],
    )

    def __str__(self):
        return f"{self.name} ({self.level})"
