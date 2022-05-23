from django.db import models

from wod.models.locations.human import Location


# Create your models here.
class Node(Location):
    type = "node"

    rank = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    merits_and_flaws = models.ManyToManyField(
        "NodeMeritFlaw", blank=True, through="NodeMeritFlawRating"
    )

    def random_rank(self):
        pass

    def set_rank(self, rank):
        pass

    def add_mf(self, mf, rating):
        pass

    def total_mf(self):
        return 0

    def filter_mf(self):
        pass

    def random_mf(self):
        pass

    def add_resonance(self, resonance):
        pass

    def resonance_rating(self, resonance):
        pass

    def filter_resonance(self):
        return []

    def total_resonance(self):
        return 0

    def random_resonance(self):
        pass

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
