from attr import attr, attrib
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

    powers = models.ManyToManyField("Power", blank=True)
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
        pass

    def total_powers(self):
        return -100

    def random_power(self):
        pass

    def get_tags(self, power):
        return []

    def add_tag(self, power, tag):
        pass

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
        return []

    def add_transformation(self, transformation):
        pass

    def filter_transformations(self):
        return []

    def add_transcendence(self, transformation=False):
        return add_dot(self, "transcendence", 10)

    def add_quantum(self):
        output = add_dot(self, "quantum", 10)
        if self.quantum >= 4 and output:
            self.add_transcendence()
        self.update_quantum_points()
        return output

    def update_quantum_points(self):
        self.quantum_points = 10 + 5 * self.quantum

        # self.fail("Quantum of 1")
        # self.fail("One dot in favored approach")
        # self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
        # self.fail("150 XP")
        # self.fail("Check spend_xp?")

    def apply_random_template(self):
        pass

    # TODO: Random XP Spend extension


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
