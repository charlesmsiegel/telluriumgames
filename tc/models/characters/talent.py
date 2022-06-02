import random

from django.db import models

from core.utils import add_dot, weighted_choice
from tc.models.characters.human import Edge, EdgeRating, Human, Path


# Create your models here.
class Talent(Human):
    type = "talent"

    moment_of_inspiration = models.ForeignKey(
        "MomentOfInspiration", blank=True, null=True, on_delete=models.CASCADE
    )

    inspiration = models.IntegerField(default=1)

    gifts = models.ManyToManyField("Gift", blank=None)

    intuitive = models.IntegerField(default=0)
    reflective = models.IntegerField(default=0)
    destructive = models.IntegerField(default=0)

    def has_moment_of_inspiration(self):
        return self.moment_of_inspiration is not None

    def add_moment_of_inspiration(self, inspiration):
        self.moment_of_inspiration = inspiration
        return True

    def add_facet(self, facet):
        facet = facet.lower()
        if add_dot(self, facet, 5):
            if getattr(self, facet) == 1:
                add_dot(self, "inspiration", 10)
            if getattr(self, facet) == 3:
                add_dot(self, "inspiration", 10)
            if getattr(self, facet) == 5:
                add_dot(self, "inspiration", 10)
            return True
        return False

    def random_moment_of_inspiration(self):
        self.add_moment_of_inspiration(
            MomentOfInspiration.objects.order_by("?").first()
        )

    def has_facets(self):
        return self.total_facets() == 3

    def total_facets(self):
        return self.intuitive + self.reflective + self.destructive

    def random_facets(self):
        while self.total_facets() < 3:
            d = {
                "intuitive": self.intuitive,
                "reflective": self.reflective,
                "destructive": self.destructive,
            }
            d = {k: v for k, v in d.items() if v < 5}
            choice = weighted_choice(d)
            self.add_facet(choice)

    def add_gift(self, gift):
        if gift in self.gifts.all():
            return False
        self.gifts.add(gift)
        return True

    def total_gifts(self, path=None):
        if path is None:
            return self.gifts.count()
        gifts = self.gifts.all()
        path_gifts = []
        for keyword in path.gift_keywords:
            path_gifts.extend([x for x in gifts if keyword in x.keywords])
        return len(list(set(path_gifts)))

    def has_gifts(self):
        output = True
        p1 = self.paths.filter(type="origin").first()
        p2 = self.paths.filter(type="role").first()
        p3 = self.paths.filter(type="society").first()
        output = output and self.total_gifts() == 4
        output = output and self.total_gifts(path=p1) >= 1
        output = output and self.total_gifts(path=p2) >= 1
        output = output and self.total_gifts(path=p3) >= 1
        return output

    def random_gifts(self):
        p1 = self.paths.filter(type="origin").first()
        p2 = self.paths.filter(type="role").first()
        p3 = self.paths.filter(type="society").first()
        possible_gifts = self.filter_gifts(path=p1)
        if len(possible_gifts) != 0:
            self.add_gift(random.choice(possible_gifts))
        possible_gifts = self.filter_gifts(path=p2)
        if len(possible_gifts) != 0:
            self.add_gift(random.choice(possible_gifts))
        possible_gifts = self.filter_gifts(path=p3)
        if len(possible_gifts) != 0:
            self.add_gift(random.choice(possible_gifts))
        possible_gifts = self.filter_gifts()
        if len(possible_gifts) != 0:
            self.add_gift(random.choice(possible_gifts))

    def filter_gifts(self, keyword=None, path=None):
        gifts = Gift.objects.all()
        gifts = [x for x in gifts if x.check_prereqs(self)]
        gifts = [x for x in gifts if x not in self.gifts.all()]
        if keyword is not None:
            gifts = [x for x in gifts if keyword in x.keywords]
        if path is not None:
            gifts = [
                x
                for x in gifts
                if set(x.keywords).intersection(set(path.gift_keywords)) != set()
            ]
        return gifts

    def has_template(self):
        attribute_flag = self.total_attributes() == 25
        if self.stamina >= 3:
            self.injured_levels = 2
        if self.stamina == 5:
            self.bruised_levels = 2
        return (
            attribute_flag
            and self.has_gifts()
            and self.has_moment_of_inspiration()
            and self.has_facets()
        )

    def random_path(self, path_type=None):
        if path_type is None:
            paths = Path.objects.all()
        else:
            paths = Path.objects.filter(type=path_type)
        paths = [
            x for x in paths if self.path_rating(x) != 5 and len(x.gift_keywords) != 0
        ]
        d = {p: self.path_rating(p) for p in paths}
        choice = weighted_choice(d)
        self.add_path(choice)

    def apply_random_template(self):
        self.random_moment_of_inspiration()
        num = self.total_attributes()
        while self.total_attributes() < num + 1:
            add_dot(self, random.choice(self.moment_of_inspiration.attributes), 5)
            if set(
                getattr(self, x) for x in self.moment_of_inspiration.attributes
            ) == set([5]):
                add_dot(self, weighted_choice(self.get_attributes()), 5)
        self.random_gifts()
        self.random_facets()

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
                "gift": 1,
                "facet": 1,
            }
            trait_type = weighted_choice(options)
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
                    {p.name: self.path_rating(p) for p in Path.objects.all()}
                )
            elif trait_type == "approach":
                trait = random.choice(["Favor FIN", "Favor FOR", "Favor RES"])
            elif trait_type == "gift":
                if len(self.filter_gifts()) != 0:
                    trait = random.choice(self.filter_gifts()).name
            elif trait_type == "facet":
                trait = random.choice(["Intuitive", "Reflective", "Destructive"])
            else:
                trait = None
            self.spend_xp(trait)

    def xp_cost(self, trait_type):
        cost = super().xp_cost(trait_type)
        if cost != 10000:
            return cost
        if trait_type == "path gift":
            return 4
        if trait_type == "gift":
            return 5
        if trait_type == "facet":
            return 10
        return 10000

    def spend_xp(self, trait):
        if super().spend_xp(trait):
            return True
        if trait in [
            gift.name
            for path in self.paths.all()
            for gift in self.filter_gifts(path=path)
        ]:
            cost = self.xp_cost("path gift")
            if self.xp >= cost:
                if self.add_gift(Gift.objects.get(name=trait)):
                    self.xp -= cost
                    self.add_to_spend(trait, 1, cost)
                    return True
        elif trait in [x.name for x in self.filter_gifts()]:
            cost = self.xp_cost("gift")
            if self.xp >= cost:
                if self.add_gift(Gift.objects.get(name=trait)):
                    self.xp -= cost
                    self.add_to_spend(trait, 1, cost)
                    return True
        elif trait in ["Intuitive", "Reflective", "Destructive"]:
            cost = self.xp_cost("facet")
            if self.xp >= cost:
                if self.add_facet(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait.lower()), cost)
                    return True
        self.save()
        return False


