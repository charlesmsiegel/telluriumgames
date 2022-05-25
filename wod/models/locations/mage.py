from django.db import models
import random

from wod.models.locations.human import Location
from wod.models.characters.mage import Resonance, Mage


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
        if rating not in mf.ratings:
            return False
        if mf in self.merits_and_flaws.all():
            current_rating = NodeMeritFlawRating.objects.get(node=self, mf=mf).rating
            if current_rating > 0 and current_rating < rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            if current_rating < 0 and current_rating > rating:
                x = NodeMeritFlawRating.objects.get(node=self, mf=mf)
                x.rating = rating
                x.save()
                return True
            return False
        NodeMeritFlawRating.objects.create(node=self, mf=mf, rating=rating)
        return True

    def total_mf(self):
        return sum([x.rating for x in NodeMeritFlawRating.objects.filter(node=self)])

    def filter_mf(self, minimum=-10, maximum=10):
        filtered = []
        for mf in NodeMeritFlaw.objects.all():
            for r in mf.ratings:
                if max(0, minimum) < r <= maximum:
                    if self.mf_rating(mf) < r:
                        filtered.append(mf)
                elif minimum < r < min(0, maximum):
                    if self.mf_rating(mf) > r:
                        filtered.append(mf)
        return list(set(filtered))

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
        if self.mf_rating(choice) == 0:
            r = random.choice(possible_ratings)
        if self.mf_rating(choice) < 0:
            possible_ratings = [x for x in possible_ratings if x < self.mf_rating(choice)]
            r = random.choice(possible_ratings)
        if self.mf_rating(choice) > 0:
            possible_ratings = [x for x in possible_ratings if x > self.mf_rating(choice)]
            r = random.choice(possible_ratings)
        if r == 0:
            return False
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
        if "Corrupted" in [x.name for x in self.merits_and_flaws.all()]:
            res, _ = Resonance.objects.get_or_create(name="Corrupted")
            self.add_resonance(res)
            self.add_resonance(res)
        if "Sphere Attuned" in [x.name for x in self.merits_and_flaws.all()]:
            sphere = random.choice(list(Mage(name="TMP").get_spheres().keys()))
            self.random_resonance(sphere=sphere)

    def random(self):
        pass


class NodeMeritFlaw(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)

    def __str__(self):
        return self.name

class NodeMeritFlawRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    mf = models.ForeignKey(NodeMeritFlaw, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class NodeResonanceRating(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)