import random

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

    short_term_aspiration_1 = models.CharField(max_length=100, default="")
    short_term_aspiration_2 = models.CharField(max_length=100, default="")
    long_term_aspiration = models.CharField(max_length=100, default="")

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
        return (
            self.short_term_aspiration_1 != ""
            and self.short_term_aspiration_2 != ""
            and self.long_term_aspiration != ""
        )

    def random_aspirations(self):
        self.add_aspiration("Test Short 1", type="short", number=1)
        self.add_aspiration("Test Short 2", type="short", number=2)
        self.add_aspiration("Test Long", type="long", number=1)

    def random_basics(self):
        self.add_name("Random Name")
        self.add_concept("Random Concept")
        self.random_aspirations()

    def has_basics(self):
        return self.has_name() and self.has_concept() and self.has_aspirations()

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

    def random_skill(self, skill_list=None):
        if skill_list is None:
            choice = weighted_choice(self.filter_skills(maximum=4))
        else:
            choice = weighted_choice(
                {
                    k: v
                    for k, v in self.filter_skills(maximum=4).items()
                    if k in skill_list
                }
            )
        return add_dot(self, choice, 5)

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
        added = False
        while not added:
            skill_choice = weighted_choice(
                {
                    k: v
                    for k, v in self.filter_skills(minimum=3).items()
                    # if self.specialties.filter(skill=k).count() == 0
                }
            )
            possible_specialties = self.filter_specialties(skill=skill_choice)
            if len(possible_specialties) != 0:
                choice = random.choice(possible_specialties)
                self.add_specialty(choice)
                added = True
            all_possibilities = []
            for skill in self.filter_skills(minimum=1).keys():
                all_possibilities.extend(self.filter_specialties(skill=skill))
            if len(all_possibilities) == 0:
                break

    def random_specialties(self):
        for skill in self.filter_skills(minimum=3).keys():
            if self.specialties.filter(skill=skill).count() == 0:
                self.random_specialty(skill=skill)

    def add_trick(self, trick):
        if trick not in self.tricks.all():
            self.tricks.add(trick)
            return True
        return False

    def has_tricks(self):
        skills = self.filter_skills(minimum=3)
        for skill in skills.keys():
            if skills[skill] - 2 != self.tricks.filter(skill=skill).count():
                return False
        return True

    def filter_tricks(self, skill=None):
        if skill is None:
            return [x for x in Trick.objects.all() if x not in self.tricks.all()]
        return [
            x for x in Trick.objects.filter(skill=skill) if x not in self.tricks.all()
        ]

    def random_trick(self, skill=None):
        if skill is not None:
            rating = self.get_skills()[skill]
            if rating >= 3 and rating - 2 > self.tricks.filter(skill=skill).count():
                skill_choice = skill
            else:
                return False
        else:
            skills_geq_3 = self.filter_skills(minimum=3)
            possible_skills = []
            for skill in skills_geq_3.keys():
                if skills_geq_3[skill] - 2 > self.tricks.filter(skill=skill).count():
                    possible_skills.append(skill)
            skill_choice = weighted_choice(
                {k: v for k, v in skills_geq_3.items() if k in possible_skills}
            )
        possible_tricks = self.filter_tricks(skill=skill_choice)
        trick = random.choice(possible_tricks)
        return self.add_trick(trick)

    def random_tricks(self):
        skills = self.filter_skills(minimum=3)
        for skill in skills.keys():
            for _ in range(skills[skill] - 2 - self.tricks.filter(skill=skill).count()):
                self.random_trick(skill=skill)

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
        self.random_basics()
        self.random_paths()
        self.random_skills()
        self.random_specialties()
        self.random_tricks()
        self.random_attributes()
        self.random_edges()
        self.apply_random_template()
        self.random_xp_spend()
        self.save()


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
    edge = models.ForeignKey(Edge, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