class Gift(models.Model):
    name = models.CharField(max_length=100, unique=True)
    keywords = models.JSONField(default=list)
    prereqs = models.JSONField(default=list)

    def __str__(self):
        return f"{self.name} ({self.keywords})"

    def check_prereqs(self, character):
        satisfied = True
        for prereq in self.prereqs:
            if prereq[0] in character.get_attributes().keys():
                satisfied = satisfied and (getattr(character, prereq[0]) >= prereq[1])
            elif prereq[0] in character.get_skills().keys():
                satisfied = satisfied and (getattr(character, prereq[0]) >= prereq[1])
            elif prereq[0] in [x.name for x in Edge.objects.all() if x.type == "edge"]:
                edge_prereq = Edge.objects.get(name=prereq[0])
                if edge_prereq in character.edges.all():
                    x = EdgeRating.objects.get(character=character, edge=edge_prereq)
                    satisfied = satisfied and (x.rating >= prereq[1])
                else:
                    satisfied = False
        if (
            sum([getattr(character, k) for k in self.keywords if hasattr(character, k)])
            == 0
            and len(
                [getattr(character, k) for k in self.keywords if hasattr(character, k)]
            )
            != 0
        ):
            satisfied = False
        return satisfied


class MomentOfInspiration(models.Model):
    name = models.CharField(max_length=100, unique=True)
    attributes = models.JSONField(default=list)

    def __str__(self):
        return self.name
