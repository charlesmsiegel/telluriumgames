import random

from django.db import models

from core.utils import add_dot, weighted_choice
from tc.models.character.human import Edge, Human


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

    def filter_mega_edges(self):
        mega_edges = MegaEdge.objects.all()
        mega_edges = [x for x in mega_edges if x.check_prereqs(self)]
        output = []
        for me in mega_edges:
            if me in self.mega_edges.all():
                me_rating = MegaEdgeRating.objects.get(character=self, mega_edge=me)
                if me_rating.rating < max(me.ratings):
                    output.append(me)
            else:
                output.append(me)
        return output

    def random_mega_edge(self, dots=100):
        pass

    def random_mega_edges(self):
        pass

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
        pass

    def get_tags(self, power):
        return []

    def add_tag(self, power, tag):
        if power not in self.powers.all():
            return False
        if power not in tag.permitted_powers.all():
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
        pass

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

    def add_transformation(self, transformation):
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
        else:
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

    def apply_random_template(self):
        self.quantum = 1

        approaches = {
            "FOR": self.get_force_attributes(),
            "FIN": self.get_finesse_attributes(),
            "RES": self.get_resilience_attributes(),
        }

        while not self.add_attribute(weighted_choice(approaches[self.approach]), 5):
            pass

        if random.random() < 0.5:
            e = Edge.objects.get(name="Fame")
        else:
            e = Edge.objects.get(name="Alternate Identity")
        self.add_edge(e)
        self.xp = 150

    # TODO: Random XP Spend extension

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
                satisfied = satisfied and (character.quantum >= prereq[1])
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
