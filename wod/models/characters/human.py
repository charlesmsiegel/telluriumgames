import random
from collections import defaultdict
from datetime import date, timedelta

import numpy as np
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, Q
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import CharacterModel, Language, Model
from core.utils import (
    add_dot,
    random_ethnicity,
    random_height,
    random_name,
    random_weight,
    weighted_choice,
)


# Create your models here.
class Archetype(Model):
    type = "archetype"

    class Meta:
        verbose_name = "Archetype"
        verbose_name_plural = "Archetypes"

    def get_absolute_url(self):
        return reverse("wod:characters:human:archetype", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("wod:characters:human:update_archetype", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"


class WoDSpecialty(Model):
    type = "specialty"

    stat = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def display_stat(self):
        return self.stat.replace("_", " ").title()

    def get_absolute_url(self):
        return reverse("wod:characters:specialty", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:human:update_specialty", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} ({self.display_stat()})"

    def get_heading(self):
        return "wod_heading"


class MeritFlaw(Model):
    type = "merit_flaw"

    ratings = models.JSONField(default=list)
    max_rating = models.IntegerField(default=0)
    human = models.BooleanField(default=False)
    kinfolk = models.BooleanField(default=False)
    garou = models.BooleanField(default=False)
    mage = models.BooleanField(default=False)
    changeling = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Merit or Flaw"
        verbose_name_plural = "Merits and Flaws"

    def get_absolute_url(self):
        return reverse("wod:characters:human:meritflaw", args=[str(self.id)])

    def get_update_url(self):
        return reverse("wod:characters:human:update_meritflaw", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        super().save(*args, **kwargs)

    def booleans(self):
        return ", ".join(
            [
                x.title()
                for x in ["human", "kinfolk", "garou", "mage"]
                if getattr(self, x)
            ]
        )


class MeritFlawRating(models.Model):
    character = models.ForeignKey("Human", on_delete=models.SET_NULL, null=True)
    mf = models.ForeignKey(MeritFlaw, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Merit or Flaw Rating"
        verbose_name_plural = "Merit and Flaw Ratings"

    def __str__(self):
        return f"{self.mf}: {self.rating}"


class Character(CharacterModel):
    type = "character"

    concept = models.CharField(max_length=100)
    creation_status = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

    def get_update_url(self):
        return reverse("wod:characters:human:update_character", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"

    def next_stage(self):
        self.creation_status += 1
        self.save()

    def prev_stage(self):
        self.creation_status -= 1
        self.save()

    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def random_concept(self):
        self.set_concept("Random")

    def random_name(self):
        self.set_name(f"Random Character {Character.objects.count()}")

    def get_absolute_url(self):
        return reverse("wod:characters:character", kwargs={"pk": self.pk})


class Human(Character):
    type = "human"

    nature = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="nature_of",
    )
    demeanor = models.ForeignKey(
        Archetype,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="demeanor_of",
    )

    derangements = models.ManyToManyField("Derangement", blank=True)

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

    specialties = models.ManyToManyField(WoDSpecialty, blank=True)

    contacts = models.IntegerField(default=0)
    mentor = models.IntegerField(default=0)

    willpower = models.IntegerField(default=3)

    merits_and_flaws = models.ManyToManyField(
        MeritFlaw, blank=True, through=MeritFlawRating, related_name="flawed"
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

    childhood = models.TextField(default="", blank=True, null=True)
    history = models.TextField(default="", blank=True, null=True)
    goals = models.TextField(default="", blank=True, null=True)
    notes = models.TextField(default="", blank=True, null=True)

    xp = models.IntegerField(default=0)
    spent_xp = models.TextField(default="")

    current_health_levels = models.CharField(default="", max_length=100, blank=True)
    max_health_levels = models.IntegerField(default=7)

    freebies = 15
    background_points = 5

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"

    def get_update_url(self):
        return reverse("wod:characters:human:update_human", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"

    def get_mf_and_rating_list(self):
        return [(x.name, self.mf_rating(x)) for x in self.merits_and_flaws.all()]

    def get_specialty(self, stat):
        spec = self.specialties.filter(stat=stat).first()
        if spec is None:
            return None
        return spec.name

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
            name = random_name(gender, self.ethnicity)
            count = 0
            while Character.objects.filter(name=name).exists() and count < 20:
                self.ethnicity = random_ethnicity()
                name = random_name(gender, self.ethnicity)
                count += 1
            if count == 20:
                name = f"Random Name {random.randint(1, 10000000000)}"
            self.set_name(name)

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

    def random_attributes(self, primary=7, secondary=5, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.total_physical_attributes() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(
                self.get_physical_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        while self.total_social_attributes() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(
                self.get_social_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        while self.total_mental_attributes() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(
                self.get_mental_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)

    def has_attributes(self, primary=7, secondary=5, tertiary=3):
        triple = [
            self.total_physical_attributes(),
            self.total_mental_attributes(),
            self.total_social_attributes(),
        ]
        triple.sort()
        return triple == [3 + tertiary, 3 + secondary, 3 + primary]

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
        choice = weighted_choice(
            self.filter_abilities(maximum=maximum), ceiling=5, floor=0
        )
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

    def random_abilities(self, primary=13, secondary=9, tertiary=5):
        ability_types = [primary, secondary, tertiary]
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

    def has_abilities(self, primary=13, secondary=9, tertiary=5):
        triple = [self.total_talents(), self.total_skills(), self.total_knowledges()]
        triple.sort()
        return triple == [tertiary, secondary, primary]

    def add_specialty(self, specialty):
        if getattr(self, specialty.stat) < 4 and specialty.stat not in [
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
        ]:
            return False
        if specialty in self.specialties.all():
            return False
        self.specialties.add(specialty)
        return True

    def has_specialties(self):
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
            return WoDSpecialty.objects.all().exclude(pk__in=self.specialties.all())
        return WoDSpecialty.objects.filter(stat=stat).exclude(
            pk__in=self.specialties.all()
        )

    def random_specialty(self, stat):
        options = self.filter_specialties(stat=stat)
        return self.add_specialty(random.choice(options))

    def random_specialties(self):
        need_specialty = []
        for attribute in self.filter_attributes(minimum=4):
            if attribute not in need_specialty:
                need_specialty.append(attribute)
        for ability in self.filter_abilities(minimum=4):
            if ability not in need_specialty:
                need_specialty.append(ability)
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
            if ability not in need_specialty:
                need_specialty.append(ability)
        for stat in need_specialty:
            self.specialties.add(random.choice(self.filter_specialties(stat=stat)))

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
        if self.total_backgrounds() > self.background_points:
            self.freebies -= self.total_backgrounds() - self.background_points
        return self.total_backgrounds() >= self.background_points

    def random_background(self):
        choice = weighted_choice(self.get_backgrounds())
        return self.add_background(choice)

    def random_backgrounds(self, backgrounds=None):
        if backgrounds is None:
            backgrounds = {}
        for trait, value in backgrounds.items():
            setattr(self, trait, value)
        while not self.has_backgrounds():
            self.random_background()

    def add_willpower(self):
        return add_dot(self, "willpower", 10)

    def add_random_language(self):
        d = {
            l.name: l.frequency
            for l in Language.objects.all()
            if l not in self.languages.all()
        }
        if len(d) == 0:
            return False
        choice = weighted_choice(d)
        choice = Language.objects.get(name=choice)
        self.languages.add(choice)
        self.save()
        return True

    def add_mf(self, mf, rating):
        if rating in mf.ratings:
            mfr, _ = MeritFlawRating.objects.get_or_create(character=self, mf=mf)
            mfr.rating = rating
            mfr.save()
            if mf.name in ["Language", "Natural Linguist"]:
                num_languages = self.mf_rating(MeritFlaw.objects.get(name="Language"))
                if self.merits_and_flaws.filter(name="Natural Linguist").exists():
                    num_languages *= 2
                while self.languages.count() < num_languages:
                    self.add_random_language()
            if mf.name == "Deranged":
                self.random_derangement()
            return True
        return False

    def add_derangement(self, derangement):
        if derangement in self.derangements.all():
            return False
        self.derangements.add(derangement)
        return True

    def random_derangement(self):
        d = (
            Derangement.objects.exclude(pk__in=self.derangements.all())
            .order_by("?")
            .first()
        )
        return self.add_derangement(d)

    def filter_mfs(self):
        character_type = self.type
        if character_type in ["fomor"]:
            character_type = "human"

        new_mfs = MeritFlaw.objects.exclude(pk__in=self.merits_and_flaws.all())

        non_max_mf = MeritFlawRating.objects.filter(character=self).exclude(
            Q(rating=F("mf__max_rating"))
        )

        had_mfs = MeritFlaw.objects.filter(pk__in=non_max_mf)
        mf = new_mfs | had_mfs
        if self.has_max_flaws():
            mf = mf.filter(max_rating__gt=0)
        return mf.filter(Q(**{character_type: True}))

    def mf_rating(self, mf):
        if mf not in self.merits_and_flaws.all():
            return 0
        return MeritFlawRating.objects.get(character=self, mf=mf).rating

    def has_max_flaws(self):
        return self.total_flaws() <= -7

    def total_flaws(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating < 0
        )

    def total_merits(self):
        return sum(
            x.rating
            for x in MeritFlawRating.objects.filter(character=self)
            if x.rating > 0
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

    def random_birthdate(self, age):
        earliest_date = date.today() - timedelta(days=(age + 1) * 365)
        int_delta = 365 * 24 * 60 * 60
        random_second = random.randrange(int_delta)
        return earliest_date + timedelta(seconds=random_second)

    def random_finishing_touches(self):
        self.age = random.randint(18, 80)
        birthday = self.random_birthdate(self.age)
        self.date_of_birth = birthday
        self.hair = "Brown"
        self.eyes = "Blue"
        self.nationality = "American"
        self.height = random_height(self.sex)
        self.weight = random_weight(self.sex)
        self.description = "Description"
        self.apparent_age = self.age
        self.save()

    def has_history(self):
        return self.childhood != "" and self.history != "" and self.goals != ""

    def random_history(self):
        self.childhood = "Childhood"
        self.history = "History"
        self.goals = "Goals"
        self.save()

    def freebie_cost(self, trait):
        costs = defaultdict(
            lambda: 10000,
            {
                "attribute": 5,
                "ability": 2,
                "background": 1,
                "willpower": 1,
                "meritflaw": 1,
            },
        )
        return costs[trait]

    def spend_freebies(self, trait):
        if trait in self.get_attributes():
            return self.spend_freebies_attribute(trait)
        if trait in self.get_abilities():
            return self.spend_freebies_ability(trait)
        if trait in self.get_backgrounds():
            return self.spend_freebies_background(trait)
        if trait == "willpower":
            return self.spend_freebies_willpower()
        if trait in [x.name for x in MeritFlaw.objects.all()]:
            return self.spend_freebies_mf(trait)
        return trait

    def spend_freebies_attribute(self, trait):
        cost = self.freebie_cost("attribute")
        if cost <= self.freebies:
            maximum = 5
            if self.merits_and_flaws.filter(
                name=f"Legendary Attributes - {trait.title()}"
            ).exists():
                maximum = 6
            if self.add_attribute(trait, maximum=maximum):
                self.freebies -= cost
                return True
            return False
        return False

    def spend_freebies_ability(self, trait):
        cost = self.freebie_cost("ability")
        if cost <= self.freebies:
            if self.add_ability(trait):
                self.freebies -= cost
                return True
            return False
        return False

    def spend_freebies_background(self, trait):
        cost = self.freebie_cost("background")
        if trait in ["enhancement", "sanctum", "totem"]:
            cost *= 2
        if cost <= self.freebies:
            if self.add_background(trait):
                self.freebies -= cost
                return True
            return False
        return False

    def spend_freebies_willpower(self):
        if self.willpower < 8:
            cost = self.freebie_cost("willpower")
            if cost <= self.freebies:
                if self.add_willpower():
                    self.freebies -= cost
                    return True
                return False
            return False
        return False

    def spend_freebies_mf(self, trait):
        if not self.has_max_flaws():
            cost = self.freebie_cost("meritflaw")  # rating?
            mf = MeritFlaw.objects.get(name=trait)
            abs_ratings = [abs(x) for x in mf.ratings]
            abs_ratings = [x for x in abs_ratings if x > abs(self.mf_rating(mf))]
            if len(abs_ratings) == 0:
                return False
            rating = min(abs_ratings)
            if rating not in mf.ratings:
                rating *= -1
            cost *= rating - self.mf_rating(mf)
            if cost <= self.freebies:
                if self.add_mf(mf, rating):
                    self.freebies -= cost
                    return True
                return False
            return False
        return False

    def xp_cost(self, trait):
        costs = defaultdict(
            lambda: 10000,
            {
                "attribute": 4,
                "ability": 2,
                "new ability": 3,
                "new background": 5,
                "background": 3,
                "willpower": 1,
            },
        )
        return costs[trait]

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
                maximum = 5
                if self.merits_and_flaws.filter(
                    name=f"Legendary Attributes - {trait.title()}"
                ).exists():
                    maximum = 6
                if self.add_attribute(trait, maximum=maximum):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.get_abilities():
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
        if trait in self.get_backgrounds():
            if getattr(self, trait) != 0:
                cost = self.xp_cost("background") * getattr(self, trait)
            else:
                cost = self.xp_cost("new background")
            if trait in ["enhancement", "sanctum", "totem"]:
                cost *= 2
            if cost <= self.xp:
                if self.add_background(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait == "willpower":
            cost = self.xp_cost("willpower") * getattr(self, trait)
            if cost <= self.xp:
                if self.add_willpower():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        return trait

    def freebie_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
            "meritflaw": 1,
        }

    def random_freebie_functions(self):
        return {
            "attribute": self.random_freebies_attributes,
            "ability": self.random_freebies_abilities,
            "background": self.random_freebies_background,
            "willpower": self.random_freebies_willpower,
            "meritflaw": self.random_freebies_meritflaw,
        }

    def random_freebies(self):
        frequencies = self.freebie_frequencies()
        while self.freebies > 0:
            choice = weighted_choice(frequencies, ceiling=100)
            self.random_freebie_functions()[choice]()

    def random_freebies_attributes(self):
        trait = weighted_choice(self.get_attributes())
        self.spend_freebies(trait)

    def random_freebies_abilities(self):
        trait = weighted_choice(self.get_abilities())
        self.spend_freebies(trait)

    def random_freebies_background(self):
        trait = weighted_choice(self.get_backgrounds())
        self.spend_freebies(trait)

    def random_freebies_willpower(self):
        self.spend_freebies("willpower")

    def random_freebies_meritflaw(self):
        options = [x.name for x in self.filter_mfs()]
        if len(options) != 0:
            trait = random.choice(options)
            self.spend_freebies(trait)

    def xp_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "background": 1,
            "willpower": 1,
        }

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attributes,
            "ability": self.random_xp_abilities,
            "background": self.random_xp_background,
            "willpower": self.random_xp_willpower,
        }

    def random_xp(self):
        frequencies = self.xp_frequencies()
        counter = 0
        while counter < 10000 and self.xp > 0:
            choice = weighted_choice(frequencies, ceiling=100)
            spent = self.random_xp_functions()[choice]()
            if not spent:
                counter += 1

    def random_xp_attributes(self):
        trait = weighted_choice(self.get_attributes())
        return self.spend_xp(trait)

    def random_xp_abilities(self):
        trait = weighted_choice(self.get_abilities())
        return self.spend_xp(trait)

    def random_xp_background(self):
        trait = weighted_choice(self.get_backgrounds())
        return self.spend_xp(trait)

    def random_xp_willpower(self):
        return self.spend_xp("willpower")

    def mf_based_corrections(self):
        if self.merits_and_flaws.filter(name="Ability Deficit").exists():
            stats_to_lose = random.choice(
                [self.get_talents(), self.get_skills(), self.get_knowledges()]
            )
            total_removed = 0
            for key, value in stats_to_lose.items():
                if value > 3:
                    total_removed += value - 3
                    stats_to_lose[key] = 3
                    setattr(self, key, 3)
            while total_removed > 5:
                tmp = {k: v for k, v in stats_to_lose.item() if v < 3}
                new_stat = weighted_choice(tmp)
                if self.add_ability(new_stat):
                    stats_to_lose[new_stat] += 1
                    total_removed -= 1
            while total_removed < 5:
                new_stat = weighted_choice(stats_to_lose)
                stats_to_lose[new_stat] -= 1
                setattr(self, new_stat, stats_to_lose[new_stat])
                total_removed += 1

    def random(self, freebies=15, xp=0, ethnicity=None):
        self.update_status("Ran")
        self.freebies = freebies
        self.xp = xp
        self.random_name(ethnicity=ethnicity)
        self.random_concept()
        self.random_archetypes()
        self.random_attributes()
        self.random_abilities()
        self.random_backgrounds()
        self.random_freebies()
        self.mf_based_corrections()
        self.random_xp()
        self.random_specialties()
        self.random_finishing_touches()
        self.random_history()

    def get_wound_penalty(self):
        health_levels = len(self.current_health_levels)
        if health_levels <= self.max_health_levels - 6:
            return 0
        if health_levels <= self.max_health_levels - 4:
            return -1
        if health_levels <= self.max_health_levels - 2:
            return -2
        if health_levels <= self.max_health_levels - 1:
            return -5
        return -1000

    def add_bashing(self):
        if len(self.current_health_levels) < self.max_health_levels:
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
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "A"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )

    def add_lethal(self):
        if len(self.current_health_levels) < self.max_health_levels:
            self.current_health_levels += "L"
        self.current_health_levels = "".join(
            sorted(self.current_health_levels, key=self.sort_damage)
        )


class Group(Model):
    type = "group"

    members = models.ManyToManyField(Human, blank=True)
    leader = models.ForeignKey(
        Human,
        blank=True,
        related_name="leads_group",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def get_update_url(self):
        return reverse("wod:characters:human:update_group", kwargs={"pk": self.pk})

    def get_heading(self):
        return "wod_heading"

    def random_name(self):
        self.name = f"Random Group {Group.objects.count()}"
        return True

    def get_absolute_url(self):
        return reverse("wod:characters:group", kwargs={"pk": self.pk})

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
        member_type=Human,
        character_kwargs=None,
    ):
        self.update_status("Ran")
        if character_kwargs is None:
            character_kwargs = {}
        if self.name == "":
            self.random_name()
        if num_chars is None:
            num_chars = random.randint(3, 7)
        if not new_characters and member_type.objects.count() < num_chars:
            raise ValueError(f"Not enough {member_type}!")
        if not new_characters:
            self.members.set(member_type.objects.order_by("?")[:num_chars])
        else:
            if user is None:
                if User.objects.filter(profile__wod_st=True).count() > 0:
                    user = (
                        User.objects.filter(profile__wod_st=True).order_by("?").first()
                    )
                else:
                    user = User.objects.create_user(username="New User")
                    user.profile.wod_st = True
                    user.save()
            for _ in range(num_chars):
                if not random_names:
                    name = f"{self.name} {self.members.count() + 1}"
                else:
                    name = ""
                m = member_type.objects.create(name=name, owner=user,)
                m.random(freebies=freebies, xp=xp, **character_kwargs)
                self.members.add(m)
        self.leader = self.members.order_by("?").first()
        self.save()


class Derangement(Model):
    type = "derangement"

    class Meta:
        verbose_name = "Derangement"
        verbose_name_plural = "Derangements"

    def get_absolute_url(self):
        return reverse("wod:characters:human:derangement", args=[str(self.id)])

    def get_update_url(self):
        return reverse(
            "wod:characters:human:update_derangement", kwargs={"pk": self.pk}
        )

    def get_heading(self):
        return "wod_heading"
