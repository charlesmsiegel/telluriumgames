import random
from itertools import product

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from polymorphic.models import PolymorphicModel

from core.models import Language, Model
from core.utils import add_dot, random_ethnicity, random_name, weighted_choice


# Create your models here.
class Mortal(Model):
    type = "mortal"

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

    merits = models.ManyToManyField("CoDMerit", through="MeritRating")

    # Add 1 die to rolls when relevant - specialy
    specialties = models.ManyToManyField("CoDSpecialty", blank=True)

    willpower = models.IntegerField(default=1)

    morality = models.IntegerField(default=7)

    morality_name = models.CharField(max_length=30, default="Integrity")

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

    conditions = models.ManyToManyField("Condition", blank=True)

    xp = models.IntegerField(default=0)
    beats = models.IntegerField(default=0)

    spent_xp = models.TextField(default="")

    class Meta:
        verbose_name = "Mortal"
        verbose_name_plural = "Mortals"

    def get_absolute_url(self):
        return reverse("cod:characters:character", args=[str(self.id)])

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

    def has_virtue(self):
        return self.virtue != ""

    def filter_virtues(self, virtue_list=None):
        virtues = [x for x in self.virtue.split(", ") if x]
        return [x for x in virtue_list if x not in virtues]

    def random_virtue(self):
        virtues = [
            "Competitive",
            "Generous",
            "Just",
            "Loyal",
            "Hopeful",
            "Loving",
            "Honest",
            "Trustworthy",
            "Ambitious",
            "Patient",
            "Courageous",
        ]
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
        vices = [
            "Ambitious",
            "Arrogant",
            "Competitive",
            "Greedy",
            "Pessimistic",
            "Hateful",
            "Deceitful",
            "Cruel",
            "Addictive",
            "Hasty",
            "Corrupt",
            "Dogmatic",
        ]
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
            return CoDSpecialty.objects.all().exclude(pk__in=self.specialties.all())
        return CoDSpecialty.objects.filter(skill=skill).exclude(
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
        if not CoDMerit.objects.filter(name=name).exists():
            return 0
        merit = CoDMerit.objects.get(name=name)
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

    @staticmethod
    def allowed_merit_types():
        return ["Mental", "Physical", "Social", "Supernatural", "Fighting"]

    def filter_merits(self, dots=None):
        ratings = MeritRating.objects.filter(character=self)
        had_merits = [x.merit.id for x in ratings]
        had_merits = CoDMerit.objects.filter(pk__in=had_merits)

        new_merits = CoDMerit.objects.filter(
            merit_type__in=self.allowed_merit_types()
        ).exclude(pk__in=[x.id for x in had_merits])
        new_merits = new_merits.filter(min_rating__lte=dots)

        tmp = []
        for merit in had_merits:
            merits = ratings.filter(merit=merit)
            r = min(merits.values_list("rating", flat=True))
            if len([x for x in merit.ratings if x > r]) != 0:
                rprime = min(x for x in merit.ratings if x > r)
            else:
                rprime = 100000
            if r != merit.max_rating:
                if merit.is_style:
                    if rprime <= dots:
                        tmp.append(merit)
                else:
                    if rprime - r <= dots:
                        tmp.append(merit)
        had_merits = CoDMerit.objects.filter(pk__in=[x.id for x in tmp])

        all_merits = new_merits | had_merits

        return [x for x in all_merits if x.check_prereqs(self)]

    def random_merit(self, dots=7):
        merit_candidates = self.filter_merits(dots=dots)
        if len(merit_candidates) != 0:
            merit_candidates = {k: k.count_prereqs(self) for k in merit_candidates}
            choice = weighted_choice(merit_candidates, floor=0, ceiling=100)
            possible_details = choice.filter_details(self)
            if len(possible_details) == 0:
                detail = None
                if choice.requires_detail:
                    return False
            else:
                detail = random.choice(possible_details)
            return self.add_merit(choice, detail=detail)
        return False

    def random_merits(self, total_dots=7):
        dots = total_dots
        while not self.has_merits():
            self.random_merit(dots=dots)
            dots = total_dots - self.total_merits()

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
        if trait_type == "morality":
            return 2
        if trait_type == "willpower":
            return 1
        return 10000

    def xp_frequencies(self):
        return {
            "attribute": 1,
            "merit": 1,
            "specialty": 1,
            "skill": 1,
            "morality": 1,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "merit": self.random_xp_merit,
            "specialty": self.random_xp_specialty,
            "skill": self.random_xp_skill,
            "morality": self.random_xp_morality,
            "willpower": self.random_xp_willpower,
        }

    def random_xp_willpower(self):
        return self.spend_xp_willpower()

    def random_xp_attributes(self):
        trait = weighted_choice(self.filter_attributes(maximum=4))
        return self.spend_xp_attribute(trait)

    def random_xp_skill(self):
        trait = weighted_choice(self.filter_skills(maximum=4))
        return self.spend_xp_skill(trait)

    def random_xp_merit(self):
        merit_candidates = self.filter_merits(dots=self.xp)
        trait = random.choice(merit_candidates)
        detail = None
        possible_details = trait.filter_details(self)
        if len(possible_details) == 0:
            detail = None
        else:
            detail = random.choice(possible_details)
        if detail is None and trait.requires_detail:
            return False
        return self.spend_xp_merit(trait, detail)

    def random_xp_specialty(self):
        skill_choice = weighted_choice(self.filter_skills(minimum=1))
        possible_specialties = self.filter_specialties(skill=skill_choice)
        if len(possible_specialties) != 0:
            trait = random.choice(possible_specialties)
            return self.spend_xp_specialty(trait)
        return False

    def random_xp_morality(self):
        return self.spend_xp_morality()

    def random_spend_xp(self):
        frequencies = self.xp_frequencies()
        counter = 0
        while counter < 10000 and self.xp > 0:
            choice = weighted_choice(frequencies)
            spent = self.random_xp_functions()[choice]()
            if not spent:
                counter += 1

    def add_to_spend(self, trait, value, cost):
        trait = trait.replace("_", " ").title()
        new_term = f"{trait} {value} ({cost} XP)"
        spent = self.spent_xp.split(", ")
        spent.append(new_term)
        spent = [x for x in spent if len(x) != 0]
        self.spent_xp = ", ".join(spent)

    def spend_xp_attribute(self, trait):
        cost = self.xp_cost("attribute")
        if cost <= self.xp:
            if self.add_attribute(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                return True
            return False
        return False

    def spend_xp_skill(self, trait):
        cost = self.xp_cost("skill")
        if cost <= self.xp:
            if self.add_skill(trait):
                self.xp -= cost
                self.add_to_spend(trait, getattr(self, trait), cost)
                return True
            return False
        return False

    def spend_xp_merit(self, trait, detail=None):
        cost = self.xp_cost("merit")
        if cost <= self.xp:
            if self.add_merit(trait, detail=detail):
                self.xp -= cost * self.merit_rating(trait)
                self.add_to_spend(trait.name, self.merit_rating(trait), cost)
                return True
            return False
        return False

    def spend_xp_specialty(self, trait):
        cost = self.xp_cost("specialty")
        if cost <= self.xp:
            if self.add_specialty(trait):
                self.xp -= cost
                self.add_to_spend(trait.name, 1, cost)
                return True
            return False
        return False

    def add_morality(self):
        return add_dot(self, "morality", 10)

    def add_willpower(self):
        return add_dot(self, "willpower", self.resolve + self.composure)

    def spend_xp_morality(self):
        cost = self.xp_cost("morality")
        if cost <= self.xp:
            if self.add_morality():
                self.xp -= cost
                self.add_to_spend("morality", getattr(self, "morality"), cost)
                return True
            return False
        return False

    def spend_xp_willpower(self):
        cost = self.xp_cost("willpower")
        if cost <= self.xp:
            if self.add_willpower():
                self.xp -= cost
                self.add_to_spend("willpower", getattr(self, "willpower"), cost)
                return True
            return False
        return False

    def spend_xp(self, trait):
        if trait in self.get_attributes():
            return self.spend_xp_attribute(trait)
        if trait in self.get_skills():
            return self.spend_xp_skill(trait)
        if CoDMerit.objects.filter(name=trait).exists():
            return self.spend_xp_merit(trait)
        if CoDSpecialty.objects.filter(name=trait).exists():
            return self.spend_xp_specialty(trait)
        if trait == "morality":
            return self.spend_xp_morality()
        if trait == "willpower":
            return self.spend_xp_willpower()
        return False

    def add_condition(self, condition):
        if condition in self.conditions.all():
            return False
        self.conditions.add(condition)
        return True

    def remove_condition(self, condition):
        if condition not in self.conditions.all():
            return False
        self.conditions.remove(condition)
        return True

    def random_condition(self):
        c = Condition.objects.all().order_by("?").first()
        return self.add_condition(c)

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


class CoDMerit(Model):
    type = "merit"

    ratings = models.JSONField(default=list)
    min_rating = models.IntegerField(default=0)
    max_rating = models.IntegerField(default=0)
    prereqs = models.JSONField(default=list)
    requires_detail = models.BooleanField(default=False)
    possible_details = models.JSONField(default=list)
    merit_type = models.CharField(max_length=100, default="")
    is_style = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Merit"
        verbose_name_plural = "Merits"

    def get_absolute_url(self):
        return reverse("cod:characters:mortal:merit", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        self.min_rating = min(self.ratings)
        super().save(*args, **kwargs)

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
        if CoDMerit.objects.filter(name=prereq[0]).exists():
            m = CoDMerit.objects.get(name=prereq[0])
            if prereq[1] == "same":
                minval = character.merit_rating(self)
            else:
                minval = prereq[1]
            if m in character.merits.all():
                if (
                    len(
                        [
                            x
                            for x in MeritRating.objects.filter(
                                character=character, merit=m
                            )
                            if x.rating >= minval
                        ]
                    )
                    == 0
                ):
                    return False
                return True
            return False
        if prereq[0] == "morality" and prereq[1] < 0:
            if character.morality > -prereq[1]:
                return False
            return True
        if hasattr(character, prereq[0]):
            if getattr(character, prereq[0]) < prereq[1]:
                return False
            return True
        if prereq[0] == "Morality Name":
            if character.morality_name == prereq[1]:
                return True
        return False

    def check_prereqs(self, character):
        if len(self.prereqs) == 0:
            return True
        for prereq_set in self.prereqs:
            prereqs = [self.prereq_satisfied(x, character) for x in prereq_set]
            if all(prereqs):
                return True
        return False

    def count_prereqs(self, character):
        if len(self.prereqs) == 0:
            return 0
        sets = []
        for prereq_set in self.prereqs:
            prereqs = [self.prereq_satisfied(x, character) for x in prereq_set]
            prereqs = [x for x in prereqs if x]
            sets.append(len(prereqs))
        return max(sets)

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
        elif self.name == "Contacts":
            detail_dict = {
                "academics": ["Rare Book Dealer", "Law Professor", "Head Librarian"],
                "computer": [
                    "AI Researcher",
                    "Hardcore Computer Gamer",
                    "White Hat Hacker",
                ],
                "crafts": [
                    "Automotive Engineer",
                    "Makerspace Enthusiast",
                    "Police Sketch Artist",
                ],
                "investigation": [
                    "Conspiracy Buff",
                    "Medical Examiner",
                    "Private Investigator",
                ],
                "medicine": ["Bio-Tech Company Researcher", "Chronic Patient", "EMT"],
                "occult": [
                    "Anthropology Professor",
                    "Neo-Pagan Author",
                    "Weird Hermit Down the Street",
                ],
                "politics": [
                    "Personal Assistant to the Governor",
                    "Political Blogger",
                    "Union Leader",
                ],
                "science": [
                    "Experimental Physicist",
                    "Geology Professor",
                    "Mad Inventor",
                ],
                "athletics": [
                    "Parkour Enthusiast",
                    "Physical Therapist",
                    "Running Club Buddy",
                ],
                "brawl": ["Club Bouncer", "Self-defense Teacher", "Sparring Partner"],
                "drive": ["Bush Pilot", "Mechanic", "Street Racer"],
                "firearms": [
                    "Gun store owner",
                    "Local law enforcement",
                    "Sharpshooter",
                ],
                "larceny": [
                    "Shady Pawn Shop Owner",
                    "Parole Officer",
                    "Three-Card Monte Dealer",
                ],
                "stealth": ["Bow Hunter", "Burglar", "Lookout from a Former Job"],
                "survival": [
                    "Homeless Person",
                    "Off-the-grid Survivalist",
                    "Scout Master",
                ],
                "weaponry": [
                    "Fencing Instructor",
                    "Gang Member",
                    "Western Martial Arts Enthusiast",
                ],
                "animal_ken": [
                    "Crazy Cat Lady",
                    "Rodeo Horse Trainer",
                    "Zoo Veterinarian",
                ],
                "empathy": ["Shoulder to Cry On", "Police Profiler", "Psych Student"],
                "expression": [
                    "Investigative Journalist",
                    "Political Speech Writer",
                    "Reclusive Poet",
                ],
                "intimidation": [
                    "Barroom Tough Guy",
                    "High-Powered Executive",
                    "Police Interrogator",
                ],
                "persuasion": ["Car Salesman", "Speech Coach", "Trial Lawyer"],
                "socialize": ["Diplomat", "Drinking Buddy", "Society Matron"],
                "streetwise": [
                    "Bartender in a Rough Part of Town",
                    "Drug Dealer",
                    "Undercover Cop",
                ],
                "subterfuge": ["Con Artist", "Crooked Politician", "Out-of-work Actor"],
            }
            skill = weighted_choice(character.get_skills())
            possible_details = detail_dict[skill]
        elif self.name.startswith("Fighting Finesse"):
            possible_details = character.specialties.filter(skill=self.prereqs[-1][0])
        return possible_details


class CoDSpecialty(Model):
    type = "specialty"

    skill = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def get_absolute_url(self):
        return reverse("cod:characters:mortal:specialty", kwargs={"pk": self.pk})

    def display_skill(self):
        return self.skill.replace("_", " ").title()

    def __str__(self):
        return f"{self.name} ({self.display_skill()})"


class MeritRating(models.Model):
    character = models.ForeignKey(
        "Mortal", null=False, blank=False, on_delete=models.CASCADE
    )
    merit = models.ForeignKey(
        "CoDMerit", null=False, blank=False, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)
    detail = models.CharField(max_length=100, null=True, blank=True)


class Condition(Model):
    type = "condition"

    persistent = models.BooleanField(default=False)
    resolution = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("cod:characters:mortal:condition", kwargs={"pk": self.pk})


class Tilt(Model):
    type = "tilt"

    tilt_type = models.CharField(
        max_length=20,
        choices=[("personal", "Personal"), ("environmental", "Environmental"),],
    )
    effect = models.TextField(default="")
    causing = models.TextField(default="")
    ending = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("cod:characters:mortal:tilt", kwargs={"pk": self.pk})
