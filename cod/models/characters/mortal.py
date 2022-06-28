import random
from itertools import product

from django.db import models
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel

from accounts.models import CoDProfile
from core.models import Language
from core.utils import add_dot, random_ethnicity, random_name, weighted_choice


# Create your models here.
class Mortal(PolymorphicModel):
    type = "mortal"
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        CoDProfile, on_delete=models.CASCADE, related_name="characters"
    )

    status_keys = ["Un", "Sub", "App", "Ret", "Dec"]
    statuses = ["Unfinished", "Submitted", "Approved", "Retired", "Deceased"]
    status = models.CharField(
        max_length=3, choices=zip(status_keys, statuses), default="Un"
    )
    minor = models.BooleanField(default=False)

    concept = models.CharField(max_length=300)

    virtue = models.CharField(max_length=100)
    vice = models.CharField(max_length=100)

    short_term_aspiration_1 = models.CharField(max_length=100, default="")
    short_term_aspiration_2 = models.CharField(max_length=100, default="")
    long_term_aspiration = models.CharField(max_length=100, default="")

    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    resolve = models.IntegerField(default=1)

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    presence = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    composure = models.IntegerField(default=1)

    # Attribute -1 for physical or social at 0, -3 for mental
    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    crafts = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    politics = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    weaponry = models.IntegerField(default=0)

    animal_ken = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    persuasion = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

    merits = models.ManyToManyField("Merit", through="MeritRating")

    # Add 1 die to rolls when relevant - specialy
    specialties = models.ManyToManyField("Specialty", blank=True)

    willpower = models.IntegerField(default=1)
    integrity = models.IntegerField(default=7)
    size = models.IntegerField(default=5)
    speed = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    initiative_modifier = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)

    ethnicity = models.CharField(blank=True, null=True, max_length=100)
    sex = models.CharField(blank=True, null=True, max_length=100)

    breaking_point_1 = models.CharField(
        max_length=300, default="Worst thing you've ever done"
    )
    breaking_point_2 = models.CharField(
        max_length=300, default="Worst thing you can imagine doing"
    )
    breaking_point_3 = models.CharField(
        max_length=300, default="Worst thing you can imagine someone doing"
    )
    breaking_point_4 = models.CharField(
        max_length=300, default="Thing you've forgotten"
    )
    breaking_point_5 = models.CharField(max_length=300, default="Most traumatic thing")

    xp = models.IntegerField(default=0)
    spent_xp = models.TextField(default="")

    class Meta:
        verbose_name = "Mortal"
        verbose_name_plural = "Mortals"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cod:character", args=[str(self.id)])

    def add_name(self, name):
        self.name = name
        return True

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
            self.add_name(random_name(gender, self.ethnicity))

    def has_name(self):
        return self.name != ""

    def add_concept(self, concept):
        self.concept = concept
        return True

    def has_concept(self):
        return self.concept != ""

    def has_virtue(self):
        return self.virtue != ""

    def filter_virtues(self, virtue_list=None):
        virtues = [x for x in self.virtue.split(", ") if x]
        return [x for x in virtue_list if x not in virtues]

    def random_virtue(self):
        virtues = ["Competitive", "Generous", "Just", "Loyal"]
        virtues = self.filter_virtues(virtues)
        self.add_virtue(random.choice(virtues))

    def add_virtue(self, virtue):
        if virtue not in self.virtue.split(", "):
            virtues = self.virtue.split(", ")
            virtues.append(virtue)
            virtues = [x for x in virtues if x]
            self.virtue = ", ".join(virtues)
            return True
        return False

    def has_vice(self):
        return self.vice != ""

    def filter_vices(self, vice_list=None):
        vices = [x for x in self.vice.split(", ") if x]
        return [x for x in vice_list if x not in vices]

    def random_vice(self):
        vices = ["Ambitious", "Arrogant", "Competitive", "Greedy"]
        vices = self.filter_vices(vices)
        self.add_vice(random.choice(vices))

    def add_vice(self, vice):
        if vice not in self.vice.split(", "):
            vices = self.vice.split(", ")
            vices.append(vice)
            vices = [x for x in vices if x]
            self.vice = ", ".join(vices)
            return True
        return False

    def random_basis(self):
        if not self.has_name():
            self.random_name()
        self.add_concept("Concept")
        self.random_vice()
        self.random_virtue()
        self.random_aspirations()

    def random_aspirations(self):
        self.add_short_term_aspiration_1("Short Term Aspiration 1")
        self.add_short_term_aspiration_2("Short Term Aspiration 2")
        self.add_long_term_aspiration("Long Term Aspiration")

    def has_aspirations(self):
        if self.short_term_aspiration_1 == "":
            return False
        if self.short_term_aspiration_2 == "":
            return False
        if self.long_term_aspiration == "":
            return False
        return True

    def add_short_term_aspiration_1(self, aspiration):
        self.short_term_aspiration_1 = aspiration
        return True

    def add_short_term_aspiration_2(self, aspiration):
        self.short_term_aspiration_2 = aspiration
        return True

    def add_long_term_aspiration(self, aspiration):
        self.long_term_aspiration = aspiration
        return True

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_mental_attributes(self):
        return {
            "intelligence": self.intelligence,
            "wits": self.wits,
            "resolve": self.resolve,
        }

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "presence": self.presence,
            "manipulation": self.manipulation,
            "composure": self.composure,
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def total_attributes(self):
        return (
            self.total_physical_attributes()
            + self.total_social_attributes()
            + self.total_mental_attributes()
        )

    def has_attributes(self):
        triple = [
            self.total_physical_attributes(),
            self.total_mental_attributes(),
            self.total_social_attributes(),
        ]
        triple.sort()
        return triple == [6, 7, 8]

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def filter_attributes(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum
        }

    def random_attribute(self):
        choice = weighted_choice(self.filter_attributes(maximum=4))
        return add_dot(self, choice, 5)

    def random_attributes(self, primary=5, secondary=4, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.total_physical_attributes() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(self.get_physical_attributes())
            add_dot(self, attribute_choice, 5)
        while self.total_social_attributes() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(self.get_social_attributes())
            add_dot(self, attribute_choice, 5)
        while self.total_mental_attributes() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(self.get_mental_attributes())
            add_dot(self, attribute_choice, 5)

    def add_skill(self, skill, maximum=5):
        return add_dot(self, skill, maximum)

    def get_mental_skills(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "crafts": self.crafts,
            "investigation": self.investigation,
            "medicine": self.medicine,
            "occult": self.occult,
            "politics": self.politics,
            "science": self.science,
        }

    def get_physical_skills(self):
        return {
            "athletics": self.athletics,
            "brawl": self.brawl,
            "drive": self.drive,
            "firearms": self.firearms,
            "larceny": self.larceny,
            "stealth": self.stealth,
            "survival": self.survival,
            "weaponry": self.weaponry,
        }

    def get_social_skills(self):
        return {
            "animal_ken": self.animal_ken,
            "empathy": self.empathy,
            "expression": self.expression,
            "intimidation": self.intimidation,
            "persuasion": self.persuasion,
            "socialize": self.socialize,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
        }

    def total_physical_skills(self):
        return sum(self.get_physical_skills().values())

    def total_mental_skills(self):
        return sum(self.get_mental_skills().values())

    def total_social_skills(self):
        return sum(self.get_social_skills().values())

    def has_skills(self):
        triple = [
            self.total_physical_skills(),
            self.total_mental_skills(),
            self.total_social_skills(),
        ]
        triple.sort()
        return triple == [4, 7, 11]

    def total_skills(self):
        return (
            self.total_physical_skills()
            + self.total_mental_skills()
            + self.total_social_skills()
        )

    def filter_skills(self, minimum=0, maximum=5):
        return {k: v for k, v in self.get_skills().items() if minimum <= v <= maximum}

    def get_skills(self):
        tmp = {}
        tmp.update(self.get_physical_skills())
        tmp.update(self.get_mental_skills())
        tmp.update(self.get_social_skills())
        return tmp

    def random_skill(self):
        choice = weighted_choice(self.filter_skills(maximum=4))
        return add_dot(self, choice, 5)

    def random_skills(self, primary=11, secondary=7, tertiary=4):
        skill_types = [primary, secondary, tertiary]
        random.shuffle(skill_types)
        while self.total_physical_skills() < skill_types[0]:
            skill_choice = weighted_choice(self.get_physical_skills())
            add_dot(self, skill_choice, 5)
        while self.total_social_skills() < skill_types[1]:
            skill_choice = weighted_choice(self.get_social_skills())
            add_dot(self, skill_choice, 5)
        while self.total_mental_skills() < skill_types[2]:
            skill_choice = weighted_choice(self.get_mental_skills())
            add_dot(self, skill_choice, 5)

    def has_specialties(self):
        return self.specialties.count() == 3

    def filter_specialties(self, skill=None):
        if skill is None:
            return Specialty.objects.all().exclude(pk__in=self.specialties.all())
        return Specialty.objects.filter(skill=skill).exclude(
            pk__in=self.specialties.all()
        )

    def add_specialty(self, specialty):
        if specialty not in self.specialties.all():
            self.specialties.add(specialty)
            return True
        return False

    def random_specialties(self):
        for _ in range(3):
            self.random_specialty()

    def random_specialty(self):
        added = False
        while not added:
            skill_choice = weighted_choice(self.filter_skills(minimum=1))
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

    def add_merit(self, merit, detail=None):
        if merit.requires_detail and detail is None:
            raise Exception(f"Merit ({merit.name}) requires detail")
        if merit.name == "Giant":
            if "Small-Framed" in [x.name for x in self.merits.all()]:
                return False
        elif merit.name == "Small-Framed":
            if "Giant" in [x.name for x in self.merits.all()]:
                return False
        elif merit.name == "Fame":
            if "Anonymity" in [x.name for x in self.merits.all()]:
                return False
        elif merit.name == "Anonymity":
            if "Fame" in [x.name for x in self.merits.all()]:
                return False
        if merit in self.merits.all():
            if detail in [
                x.detail
                for x in MeritRating.objects.filter(character=self, merit=merit)
            ]:
                merit_rating = MeritRating.objects.get(
                    character=self, merit=merit, detail=detail
                )
                current_rating = merit_rating.rating
                values = [x for x in merit.ratings if x > current_rating]
                if len(values) != 0:
                    merit_rating.rating = min(values)
                    merit_rating.save()
                    return True
                return False
        rating = merit.ratings[0]
        MeritRating.objects.create(
            character=self, merit=merit, rating=rating, detail=detail
        )
        return True

    def remove_merit(self, merit):
        if merit in self.merits.all():
            MeritRating.objects.get(character=self, merit=merit).delete()
            return True
        return False

    def merit_rating(self, name, detail=None):
        if name not in [x.name for x in Merit.objects.all()]:
            return 0
        merit = Merit.objects.get(name=name)
        if merit not in self.merits.all():
            return 0
        if merit.requires_detail:
            details = [
                x.detail
                for x in MeritRating.objects.filter(character=self, merit=merit)
            ]
            if detail in details:
                return MeritRating.objects.get(
                    character=self, merit=merit, detail=detail
                ).rating
            return 0
        return MeritRating.objects.get(character=self, merit=merit).rating

    def total_merits(self):
        return sum(x.rating for x in MeritRating.objects.filter(character=self))

    def has_merits(self):
        return self.total_merits() == 7

    def filter_merits(self, dots=None):
        all_merits = Merit.objects.all()
        pairs = [(m, r) for m in all_merits for r in m.ratings]
        pairs = [p for p in pairs if p[1] <= dots]
        output = []
        for merit, rating in pairs:
            if merit in self.merits.all():
                r = MeritRating.objects.get(character=self, merit=merit).rating
                if rating > r:
                    output.append(merit)
            else:
                output.append(merit)
        output = list(set(output))
        return output

    def random_merit(self, dots=7):
        merit_candidates = self.filter_merits(dots=dots)
        choice = random.choice(merit_candidates)
        possible_details = choice.filter_details(self)
        if len(possible_details) == 0:
            detail = None
            if choice.requires_detail:
                return False
        else:
            detail = random.choice(possible_details)
        return self.add_merit(choice, detail=detail)

    def random_merits(self):
        dots = 7
        while not self.has_merits():
            self.random_merit(dots=dots)
            dots = 7 - self.total_merits()

    def assign_advantages(self):
        if self.merit_rating("Vice-Ridden") > 0:
            self.add_vice("New Vice")
        if self.merit_rating("Virtuous") > 0:
            self.add_virtue("New Virtue")
        if self.merit_rating("Giant") > 0:
            self.size += 1
        if self.merit_rating("Small-Framed") > 0:
            self.size -= 1
        self.willpower = self.resolve + self.composure
        self.speed = (
            self.strength + self.dexterity + 5 + self.merit_rating("Fleet of Foot")
        )
        self.health = self.size + self.stamina
        self.initiative_modifier = (
            self.dexterity + self.composure + self.merit_rating("Fast Reflexes")
        )
        if self.merit_rating("Defensive Combat (Brawl)") > 0:
            self.defense = min([self.wits, self.dexterity]) + self.brawl
        elif self.merit_rating("Defensive Combat (Weaponry)") > 0:
            self.defense = min([self.wits, self.dexterity]) + self.weaponry
        else:
            self.defense = min([self.wits, self.dexterity]) + self.athletics

    def xp_cost(self, trait_type):
        if trait_type == "attribute":
            return 4
        if trait_type == "merit":
            return 1
        if trait_type == "specialty":
            return 1
        if trait_type == "skill":
            return 2
        if trait_type == "integrity":
            return 2
        return 10000

    def random_spend_xp(self):
        frequencies = {
            "attribute": 1,
            "merit": 1,
            "specialty": 1,
            "skill": 1,
            "integrity": 1,
        }
        counter = 0
        while 10 < self.xp and counter < 50:
            counter += 1
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                if self.xp_cost(choice) <= self.xp:
                    trait = weighted_choice(self.filter_attributes(maximum=4))
                    value = getattr(self, trait) + 1
                    self.xp -= self.xp_cost(choice)
                    self.add_to_spend(trait, value, self.xp_cost(choice))
                    counter -= 1
            elif choice == "merit":
                if self.xp_cost(choice) <= self.xp:
                    merit_candidates = self.filter_merits(dots=self.xp)
                    trait = random.choice(merit_candidates)
                    possible_details = trait.filter_details(self)
                    if len(possible_details) == 0:
                        detail = None
                    else:
                        detail = random.choice(possible_details)
                    if detail is None and trait.requires_detail:
                        pass
                    else:
                        self.add_merit(trait, detail=detail)
                        self.xp -= self.xp_cost(choice)
                        self.add_to_spend(
                            trait.name,
                            MeritRating.objects.get(merit=trait, character=self).rating,
                            self.xp_cost(choice),
                        )
                        counter -= 1
            elif choice == "specialty":
                if self.xp_cost(choice) <= self.xp:
                    if self.random_specialty():
                        self.xp -= self.xp_cost(choice)
                        self.add_to_spend(
                            self.specialties.last(), 1, self.xp_cost(choice)
                        )
                        counter -= 1
            elif choice == "skill":
                if self.xp_cost(choice) <= self.xp:
                    trait = weighted_choice(self.filter_skills(maximum=4))
                    value = getattr(self, trait) + 1
                    self.xp -= self.xp_cost(choice)
                    self.add_to_spend(trait, value, self.xp_cost(choice))
                    counter -= 1
            elif choice == "integrity":
                if self.xp_cost(choice) <= self.xp:
                    if add_dot(self, "integrity", 10):
                        self.xp -= self.xp_cost(choice)
                        self.add_to_spend(
                            "integrity", self.integrity, self.xp_cost(choice)
                        )
                        counter -= 1

    def add_to_spend(self, trait, value, cost):
        trait = trait.replace("_", " ").title()
        new_term = f"{trait} {value} ({cost} XP)"
        spent = self.spent_xp.split(", ")
        spent.append(new_term)
        spent = [x for x in spent if len(x) != 0]
        self.spent_xp = ", ".join(spent)

    def spend_xp(self, trait):
        if trait in self.get_attributes():
            cost = self.xp_cost("attribute")
            if cost <= self.xp:
                if self.add_attribute(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.get_skills():
            cost = self.xp_cost("skill")
            if cost <= self.xp:
                if self.add_skill(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in [x.name for x in Merit.objects.all()]:
            cost = self.xp_cost("merit")
            if cost <= self.xp:
                if self.add_merit(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in [x.name for x in Specialty.objects.all()]:
            cost = self.xp_cost("specialty")
            if cost <= self.xp:
                if self.add_specialty(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait == "integrity":
            cost = self.xp_cost("integrity")
            if cost <= self.xp:
                if self.add_integrity(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        return False

    def random(self, xp=0):
        self.xp = xp
        self.random_basis()
        self.random_attributes()
        self.random_skills()
        self.random_specialties()
        self.random_merits()
        self.assign_advantages()
        self.random_spend_xp()
        self.save()


class Merit(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(default=list)
    max_rating = models.IntegerField(default=0)
    prereqs = models.JSONField(default=list)
    requires_detail = models.BooleanField(default=False)
    possible_details = models.JSONField(default=list)
    merit_type = models.CharField(max_length=100, default="")
    is_style = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Merit"
        verbose_name_plural = "Merits"

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    def prereq_satisfied(self, prereq, character):
        if prereq[0] in character.get_attributes().keys():
            if character.get_attributes()[prereq[0]] < prereq[1]:
                return False
            return True
        if prereq[0] in character.get_skills().keys():
            if prereq[1] == "specialty":
                if character.specialties.filter(skill=prereq[0]).count() == 0:
                    return False
                return True
            if character.get_skills()[prereq[0]] < prereq[1]:
                return False
            return True
        if prereq[0] == "skill":
            if len(character.filter_skills(minimum=prereq[1]).keys()) == 0:
                return False
            return True
        if prereq[0] == "specialty":
            possible_skills = character.filter_skills(minimum=prereq[1]).keys()
            applicable_specialties = []
            for skill in possible_skills:
                applicable_specialties.extend(character.specialties.filter(skill=skill))
            if len(applicable_specialties) == 0:
                return False
            return True
        if prereq[0] in [x.name for x in Merit.objects.all()]:
            m = Merit.objects.get(name=prereq[0])
            if m in character.merits.all():
                if (
                    MeritRating.objects.get(character=character, merit=m).rating
                    < prereq[1]
                ):
                    return False
                return True
            return False
        return False

    def check_prereqs(self, character):
        if len(self.prereqs) == 0:
            return True
        for prereq_set in self.prereqs:
            prereqs = [self.prereq_satisfied(x, character) for x in prereq_set]
            if all(prereqs):
                return True
        return False

    def filter_details(self, character):
        possible_details = self.possible_details
        if self.name == "Area of Expertise":
            possible_details = [x.name for x in character.specialties.all()]
        elif self.name == "Interdisciplinary Specialty":
            possible_details = [
                x.name
                for x in character.specialties.all()
                if x.skill in character.filter_skills(minimum=3).keys()
            ]
        elif self.name == "Investigative Aide":
            possible_details = list(character.filter_skills(minimum=3).keys())
        elif self.name == "Hobbyist Clique":
            possible_details = list(character.filter_skills(minimum=2).keys())
        elif self.name == "Professional Training":
            pairs = [(x, x.split("(")[-1][:-1].split(", ")) for x in possible_details]
            pairs = [(x[0], [y.lower().replace(" ", "_") for y in x[1]]) for x in pairs]
            all_skills = character.get_skills()
            possible_details = [
                x[0]
                for x in pairs
                if all_skills[x[1][0]] > 0 and all_skills[x[1][1]] > 0
            ]
        elif self.name == "Multilingual":
            possible_details = product(Language.objects.all(), Language.objects.all())
            possible_details = [x for x in possible_details if x[0] != x[1]]
        elif self.name == "Fighting Finesse":
            possible_details = character.specialties.filter(skill=self.prereqs[-1][0])
        return possible_details


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def display_skill(self):
        return self.skill.replace("_", " ").title()

    def __str__(self):
        return f"{self.name} ({self.display_skill()})"


class MeritRating(models.Model):
    character = models.ForeignKey(
        "Mortal", null=False, blank=False, on_delete=models.CASCADE
    )
    merit = models.ForeignKey(
        "Merit", null=False, blank=False, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)
    detail = models.CharField(max_length=100, null=True, blank=True)
