from django.db import models
import random

from wod.models.locations.human import Location
from wod.models.characters.mage import Resonance


# Create your models here.
class Node(Location):
    type = "node"

    rank = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    merits_and_flaws = models.ManyToManyField(
        "NodeMeritFlaw", blank=True, through="NodeMeritFlawRating"
    )
    resonance = models.ManyToManyField(Resonance, blank=True, through="NodeResonanceRating")

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 6)
        self.set_rank(rank)

    def set_rank(self, rank):
        self.rank = rank
        self.points = 3 * self.rank
        return True

    def add_mf(self, mf, rating):
        pass

    def total_mf(self):
        return 0

    def filter_mf(self):
        pass

    def random_mf(self):
        pass

    def add_resonance(self, resonance):
        r, _ = NodeResonanceRating.objects.get_or_create(resonance=resonance, node=self)
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def resonance_rating(self, resonance):
        if resonance in self.resonance.all():
            return NodeResonanceRating.objects.get(node=self, resonance=resonance).rating
        return 0

    def filter_resonance(self, minimum=0, maximum=5, sphere=None):
        all_res = Resonance.objects.all()
        all_res = [x for x in all_res if minimum <= self.resonance_rating(x) <= maximum]
        if sphere is not None:
            all_res = [x for x in all_res if getattr(x, sphere)]
        return all_res

    def total_resonance(self):
        return sum([x.rating for x in NodeResonanceRating.objects.filter(node=self)])

    def random_resonance(self, sphere=None):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4, sphere=sphere)
            if len(possible) == 0:
                possible = self.filter_resonance(minimum=0, maximum=4, sphere=sphere)
        else:
            possible = self.filter_resonance(minimum=0, maximum=4, sphere=sphere)
        if len(possible) == 0:
            return False
        return self.add_resonance(random.choice(possible))

    def resonance_postprocessing(self):
        pass

    def random(self):
        pass


class NodeMeritFlaw(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)


class NodeMeritFlawRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    mf = models.ForeignKey(NodeMeritFlaw, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class NodeResonanceRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)