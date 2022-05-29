import random

from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from accounts.models import WoDProfile
from core.models import Language
from core.utils import add_dot, weighted_choice


# Create your models here.
class Archetype(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    stat = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def display_skill(self):
        return self.skill.replace("_", " ").title()

    def __str__(self):
        return f"{self.name} ({self.display_skill()})"


class MeritFlaw(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ratings = models.JSONField(default=list)


class MeritFlawRating(models.Model):
    character = models.ForeignKey("Human", on_delete=models.CASCADE)
    mf = models.ForeignKey(MeritFlaw, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Character(PolymorphicModel):
    type = "character"

    name = models.CharField(max_length=100, unique=True)
    player = models.ForeignKey(
        WoDProfile, on_delete=models.CASCADE, related_name="characters"
    )
    concept = models.CharField(max_length=100)

    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def random_concept(self):
        self.set_concept("Random")

    def has_name(self):
        return self.name != ""

    def set_name(self, name):
        self.name = name
        return True

    def random_name(self):
        self.set_name(f"Random {Character.objects.count() + 1}")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wod:character", kwargs={"pk": self.pk})


class Human(Character):
    type = "human"

    nature = models.ForeignKey(
        Archetype,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="nature_of",
    )
    demeanor = models.ForeignKey(
        Archetype,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="demeanor_of",
    )

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    alertness = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    empathy = models.IntegerField(default=0)
    expression = models.IntegerField(default=0)
    intimidation = models.IntegerField(default=0)
    streetwise = models.IntegerField(default=0)
    subterfuge = models.IntegerField(default=0)

    crafts = models.IntegerField(default=0)
    drive = models.IntegerField(default=0)
    etiquette = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)

    academics = models.IntegerField(default=0)
    computer = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    science = models.IntegerField(default=0)

    specialties = models.ManyToManyField(Specialty, blank=True)

    contacts = models.IntegerField(default=0)
    mentor = models.IntegerField(default=0)

    willpower = models.IntegerField(default=3)

    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through=MeritFlawRating
    )
    languages = models.ManyToManyField(Language, blank=True)

    age = models.IntegerField(blank=True, null=True)
    apparent_age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    hair = models.CharField(blank=True, null=True, max_length=100)
    eyes = models.CharField(blank=True, null=True, max_length=100)
    ethnicity = models.CharField(blank=True, null=True, max_length=100)
    nationality = models.CharField(blank=True, null=True, max_length=100)
    height = models.CharField(blank=True, null=True, max_length=100)
    weight = models.CharField(blank=True, null=True, max_length=100)
    sex = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField(blank=True, null=True)

    childhood = models.TextField(default="", blank=True, null=True)
    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)
    notes = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.TextField(default="")

    current_health_levels = models.CharField(default="", max_length=100, blank=True)

    freebies = 15
    background_points = 5

    def has_archetypes(self):
        return self.nature is not None and self.demeanor is not None

    def set_archetypes(self, nature, demeanor):
        self.nature = nature
        self.demeanor = demeanor
        return True

    def random_archetypes(self):
        self.nature = Archetype.objects.order_by("?").first()
        self.demeanor = Archetype.objects.order_by("?").first()

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum)

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_physical_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_social_attributes())
        return tmp

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }

    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits,
        }

    def total_physical_attributes(self):
        return sum(self.get_physical_attributes().values())

    def total_social_attributes(self):
        return sum(self.get_social_attributes().values())

    def total_mental_attributes(self):
        return sum(self.get_mental_attributes().values())

    def total_attributes(self):
        return sum(self.get_attributes().values())

    def random_attributes(self):
        attribute_types = [7, 5, 3]
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

    def has_attributes(self):
        triple = [
            self.total_physical_attributes(),
            self.total_mental_attributes(),
            self.total_social_attributes(),
        ]
        triple.sort()
        return triple == [6, 8, 10]

    def filter_attributes(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum
        }

    def random_attribute(self):
        choice = weighted_choice(self.filter_attributes(maximum=4))
        self.add_attribute(choice, 5)

    def add_ability(self, ability, maximum=4):
        return add_dot(self, ability, maximum)

    def random_ability(self, maximum=4):
        choice = weighted_choice(self.filter_abilities(maximum=maximum))
        self.add_ability(choice, 5)

    def get_abilities(self):
        tmp = {}
        tmp.update(self.get_talents())
        tmp.update(self.get_skills())
        tmp.update(self.get_knowledges())
        return tmp

    def filter_abilities(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_abilities().items() if minimum <= v <= maximum
        }

    def get_talents(self):
        return {
            "alertness": self.alertness,
            "athletics": self.athletics,
            "brawl": self.brawl,
            "empathy": self.empathy,
            "expression": self.expression,
            "intimidation": self.intimidation,
            "streetwise": self.streetwise,
            "subterfuge": self.subterfuge,
        }

    def get_skills(self):
        return {
            "crafts": self.crafts,
            "drive": self.drive,
            "etiquette": self.etiquette,
            "firearms": self.firearms,
            "melee": self.melee,
            "stealth": self.stealth,
        }

    def get_knowledges(self):
        return {
            "academics": self.academics,
            "computer": self.computer,
            "investigation": self.investigation,
            "medicine": self.medicine,
            "science": self.science,
        }

    def total_talents(self):
        return sum(self.get_talents().values())

    def total_skills(self):
        return sum(self.get_skills().values())

    def total_knowledges(self):
        return sum(self.get_knowledges().values())

    def random_abilities(self):
        ability_types = [13, 9, 5]
        random.shuffle(ability_types)
        while self.total_talents() < ability_types[0]:
            ability_choice = weighted_choice(self.get_talents())
            self.add_ability(ability_choice, maximum=3)
        while self.total_skills() < ability_types[1]:
            ability_choice = weighted_choice(self.get_skills())
            self.add_ability(ability_choice, maximum=3)
        while self.total_knowledges() < ability_types[2]:
            ability_choice = weighted_choice(self.get_knowledges())
            self.add_ability(ability_choice, maximum=3)

    def total_abilities(self):
        return sum(self.get_abilities().values())

    def has_abilities(self):
        triple = [self.total_talents(), self.total_skills(), self.total_knowledges()]
        triple.sort()
        return triple == [5, 9, 13]

    def add_specialty(self, specialty):
        if specialty in self.specialties.all():
            return False
        self.specialties.add(specialty)
        return True

    def has_specialties(self):
        # TODO: Need Mage version that includes Sphere specialties
        output = True
        for attribute in self.filter_attributes(minimum=4):
            output = output and (self.specialties.filter(stat=attribute).count() > 0)
        for ability in self.filter_abilities(minimum=4):
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "martial_arts",
                "melee",
                "academics",
                "esoterica",
                "lore",
                "politics",
                "science",
            ]
        ]:
            output = output and (self.specialties.filter(stat=ability).count() > 0)
        return output

    def filter_specialties(self, stat=None):
        if stat is None:
            return [
                x for x in Specialty.objects.all() if x not in self.specialties.all()
            ]
        return [
            x
            for x in Specialty.objects.filter(stat=stat)
            if x not in self.specialties.all()
        ]

    def random_specialty(self, stat):
        options = self.filter_specialties(stat=stat)
        self.add_specialty(random.choice(options))

    def random_specialties(self):
        for attribute in self.filter_attributes(minimum=4):
            self.specialties.add(random.choice(self.filter_specialties(stat=attribute)))
        for ability in self.filter_abilities(minimum=4):
            self.specialties.add(random.choice(self.filter_specialties(stat=ability)))
        for ability in [
            x
            for x in self.filter_abilities(minimum=1)
            if x
            in [
                "arts",
                "athletics",
                "crafts",
                "firearms",
                "martial_arts",
                "melee",
                "academics",
                "esoterica",
                "lore",
                "politics",
                "science",
            ]
        ]:
            self.specialties.add(random.choice(self.filter_specialties(stat=ability)))

    def get_backgrounds(self):
        return {
            "contacts": self.contacts,
            "mentor": self.mentor,
        }

    def add_background(self, background, maximum=5):
        return add_dot(self, background, maximum)

    def total_backgrounds(self):
        return sum(self.get_backgrounds().values())

    def filter_backgrounds(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_backgrounds().items() if minimum <= v <= maximum
        }

    def has_backgrounds(self):
        return self.total_backgrounds() == self.background_points

    def random_background(self):
        choice = weighted_choice(self.get_backgrounds())
        return self.add_background(choice)

    def random_backgrounds(self):
        while not self.has_backgrounds():
            self.random_background()

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def add_mf(self, mf, rating):
        if rating in mf.ratings:
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            return True
        return False

    def filter_mfs(self):
        full_set = MeritFlaw.objects.all()
        filtered_set = []
        for mf in full_set:
            for r in mf.ratings:
                if mf not in self.merits_and_flaws.all():
                    filtered_set.append((mf, r))
                elif r > self.mf_rating(mf) > 0:
                    filtered_set.append((mf, r))
                elif r < self.mf_rating(mf) < 0:
                    filtered_set.append((mf, r))
        filtered_set = [x[0] for x in filtered_set]
        if self.has_max_flaws():
            filtered_set = [x for x in filtered_set if max(x.ratings) > 0]
        return filtered_set

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum(
            [
                x.rating
                for x in MeritFlawRating.objects.filter(character=self)
                if x.rating < 0
            ]
        )

    def total_merits(self):
        return sum(
            [
                x.rating
                for x in MeritFlawRating.objects.filter(character=self)
                if x.rating > 0
            ]
        )

    def has_finishing_touches(self):
        return (
            self.age is not None
            and self.date_of_birth is not None
            and self.hair is not None
            and self.eyes is not None
            and self.ethnicity is not None
            and self.nationality is not None
            and self.height is not None
            and self.weight is not None
            and self.sex is not None
            and self.description is not None
            and self.apparent_age is not None
        )

    def has_history(self):
        return self.childhood != "" and self.history != "" and self.goals != ""

    def freebie_cost(self, trait):
        if trait == "attribute":
            return 5
        if trait == "ability":
            return 2
        if trait == "background":
            return 1
        if trait == "willpower":
            return 1
        if trait == "meritflaw":
            return 1

    def spend_freebies(self, trait):
        if trait in self.get_attributes():
            cost = self.freebie_cost("attribute")
            if cost <= self.freebies:
                if self.add_attribute(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        elif trait in self.get_abilities():
            cost = self.freebie_cost("ability")
            if cost <= self.freebies:
                if self.add_ability(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        elif trait in self.get_backgrounds():
            cost = self.freebie_cost("background")
            if cost <= self.freebies:
                if self.add_background(trait):
                    self.freebies -= cost
                    return True
                return False
            return False
        elif trait == "willpower":
            cost = self.freebie_cost("willpower")
            if cost <= self.freebies:
                if self.add_willpower():
                    self.freebies -= cost
                    return True
                return False
            return False
        elif trait in [x.name for x in MeritFlaw.objects.all()]:
            cost = self.freebie_cost("meritflaw")  # rating?
            mf = MeritFlaw.objects.get(name=trait)
            rating = random.choice(
                [x for x in mf.ratings if abs(x) > abs(self.mf_rating(mf))]
            )  # TODO: Should this just be the "lowest" value left?
            if cost * (rating - self.mf_rating(mf)) <= self.freebies:
                if self.add_mf(mf, rating):
                    self.freebies -= cost
                    return True
                return False
            return False

    def xp_cost(self, trait):
        if trait == "attribute":
            return 4
        if trait == "ability":
            return 2
        if trait == "new ability":
            return 3
        if trait == "background":
            return 3
        if trait == "new background":
            return 5
        if trait == "willpower":
            return 1

    def add_to_spend(self, trait, value, cost):
        trait = trait.replace("_", " ").title()
        new_term = f"{trait} {value} ({cost} XP)"
        spent = self.spent_xp.split(", ")
        spent.append(new_term)
        spent = [x for x in spent if len(x) != 0]
        self.spent_xp = ", ".join(spent)

    def spend_xp(self, trait):
        if trait in self.get_attributes():
            cost = self.xp_cost("attribute") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_attribute(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        elif trait in self.get_abilities():
            cost = self.xp_cost("ability") * getattr(self, trait)
            if cost == 0:
                cost = 3
            if cost <= self.xp:
                if self.add_ability(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        elif trait in self.get_backgrounds():
            cost = self.xp_cost("background") * getattr(self, trait)
            if cost == 0:
                cost = 5
            if cost <= self.xp:
                if self.add_background(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        elif trait == "willpower":
            cost = self.xp_cost("willpower") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_willpower():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False

    def random_freebies(self):
        frequencies = {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
            "meritflaw": 1,
        }
        counter = 0
        while counter < 10 and self.freebies > 0:
            counter += 1
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                trait = weighted_choice(self.get_attributes())
                self.spend_freebies(trait)
            if choice == "ability":
                trait = weighted_choice(self.get_abilities())
                self.spend_freebies(trait)
            if choice == "background":
                trait = weighted_choice(self.get_backgrounds())
                self.spend_freebies(trait)
            if choice == "willpower":
                self.spend_freebies(choice)
            if choice == "meritflaw":
                # TOOD: improve MF trait selection in freebies
                trait = MeritFlaw.objects.order_by("?").first().name
                self.spend_freebies(trait)

    def random_xp(self):
        frequencies = {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
        }
        counter = 0
        while counter < 10 and self.xp > 0:
            counter += 1
            choice = weighted_choice(frequencies)
            if choice == "attribute":
                trait = weighted_choice(self.get_attributes())
                self.spend_xp(trait)
            if choice == "ability":
                trait = weighted_choice(self.get_abilities())
                self.spend_xp(trait)
            if choice == "background":
                trait = weighted_choice(self.get_backgrounds())
                self.spend_xp(trait)
            if choice == "willpower":
                self.spend_xp(choice)

    def random(self, freebies=15, xp=0):
        self.freebies = freebies
        self.xp = xp
        self.random_name()
        self.random_concept()
        self.random_archetypes()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.random_freebies()
        self.random_xp()
        self.random_specialties()

    def get_wound_penalty(self):
        health_levels = len(self.current_health_levels)
        if health_levels <= 1:
            return 0
        if health_levels <= 3:
            return -1
        if health_levels <= 5:
            return -2
        if health_levels <= 6:
            return -5
        return -1000

    def add_bashing(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "B"
        elif "B" in self.current_health_levels:
            self.current_health_levels = self.current_health_levels.replace("B", "L", 1)
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    @staticmethod
    def sort_damage(damage_type):
        if damage_type == "B":
            return 2
        if damage_type == "L":
            return 1
        # All other damage should be Aggravated
        return 0

    def add_aggravated(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "A"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def add_lethal(self):
        if len(self.current_health_levels) < 7:
            self.current_health_levels += "L"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )
