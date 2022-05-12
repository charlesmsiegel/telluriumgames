import random

from django.db import models
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel

from wod.models.characters import Mage, Resonance


# Create your models here.
class Location(PolymorphicModel):
    """Class for locations"""

    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    description = models.TextField(blank=True)
    gauntlet = models.IntegerField(default=7)
    shroud = models.IntegerField(default=7)
    dimension_barrier = models.IntegerField(default=6)
    reality_zone = models.TextField(blank=True, null=True)

    type = "location"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:location", args=[str(self.id)])


class City(Location):
    """Class for cities"""

    population = models.IntegerField(default=0)
    mood = models.TextField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    mages = models.ManyToManyField(Mage, related_name="cities")
    media = models.TextField(blank=True, null=True)
    politicians = models.TextField(blank=True, null=True)

    type = "city"


class Node(Location):
    """Class for nodes"""

    resonance = models.ManyToManyField(Resonance, through="NodeResRating")
    merits_and_flaws = models.ManyToManyField(
        "NodeMeritFlaw", related_name="nodes", blank=True
    )
    rank = models.IntegerField(default=1)
    size = models.IntegerField(default=0)
    quintessence_per_week = models.IntegerField(default=1)
    tass_per_week = models.IntegerField(default=1)
    tass_form = models.TextField(default="")
    quintessence_form = models.TextField(default="")

    ratio_cost = 0
    size_names = [
        "household object",
        "small room",
        "average room",
        "small building",
        "large building",
    ]

    type = "node"

    def random_resonance(self):
        current_resonance = list(NodeResRating.objects.filter(node=self))
        current_resonance = [x for x in current_resonance if x.rating < 5]
        if len(current_resonance) == 0 or random.random() < 0.3:
            self.new_resonance_trait()
        else:
            self.add_resonance_dot()

    def random_rank(self, rank):
        if rank is not None:
            self.rank = rank
        else:
            self.rank = random.randint(1, 5)

    def new_resonance_trait(self):
        all_res = list(Resonance.objects.all())
        node_res = list(NodeResRating.objects.filter(node=self))
        res_ids = [x.resonance_id for x in node_res]
        res_traits = [Resonance.objects.get(pk=x) for x in res_ids]
        res_names = [x.name for x in res_traits]
        poss = [x for x in all_res if x.name not in res_names]
        resonance_choice = random.choice(poss)
        new_res = NodeResRating(node=self, resonance=resonance_choice, rating=1)
        new_res.save()

    def add_resonance_dot(self):
        possibilities = NodeResRating.objects.filter(node=self)
        possibilities = [x for x in possibilities if x.rating < 5]
        res = random.choice(possibilities)
        res.rating += 1
        res.save()

    def random_merits_and_flaws(self, points):
        node_mfs = NodeMeritFlaw.objects.filter(value__lte=points)
        current_mfs = [x.name for x in self.merits_and_flaws.all()]
        node_mfs = [x for x in node_mfs if x.name not in current_mfs]
        flaw_count = 0
        while (
            random.random() < 0.5
            and points > 1
            and flaw_count < 7
            and len(current_mfs) != 0
        ):
            new_mf = random.choice(node_mfs)
            if new_mf.value < 0:
                flaw_count -= new_mf.value
            points -= new_mf.value
            self.merits_and_flaws.add(new_mf)
            self.save()
            current_mfs = [x.name for x in self.merits_and_flaws.all()]
            node_mfs = [x for x in node_mfs if x.name not in current_mfs]
        return points

    def total_resonance(self):
        return sum([x.rating for x in NodeResRating.objects.filter(node=self)])

    def basic_description(self):
        if self.name:
            name = self.name
        else:
            name = "It"
        out_string = (
            f"{name} is a {self.rank}-point Node roughly the size of"
            f" a {self.size_names[self.size + 2]}.\nIt produces "
            f"{self.quintessence_per_week} quintessence and "
            f"{self.tass_per_week} tass per week.\n, and its quintessence takes the "
            f"form of {self.quintessence_form}. Its tass has "
            f"the form {self.tass_form}.\n"
        )
        merits = self.merits_and_flaws.filter(value__gte=0)
        flaws = self.merits_and_flaws.filter(value__lte=0)
        merits = ", ".join(merits)
        flaws = ", ".join(flaws)
        if merits:
            out_string += f"The node has the merits {merits}.\n"
        if flaws:
            out_string += f"The node has the flaws {flaws}.\n"

        resonance = ", ".join([str(x) for x in NodeResRating.objects.filter(node=self)])
        out_string += f"Its resonance is {resonance}.\n"
        return out_string

    def random(self, rank):
        self.save()
        self.random_rank(rank)
        points = 3 * self.rank
        ratio = random.choice([0.0, 0.25, 0.25, 0.5, 0.5, 0.5, 0.75, 0.75, 1.0])
        ratio_dict = {0.0: -2, 0.25: -1, 0.5: 0, 0.75: 1, 1.0: 2}
        self.ratio_cost = ratio_dict[ratio]
        points -= self.ratio_cost
        self.size = random.choice([-2, -1, -1, 0, 0, 0, 1, 1, 2])
        points -= self.size

        while self.total_resonance() < self.rank:
            self.random_resonance()
        while points > 1 and random.random() < 0.2:
            self.random_resonance()
            points -= 1
        points = self.random_merits_and_flaws(points)

        self.quintessence_per_week = int(points * ratio)
        points -= self.quintessence_per_week
        self.tass_per_week = points
        points -= self.tass_per_week
        assert points == 0
        self.resonance_postprocessing()
        self.description = self.basic_description()

    def increase_resonance(self, trait_name):
        if trait_name in [x.name for x in self.resonance.all()]:
            resonance = Resonance.objects.get(name=trait_name)
            rating = NodeResRating.objects.get(node=self, resonance=resonance)
            if rating.rating < 5:
                rating.rating += 1
                rating.save()
        elif trait_name in [x.name for x in Resonance.objects.all()]:
            resonance = Resonance.objects.get(name=trait_name)
            new_res = NodeResRating(node=self, resonance=resonance, rating=1)
            new_res.save()
        else:
            resonance = Resonance.objects.create(name=trait_name)
            new_res = NodeResRating(node=self, resonance=resonance, rating=1)
            new_res.save()

    def resonance_postprocessing(self):
        if "Corrupted" in [x.name for x in self.merits_and_flaws.all()]:
            if "Corrupted" in [x.name for x in Resonance.objects.all()]:
                res = Resonance.objects.get(name="Corrupted")
            else:
                res = Resonance.objects.create(name="Corrupted")
            self.increase_resonance(trait_name="Corrupted")
            self.increase_resonance(trait_name="Corrupted")
        if "Sphere Attuned" in [x.name for x in self.merits_and_flaws.all()]:
            spheres = [
                "Correspondence",
                "Time",
                "Spirit",
                "Entropy",
                "Mind",
                "Prime",
                "Matter",
                "Forces",
                "Life",
                "Data",
                "Primal Utility",
                "Dimensional Science",
            ]
            sphere = random.choice(spheres)
            sphere_name = sphere.replace(" ", "_").lower()
            res = [x for x in Resonance.objects.all() if getattr(x, sphere_name)]
            new_res = random.choice(res)
            self.increase_resonance(trait_name=new_res.name)


class NodeMeritFlaw(models.Model):
    """Class for node merit/flaw"""

    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)


class NodeResRating(models.Model):
    """Class for resonance rating"""

    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    resonance = models.ForeignKey(
        Resonance, on_delete=models.CASCADE, related_name="nodes"
    )
    rating = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.resonance.name} ({self.rating})"
