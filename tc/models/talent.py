from django.db import models
from polymorphic.models import PolymorphicModel
from accounts.models import TCProfile
from django.shortcuts import reverse
from core.utils import weighted_choice, add_dot
import random


# Create your models here.
class Specialty(models.Model):
    skill_keys = [
        "aim",
        "ath",
        "clo",
        "com",
        "cul",
        "emp",
        "eni",
        "hum",
        "int",
        "lar",
        "med",
        "per",
        "pil",
        "sci",
        "sur",
        "tec",
    ]
    skill_name = [
        "aim",
        "athletics",
        "close_combat",
        "command",
        "culture",
        "empathy",
        "enigmas",
        "humanities",
        "integrity",
        "larceny",
        "medicine",
        "persuasion",
        "pilot",
        "science",
        "survival",
        "technology",
    ]

    skill = models.CharField(
        max_length=3, choices=zip(skill_keys, skill_name), default="aim"
    )
    specialty = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def display_skill(self):
        return (
            self.skill_name[self.skill_keys.index(self.skill)].replace("_", " ").title()
        )

    def __str__(self):
        return (
            f"{self.specialty} ({self.get_skill_display().replace('_', ' ').title()})"
        )


class Trick(models.Model):
    name = models.CharField(max_length=100)
    skill_keys = [
        "aim",
        "ath",
        "clo",
        "com",
        "cul",
        "emp",
        "eni",
        "hum",
        "int",
        "lar",
        "med",
        "per",
        "pil",
        "sci",
        "sur",
        "tec",
    ]
    skill_name = [
        "aim",
        "athletics",
        "close_combat",
        "command",
        "culture",
        "empathy",
        "enigmas",
        "humanities",
        "integrity",
        "larceny",
        "medicine",
        "persuasion",
        "pilot",
        "science",
        "survival",
        "technology",
    ]

    skill = models.CharField(
        max_length=3, choices=zip(skill_keys, skill_name), default="aim"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Edge(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(null=True, default=list)
    description = models.TextField(default="")
    prereq_attributes = models.ManyToManyField("AttributePrereq", blank=True)
    prereq_skills = models.ManyToManyField("SkillPrereq", blank=True)
    prereq_path_rating = models.IntegerField(default=0)
    prereq_edges = models.ManyToManyField(
        "EdgePrereq", blank=True, related_name="prereq_to"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class EnhancedEdge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    prereq_edges = models.ManyToManyField("EdgePrereq", blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    skills = models.JSONField(default=list)
    edges = models.ManyToManyField(Edge, blank=True)
    type = models.CharField(
        max_length=3, choices=[("ORI", "Origin"), ("ROL", "Role"), ("SOC", "Society"),]
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class PathConnection(models.Model):
    name = models.CharField(max_length=100)
    path = models.ForeignKey("Path", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class PathConnectionRating(models.Model):
    character = models.ForeignKey(
        "Human", on_delete=models.CASCADE, blank=True, null=True
    )
    path = models.ForeignKey("Path", null=True, blank=True, on_delete=models.CASCADE)
    path_connection = models.ForeignKey(
        "PathConnection", on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.character.name}, {self.path_connection}: {self.rating}"


class Human(PolymorphicModel):
    type = "Human"
    name = models.CharField(max_length=100, default="")
    player = models.ForeignKey(
        TCProfile,
        on_delete=models.CASCADE,
        related_name="characters",
        blank=True,
        null=True,
    )
    concept = models.CharField(max_length=100, default="")

    short_term_aspiration_1 = models.TextField(default="")
    short_term_aspiration_2 = models.TextField(default="")
    long_term_aspiration = models.TextField(default="")

    paths = models.ManyToManyField(
        "PathConnection",
        blank=True,
        related_name="characters_on_path",
        through=PathConnectionRating,
    )

    intellect = models.IntegerField(default=1)
    cunning = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)
    might = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    favored_approach = models.CharField(
        max_length=3,
        choices=[("FOR", "Force"), ("FIN", "Finesse"), ("RES", "Resilience"),],
        default="FOR",
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

    edges = models.ManyToManyField(
        Edge, related_name="edges_of", through="EdgeRating", blank=True
    )
    enhanced_edges = models.ManyToManyField(
        EnhancedEdge, related_name="edges_of", blank=True
    )

    moment_of_inspiration = models.TextField(default="")
    defense = models.IntegerField(default=1)
    bruised_levels = models.IntegerField(default=2)
    injured_levels = models.IntegerField(default=2)
    maimed_levels = models.IntegerField(default=1)

    xp = models.IntegerField(default=0)
    xp_spending = models.TextField(default="")

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("tc:character", args=[str(self.id)])

    def random_concept(self, name=None):
        if name is None:
            self.name = "Test 1"
        else:
            self.name = name
        self.concept = "Nova Character"

    def random_aspirations(self):
        self.short_term_aspiration_1 = "Short Term 1"
        self.short_term_aspiration_2 = "Short Term 2"
        self.long_term_aspiration = "Long Term"
        self.save()

    def random_paths(self):
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="ORI")))
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="ROL")))
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="SOC")))
        for path in PathConnectionRating.objects.filter(character=self):
            skills = path.path.skills
            skill_dict = {k: v for k, v in self.get_skills().items() if k in skills}
            total_skills = self.total_skills()
            while self.total_skills() < total_skills + 3:
                skill_choice = weighted_choice(skill_dict)
                add_dot(self, skill_choice, 5)

            total_diff = 2
            while total_diff > 0:
                result = self.add_random_edge(sublist=list(path.path.edges.all()))
                if result:
                    diff, (edge, rating) = result
                    diff = int(diff)
                    if diff <= total_diff:
                        self.apply_edge(edge, rating)
                        total_diff -= diff

    def random_skills(self):
        count = 0
        while count < 6:
            if self.add_random_skill():
                count += 1
        high_skills = {k for k, v in self.get_skills().items() if v >= 3}
        for skill_rating in high_skills:
            for _ in range(skill_rating.rating - 2):
                self.add_random_skill_trick(sublist=[skill_rating])
        self.add_random_skill_trick()
        for skill in [k for k, v in self.get_skills().items() if v >= 3]:
            self.add_random_skill_specialty(sublist=[skill])

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

    def total_skills(self):
        return sum(self.get_skills().values())

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

        approach = random.choice(approaches.keys())

        for key in approaches[approach]:
            add_dot(self, approaches[approach][key], 5)

        while self.physical_attribute_sum() < attribute_types[0] + 4:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            add_dot(self, attribute_choice, 5)
        while self.social_attribute_sum() < attribute_types[1] + 4:
            attribute_choice = weighted_choice(self.get_social_attributes())
            add_dot(self, attribute_choice, 5)
        while self.mental_attribute_sum() < attribute_types[2] + 4:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            add_dot(self, attribute_choice, 5)

