from django.db import models
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel

from accounts.models import TCProfile
from core.utils import add_dot, weighted_choice


# Create your models here.
class Human(PolymorphicModel):
    type = "human"

    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        TCProfile, on_delete=models.CASCADE, related_name="characters"
    )

    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)

    concept = models.CharField(max_length=100)

    paths = models.ManyToManyField("Path", blank=True)

    intellect = models.IntegerField(default=1)
    cunning = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)
    might = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    aim = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    close_combat = models.IntegerField(default=0)
    command = models.IntegerField(default=0)
    culture = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    enigmas = models.IntegerField(default=0)
    humanities = models.IntegerField(default=0)
    integrity = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)
    pilot = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    technology = models.IntegerField(default=0)

    specialties = models.ManyToManyField("Specialty", blank=True)
    tricks = models.ManyToManyField("Trick", blank=True)
    edges = models.ManyToManyField("Edge", blank=True, through="EdgeRating")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tc:character", args=[str(self.id)])

    def add_name(self, name):
        self.name = name
        return True

    def has_name(self):
        return self.name != ""

    def add_concept(self, concept):
        self.concept = concept
        return True

    def has_concept(self):
        return self.concept != ""

    def add_aspiration(self, aspiration, type="short", number=1):
        if type == "short":
            if number == 1:
                self.short_term_aspiration_1 = aspiration
            else:
                self.short_term_aspiration_2 = aspiration
        else:
            self.long_term_aspiration = aspiration

    def has_aspirations(self):
        pass

    def random_aspirations(self):
        pass

    def random_basics(self):
        pass

    def has_basics(self):
        pass

    def has_skills(self):
        pass

    def get_skills(self):
        return {
            "aim": 0,
            "athletics": self.athletics,
            "close_combat": self.close_combat,
            "command": self.command,
            "culture": self.culture,
            "empathy": self.empathy,
            "enigmas": self.enigmas,
            "humanities": self.humanities,
            "integrity": self.integrity,
            "larceny": self.larceny,
            "medicine": self.medicine,
            "persuasion": self.persuasion,
            "pilot": self.pilot,
            "science": self.science,
            "survival": self.survival,
            "technology": self.technology,
        }

    def filter_skills(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_skills().items() if minimum <= v <= maximum}

    def total_skills(self):
        return sum(self.get_skills().values())

    def random_skill(self):
        pass

    def random_skills(self):
        pass

    def add_specialty(self, specialty):
        if specialty not in self.specialties.all():
            self.specialties.add(specialty)
            return True
        return False

    def filter_specialties(self, skill=None):
        if skill is None:
            return [
                x for x in Specialty.objects.all() if x not in self.specialties.all()
            ]
        return [
            x
            for x in Specialty.objects.filter(skill=skill)
            if x not in self.specialties.all()
        ]

    def has_specialties(self):
        for skill in self.filter_skills(minimum=3).keys():
            if self.specialties.filter(skill=skill).count() == 0:
                return False
        return True

    def random_specialty(self, skill=None):
        pass

    def random_specialties(self):
        pass

    def add_trick(self, trick):
        pass

    def has_tricks(self):
        pass

    def filter_tricks(self, skill=None):
        return []

    def random_trick(self, skill=None):
        pass

    def random_tricks(self):
        pass

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def has_attributes(self):
        pass

    def filter_attributes(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum
        }

    def get_attributes(self):
        return {
            "intellect": self.intellect,
            "cunning": self.cunning,
            "resolve": self.resolve,
            "might": self.might,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
            "presence": self.presence,
            "manipulation": self.manipulation,
            "composure": self.composure,
        }

    def total_attributes(self):
        return sum(self.get_attributes().values())

    def random_attribute(self):
        pass

    def random_attributes(self):
        pass

    def add_path(self, path):
        pass

    def has_paths(self):
        pass

    def random_path(self):
        pass

    def add_edge(self, edge):
        if edge in self.edges.all():
            edge_rating = EdgeRating.objects.get(character=self, edge=edge)
            current_rating = edge_rating.rating
            values = [x for x in edge.ratings if x > current_rating]
            if len(values) != 0:
                edge_rating.rating = min(values)
                edge_rating.save()
                return True
            return False
        EdgeRating.objects.create(character=self, edge=edge, rating=min(edge.ratings))
        return True

    def total_edges(self):
        return sum([x.rating for x in EdgeRating.objects.filter(character=self)])

    def has_edges(self):
        pass

    def random_edge(self):
        pass

    def random_edges(self):
        pass

    def has_template(self):
        pass

    def apply_random_template(self):
        pass

    def xp_cost(self, trait_type):
        pass

    def random_xp_spend(self):
        pass

    def random(self):
        pass


class Path(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100,
        choices=[("origin", "origin"), ("role", "role"), ("society", "society")],
        blank=True,
    )
    abilities = models.JSONField(default=list)
    edges = models.ManyToManyField("Edge", blank=True)


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)


class Trick(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)


class Edge(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(default=list)


class EdgeRating(models.Model):
    character = models.ForeignKey(
        Human, null=False, blank=False, on_delete=models.CASCADE
    )
    edge = models.ForeignKey(
        Edge, null=False, blank=False, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)
