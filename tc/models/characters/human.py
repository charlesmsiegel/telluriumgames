import random

from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel

from core.models import Model
from core.utils import add_dot, random_ethnicity, random_name, weighted_choice


# Create your models here.
class Human(Model):
    type = "human"

    concept = models.CharField(max_length=100)

    short_term_aspiration_1 = models.CharField(max_length=100, default="")
    short_term_aspiration_2 = models.CharField(max_length=100, default="")
    long_term_aspiration = models.CharField(max_length=100, default="")

    paths = models.ManyToManyField("TCPath", blank=True, through="PathRating")

    intellect = models.IntegerField(default=1)
    cunning = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)
    might = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    approach = models.CharField(
        max_length=3,
        default="RES",
        choices=[("RES", "Resistance"), ("FOR", "Force"), ("FIN", "Finesse")],
    )

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
    enhanced_edges = models.ManyToManyField("EnhancedEdge", blank=True)

    bruised_levels = models.IntegerField(default=1)
    injured_levels = models.IntegerField(default=1)
    maimed_levels = models.IntegerField(default=1)

    ethnicity = models.CharField(blank=True, null=True, max_length=100)
    sex = models.CharField(blank=True, null=True, max_length=100)

    defense = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)

    spent_xp = models.TextField(default="")

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("tc:characters:character", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_human", kwargs={"pk": self.pk})

    def random_name(self, ethnicity=None):
        if ethnicity is not None:
            self.ethnicity = ethnicity
        if self.ethnicity is None:
            self.ethnicity = random_ethnicity()
        if self.sex is None:
            sex = random.random()
            if sex < 0.495:
                self.sex = "Male"
                gender = "m"
            elif sex < 0.99:
                self.sex = "Female"
                gender = "f"
            else:
                self.sex = "Other"
                gender = "mf"
        if not self.has_name():
            self.set_name(random_name(gender, self.ethnicity))

    def add_concept(self, concept):
        self.concept = concept
        return True

    def has_concept(self):
        return self.concept != ""

    def add_aspiration(self, aspiration, aspiration_type="short", number=1):
        if aspiration_type == "short":
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
        self.add_aspiration("Test Short 1", aspiration_type="short", number=1)
        self.add_aspiration("Test Short 2", aspiration_type="short", number=2)
        self.add_aspiration("Test Long", aspiration_type="long", number=1)

    def random_basics(self):
        if not self.has_name():
            self.random_name()
        self.add_concept("Random Concept")
        self.random_aspirations()

    def has_basics(self):
        return self.has_name() and self.has_concept() and self.has_aspirations()

    def has_skills(self):
        if PathRating.objects.filter(character=self, path__type="origin").count() == 0:
            return False
        if PathRating.objects.filter(character=self, path__type="role").count() == 0:
            return False
        if PathRating.objects.filter(character=self, path__type="society").count() == 0:
            return False
        p1 = PathRating.objects.filter(character=self, path__type="origin").first()
        p2 = PathRating.objects.filter(character=self, path__type="role").first()
        p3 = PathRating.objects.filter(character=self, path__type="society").first()
        return (
            self.total_skills(path=p1.path) >= 3
            and self.total_skills(path=p2.path) >= 3
            and self.total_skills(path=p3.path) >= 3
            and self.total_skills() == 15
        )

    def get_skills(self):
        return {
            "aim": self.aim,
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

    def add_skill(self, skill, maximum=5):
        return add_dot(self, skill, maximum)

    def total_skills(self, path=None):
        if path is None:
            return sum(self.get_skills().values())
        return sum(v for k, v in self.get_skills().items() if k in path.skills)

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
        p1 = PathRating.objects.filter(character=self, path__type="origin").first()
        p2 = PathRating.objects.filter(character=self, path__type="role").first()
        p3 = PathRating.objects.filter(character=self, path__type="society").first()
        while self.total_skills(path=p1.path) < 3:
            self.random_skill(skill_list=p1.path.skills)
        while self.total_skills(path=p2.path) < 3:
            self.random_skill(skill_list=p2.path.skills)
        while self.total_skills(path=p3.path) < 3:
            self.random_skill(skill_list=p3.path.skills)
        while self.total_skills() < 15:
            self.random_skill()

    def add_specialty(self, specialty):
        if specialty not in self.specialties.all():
            self.specialties.add(specialty)
            return True
        return False

    def filter_specialties(self, skill=None):
        if skill is None:
            return Specialty.objects.all().exclude(pk__in=self.specialties.all())
        return Specialty.objects.filter(skill=skill).exclude(
            pk__in=self.specialties.all()
        )

    def has_specialties(self):
        for skill in self.filter_skills(minimum=3).keys():
            if self.specialties.filter(skill=skill).count() == 0:
                return False
        return True

    def random_specialty(self, skill=None):
        added = False
        while not added:
            if skill is None:
                skill_choice = weighted_choice(self.filter_skills(minimum=3))
            else:
                skill_choice = skill
            possible_specialties = self.filter_specialties(skill=skill_choice)
            if len(possible_specialties) != 0:
                choice = random.choice(possible_specialties)
                self.add_specialty(choice)
                added = True
            all_possibilities = []
            for ski in self.filter_skills(minimum=1).keys():
                all_possibilities.extend(self.filter_specialties(skill=ski))
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
            return Trick.objects.all().exclude(pk__in=self.tricks.all())
        return Trick.objects.filter(skill=skill).exclude(pk__in=self.tricks.all())

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
            for ski in skills_geq_3.keys():
                if skills_geq_3[ski] - 2 > self.tricks.filter(skill=ski).count():
                    possible_skills.append(ski)
            skill_choice = weighted_choice(
                {k: v for k, v in skills_geq_3.items() if k in possible_skills}
            )
        possible_tricks = self.filter_tricks(skill=skill_choice)
        if len(possible_tricks) == 0:
            return False
        trick = random.choice(possible_tricks)
        return self.add_trick(trick)

    def random_tricks(self):
        skills = self.filter_skills(minimum=3)
        for skill in skills.keys():
            for _ in range(skills[skill] - 2 - self.tricks.filter(skill=skill).count()):
                self.random_trick(skill=skill)

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def has_attributes(self, template=False):
        totals = [
            self.physical_attribute_sum(),
            self.mental_attribute_sum(),
            self.social_attribute_sum(),
        ]
        totals.sort()
        if not template:
            return totals == [6, 8, 10]
        return totals in [[7, 8, 10], [6, 9, 10], [6, 8, 11]]

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

    def get_physical_attributes(self):
        return {
            "might": self.might,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_mental_attributes(self):
        return {
            "intellect": self.intellect,
            "cunning": self.cunning,
            "resolve": self.resolve,
        }

    def get_social_attributes(self):
        return {
            "presence": self.presence,
            "manipulation": self.manipulation,
            "composure": self.composure,
        }

    def get_force_attributes(self):
        return {
            "might": self.might,
            "intellect": self.intellect,
            "presence": self.presence,
        }

    def get_finesse_attributes(self):
        return {
            "cunning": self.cunning,
            "dexterity": self.dexterity,
            "manipulation": self.manipulation,
        }

    def get_resilience_attributes(self):
        return {
            "resolve": self.resolve,
            "composure": self.composure,
            "stamina": self.stamina,
        }

    def physical_attribute_sum(self):
        return sum(self.get_physical_attributes().values())

    def mental_attribute_sum(self):
        return sum(self.get_mental_attributes().values())

    def social_attribute_sum(self):
        return sum(self.get_social_attributes().values())

    def force_attribute_sum(self):
        return sum(self.get_force_attributes().values())

    def finesse_attribute_sum(self):
        return sum(self.get_finesse_attributes().values())

    def resilience_attribute_sum(self):
        return sum(self.get_resilience_attributes().values())

    def random_attribute(self, attribute_set=None):
        if attribute_set is None:
            attribute_set = self.get_attributes()
        add_dot(self, weighted_choice(attribute_set), 5)

    def random_attributes(self, primary=6, secondary=4, tertiary=2):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.physical_attribute_sum() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            add_dot(self, attribute_choice, 5)
        while self.social_attribute_sum() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(self.get_social_attributes())
            add_dot(self, attribute_choice, 5)
        while self.mental_attribute_sum() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            add_dot(self, attribute_choice, 5)

        approaches = {
            "force": self.get_force_attributes(),
            "finesse": self.get_finesse_attributes(),
            "resilience": self.get_resilience_attributes(),
        }

        approach = random.choice(list(approaches.keys()))
        for key in approaches[approach]:
            add_dot(self, key, 5)

        while self.physical_attribute_sum() < attribute_types[0] + 4:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            add_dot(self, attribute_choice, 5)
        while self.social_attribute_sum() < attribute_types[1] + 4:
            attribute_choice = weighted_choice(self.get_social_attributes())
            add_dot(self, attribute_choice, 5)
        while self.mental_attribute_sum() < attribute_types[2] + 4:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            add_dot(self, attribute_choice, 5)

    def add_path(self, path, connection=None):
        p, _ = PathRating.objects.get_or_create(character=self, path=path)
        if p.connection is None:
            if connection is None:
                connection = (
                    PathConnection.objects.filter(path=path).order_by("?").first()
                )
            p.connection = connection
            p.save()
        if p.rating < 5:
            p.rating += 1
            p.save()
            return True
        return False

    def has_paths(self):
        origin = self.paths.filter(type="origin").count() > 0
        role = self.paths.filter(type="role").count() > 0
        society = self.paths.filter(type="society").count() > 0
        return origin and role and society

    def random_path(self, path_type=None):
        if path_type is None:
            paths = TCPath.objects.all()
        else:
            paths = TCPath.objects.filter(type=path_type)
        paths = [x for x in paths if self.path_rating(x) != 5]
        d = {p: self.path_rating(p) for p in paths}
        choice = weighted_choice(d)
        self.add_path(choice)

    def random_paths(self):
        self.random_path(path_type="origin")
        self.random_path(path_type="role")
        self.random_path(path_type="society")

    def path_rating(self, path):
        if not isinstance(path, TCPath):
            path = TCPath.objects.get(name=path)
        if path not in self.paths.all():
            return 0
        return PathRating.objects.get(character=self, path=path).rating

    def total_path_rating(self):
        return sum(self.path_rating(x) for x in TCPath.objects.all())

    def has_connection(self, path):
        if self.path_rating(path) == 0:
            return True
        path_rating = PathRating.objects.get(character=self, path=path)
        return path_rating.connection is not None

    def set_connection(self, path, connection):
        if self.path_rating(path) == 0:
            return True
        path_rating = PathRating.objects.get(character=self, path=path)
        path_rating.connection = connection
        path_rating.save()
        return True

    def edge_rating(self, edge):
        if not isinstance(edge, Edge):
            edge = Edge.objects.get(name=edge)
        if edge not in self.edges.all():
            return 0
        return EdgeRating.objects.get(character=self, edge=edge).rating

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
        return sum(x.rating for x in EdgeRating.objects.filter(character=self))

    def total_path_edges(self, path=None):
        list_of_path_edges = []
        if path is None:
            for p in self.paths.all():
                list_of_path_edges.extend(list(p.edges.all()))
        else:
            list_of_path_edges.extend(list(path.edges.all()))
        list_of_path_edges = list(set(list_of_path_edges))
        path_edges_possessed = [x for x in list_of_path_edges if x in self.edges.all()]
        total = 0
        for edge in path_edges_possessed:
            total += EdgeRating.objects.get(character=self, edge=edge).rating
        return total

    def filter_edges(self, dots=100):
        ratings = EdgeRating.objects.filter(character=self)
        had_edges_id = [x.edge.id for x in ratings]
        ratings = [
            er
            for er in ratings
            if len(
                [x for x in er.edge.ratings if x > er.rating and x - er.rating <= dots]
            )
            != 0
        ]
        ratings = [er for er in ratings if er.rating < er.edge.max_rating]
        had_edges = Edge.objects.filter(pk__in=[x.edge.id for x in ratings])

        new_edges = Edge.objects.exclude(pk__in=had_edges_id)
        new_edges = new_edges.filter(min_rating__lte=dots)

        all_edges = had_edges | new_edges
        all_edges = [x for x in all_edges if x.type == "edge" and x.check_prereqs(self)]

        return all_edges

    def filter_enhanced_edges(self):
        return [
            x
            for x in EnhancedEdge.objects.all().exclude(
                pk__in=self.enhanced_edges.all()
            )
            if x.check_prereqs(self)
        ]

    def has_edges(self, start=False):
        output = True
        p1 = self.paths.filter(type="origin").first()
        p2 = self.paths.filter(type="role").first()
        p3 = self.paths.filter(type="society").first()
        output = output and self.total_path_edges() >= 6
        output = output and self.total_path_edges(path=p1) >= 2
        output = output and self.total_path_edges(path=p2) >= 2
        output = output and self.total_path_edges(path=p3) >= 2
        if start:
            output = output and self.total_path_edges() == 6
        else:
            output = output and self.total_edges() == 10
        return output

    def random_edge(self, dots=100, sublist=None):
        if sublist is not None:
            sublist = [
                x
                for x in sublist
                if len([y for y in x.ratings if self.edge_rating(x) < y <= dots]) != 0
            ]
            if len(sublist) != 0:
                sublist = {k: k.count_prereqs(self) for k in sublist}
                choice = weighted_choice(sublist, floor=0, ceiling=100)
                num_dots = [
                    x for x in choice.ratings if self.edge_rating(choice) < x <= dots
                ]
                return self.add_edge(choice)
            return False
        index = random.randint(1, Edge.objects.last().id)
        if Edge.objects.filter(pk=index).exists():
            choice = Edge.objects.get(pk=index)
            num_dots = [
                x for x in choice.ratings if self.edge_rating(choice) < x <= dots
            ]
            if choice.type == "edge" and len(num_dots) != 0:
                if random.randint(
                    0, choice.count_prereqs(self) + 1
                ) <= choice.count_prereqs(self):
                    return self.add_edge(choice)
                return False
            return False
        return False

    def random_edges(self):
        p1 = self.paths.filter(type="origin").first()
        p2 = self.paths.filter(type="role").first()
        p3 = self.paths.filter(type="society").first()
        failures = 0
        while self.total_edges() < 2 and failures < 20:
            if not self.random_edge(
                dots=2 - self.total_edges(), sublist=list(p1.edges.all())
            ):
                failures += 1
        while self.total_edges() < 4 and failures < 20:
            if not self.random_edge(
                dots=4 - self.total_edges(), sublist=list(p2.edges.all())
            ):
                failures += 1
        while self.total_edges() < 6 and failures < 20:
            if not self.random_edge(
                dots=6 - self.total_edges(), sublist=list(p3.edges.all())
            ):
                failures += 1

    def has_template(self):
        attribute_flag = self.total_attributes() == 25
        edges_flag = self.total_edges() == 10
        if self.stamina >= 3:
            self.injured_levels = 2
        if self.stamina == 5:
            self.bruised_levels = 2
        return attribute_flag and edges_flag

    def apply_random_template(self):
        attributes = self.filter_attributes(maximum=4)
        self.add_attribute(weighted_choice(attributes))
        total_edges = self.total_edges()
        attempts = 0
        while (self.total_edges() - total_edges) < 4 and attempts < 20:
            self.random_edge(dots=4 + total_edges - self.total_edges())
            attempts += 1
        if self.stamina >= 3:
            self.injured_levels = 2
        if self.stamina == 5:
            self.bruised_levels = 2

    def xp_cost(self, trait_type):
        if trait_type == "attribute":
            return 10
        if trait_type == "edge":
            return 3
        if trait_type == "path edge":
            return 2
        if trait_type == "enhanced edge":
            return 6
        if trait_type == "skill":
            return 5
        if trait_type == "skill trick":
            return 3
        if trait_type == "skill specialty":
            return 3
        if trait_type == "path":
            return 18
        if trait_type == "favored approach":
            return 15
        return 10000

    def get_path_edges(self, dots=100):
        path_edge_list = []
        for p in self.paths.all():
            path_edge_list.extend(
                [x.name for x in p.edges.all() if self.edge_rating(x) <= dots]
            )
        return path_edge_list

    def spend_xp(self, trait):
        if trait in self.get_attributes():
            return self.spend_xp_attribute(trait)
        if trait in self.get_path_edges(dots=self.xp // self.xp_cost("path edge")):
            return self.spend_xp_edge(trait, "path edge")
        if trait in [
            x.name for x in self.filter_edges(dots=self.xp // self.xp_cost("edge"))
        ]:
            return self.spend_xp_edge(trait, "edge")
        if trait in [x.name for x in EnhancedEdge.objects.all()]:
            return self.spend_xp_enhanced_edge(trait)
        if trait in self.get_skills():
            return self.spend_xp_skill(trait)
        if trait in [x.name for x in self.filter_tricks()]:
            return self.spend_xp_trick(trait)
        if trait in [x.name for x in self.filter_specialties()]:
            return self.spend_xp_specialty(trait)
        if trait in [x.name for x in TCPath.objects.all() if self.path_rating(x) < 5]:
            return self.spend_xp_path(trait)
        if trait in ["Favor FIN", "Favor FOR", "Favor RES"]:
            return self.spend_xp_approach(trait)
        self.save()
        return False

    def spend_xp_attribute(self, trait):
        cost = self.xp_cost("attribute")
        if self.xp >= cost:
            if self.add_attribute(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                return True
            return False
        return False

    def spend_xp_edge(self, trait, edge_type):
        e = Edge.objects.get(name=trait)
        new_rating = min(x for x in e.ratings if x > self.edge_rating(e))
        cost = self.xp_cost(edge_type) * (new_rating - self.edge_rating(e))
        if self.xp >= cost:
            if self.add_edge(e):
                self.xp -= cost
                self.add_to_spend(trait, self.edge_rating(e), cost)
                return True
            return False
        return False

    def spend_xp_enhanced_edge(self, trait):
        ee = EnhancedEdge.objects.get(name=trait)
        if ee not in self.enhanced_edges.all():
            cost = self.xp_cost("enhanced edge")
            if self.xp >= cost:
                self.enhanced_edges.add(ee)
                self.xp -= cost
                self.add_to_spend(trait, 1, cost)
                return True
            return False
        return False

    def spend_xp_skill(self, trait):
        cost = self.xp_cost("skill")
        if self.xp >= cost:
            if self.add_skill(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                return True
            return False
        return False

    def spend_xp_trick(self, trait):
        cost = self.xp_cost("skill trick")
        if self.xp >= cost:
            if self.add_trick(Trick.objects.get(name=trait)):
                self.xp -= cost
                self.add_to_spend(trait, 1, cost)
                return True
            return False
        return False

    def spend_xp_specialty(self, trait):
        cost = self.xp_cost("skill specialty")
        if self.xp >= cost:
            if self.add_specialty(Specialty.objects.get(name=trait)):
                self.xp -= cost
                self.add_to_spend(trait, 1, cost)
                return True
            return False
        return False

    def spend_xp_path(self, trait):
        cost = self.xp_cost("path")
        if self.xp >= cost:
            if self.add_path(TCPath.objects.get(name=trait)):
                self.xp -= cost
                self.add_to_spend(
                    trait, self.path_rating(TCPath.objects.get(name=trait)), cost
                )
                return True
            return False
        return False

    def spend_xp_approach(self, trait):
        cost = self.xp_cost("favored approach")
        if self.xp >= cost and self.approach != trait.split(" ")[-1]:
            self.approach = trait.split(" ")[-1]
            self.xp -= cost
            self.add_to_spend(trait, 1, cost)
            return True
        return False

    def add_to_spend(self, trait, value, cost):
        trait = trait.replace("_", " ").title()
        new_term = f"{trait} {value} ({cost} XP)"
        spent = self.spent_xp.split(", ")
        spent.append(new_term)
        spent = [x for x in spent if len(x) != 0]
        self.spent_xp = ", ".join(spent)

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
                    {p.name: self.path_rating(p) for p in TCPath.objects.all()}
                )
            elif trait_type == "approach":
                trait = random.choice(["Favor FIN", "Favor FOR", "Favor RES"])
            else:
                trait = None
            self.spend_xp(trait)

    def random(self, xp=0):
        self.random_basics()
        self.random_paths()
        self.random_skills()
        self.random_specialties()
        self.random_tricks()
        self.random_attributes()
        self.random_edges()
        self.apply_random_template()
        self.xp = xp
        self.random_spend_xp()
        self.save()


class TCPath(Model):
    type = "path"

    type = models.CharField(
        max_length=100,
        choices=[("origin", "origin"), ("role", "role"), ("society", "society")],
        blank=True,
    )
    skills = models.JSONField(default=list)
    edges = models.ManyToManyField("Edge", blank=True)
    gift_keywords = models.JSONField(default=list)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("tc:characters:path", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_path", kwargs={"pk": self.pk})


class Specialty(Model):
    type = "specialty"

    skill = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def display_skill(self):
        return self.skill.replace("_", " ").title()

    def get_absolute_url(self):
        return reverse("tc:characters:specialty", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_specialty", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} ({self.display_skill()})"


class Trick(Model):
    type = "trick"

    skill = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("tc:characters:trick", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_trick", kwargs={"pk": self.pk})


class Edge(Model):
    type = "edge"

    ratings = models.JSONField(default=list)
    min_rating = models.IntegerField(default=0)
    max_rating = models.IntegerField(default=0)
    prereqs = models.JSONField(default=list)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("tc:characters:edge", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_edge", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        self.min_rating = min(self.ratings)
        super().save(*args, **kwargs)

    def check_prereqs(self, character):
        return check_prereqs(self, character)

    def count_prereqs(self, character):
        if len(self.prereqs) == 0:
            return 0
        sets = []
        for prereq_set in self.prereqs:
            prereqs = [prereq_satisfied(x, character, self) for x in prereq_set]
            prereqs = [x for x in prereqs if x]
            sets.append(len(prereqs))
        return max(sets)


class EnhancedEdge(Model):
    type = "enhanced_edge"

    prereqs = models.JSONField(default=list)

    def get_absolute_url(self):
        return reverse("tc:characters:enhanced_edge", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_enhanced_edge", kwargs={"pk": self.pk})

    def check_prereqs(self, character):
        return check_prereqs(self, character)

    def count_prereqs(self, character):
        if len(self.prereqs) == 0:
            return 0
        sets = []
        for prereq_set in self.prereqs:
            prereqs = [self.prereq_satisfied(x, character) for x in prereq_set]
            prereqs = [x for x in prereqs if x]
            sets.append(len(prereqs))
        return max(sets)


class EdgeRating(models.Model):
    character = models.ForeignKey(
        Human, null=False, blank=False, on_delete=models.CASCADE
    )
    edge = models.ForeignKey(Edge, null=False, blank=False, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.edge.name}: {self.rating}"


class PathRating(models.Model):
    character = models.ForeignKey(
        Human, null=False, blank=False, on_delete=models.CASCADE
    )
    path = models.ForeignKey(TCPath, null=False, blank=False, on_delete=models.CASCADE)
    connection = models.ForeignKey(
        "PathConnection", null=True, blank=True, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.path.name}: {self.rating}"


class PathConnection(Model):
    type = "path_connection"

    path = models.ForeignKey(TCPath, blank=True, null=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("tc:characters:pathconnection", args=[str(self.id)])
    
    def get_update_url(self):
        return reverse("tc:characters:human:update_pathconnection", kwargs={"pk": self.pk})


def prereq_satisfied(prereq, character, obj):
    if prereq[0] in character.get_attributes().keys():
        return getattr(character, prereq[0]) >= prereq[1]
    if prereq[0] in character.get_skills().keys():
        return getattr(character, prereq[0]) >= prereq[1]
    if Edge.objects.filter(name=prereq[0]).exists():
        edge_prereq = Edge.objects.get(name=prereq[0])
        if edge_prereq.type == "edge":
            return character.edge_rating(edge_prereq) >= prereq[1]
    if prereq[0] == "path":
        any(
            x.rating > prereq[1]
            for x in PathRating.objects.filter(character=character)
            if obj in x.path.edges.all()
        )
    return False


def check_prereqs(obj, character):
    if len(obj.prereqs) == 0:
        return True
    for prereq_set in obj.prereqs:
        prereqs = [prereq_satisfied(x, character, obj) for x in prereq_set]
        if all(prereqs):
            return True
    return False
