import random

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from core.models import CharacterModel, Model, ModelWithPrereqs
from core.utils import add_dot, weighted_choice


# Create your models here.
class ExMortal(CharacterModel):
    type = "mortal"

    creation_status = models.IntegerField(default=1)

    bonus_points = 21
    num_merits = 7

    concept = models.CharField(max_length=100)

    tertiary = lambda x: []

    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    perception = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    wits = models.IntegerField(default=1)
    charisma = models.IntegerField(default=1)
    manipulation = models.IntegerField(default=1)
    appearance = models.IntegerField(default=1)

    archery = models.IntegerField(default=0)
    athletics = models.IntegerField(default=0)
    awareness = models.IntegerField(default=0)
    brawl = models.IntegerField(default=0)
    bureaucracy = models.IntegerField(default=0)
    craft = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)
    integrity = models.IntegerField(default=0)
    investigation = models.IntegerField(default=0)
    larceny = models.IntegerField(default=0)
    linguistics = models.IntegerField(default=0)
    lore = models.IntegerField(default=0)
    martial_arts = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    melee = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    performance = models.IntegerField(default=0)
    presence = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)
    ride = models.IntegerField(default=0)
    sail = models.IntegerField(default=0)
    socialize = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    thrown = models.IntegerField(default=0)
    war = models.IntegerField(default=0)

    willpower = models.IntegerField(default=0)
    health_levels = models.IntegerField(default=0)
    essence = models.IntegerField(default=0)

    specialties = models.ManyToManyField("ExSpecialty", blank=True)
    intimacies = models.ManyToManyField("Intimacy", blank=True)
    merits = models.ManyToManyField("ExMerit", blank=True, through="MeritRating")

    xp = models.IntegerField(default=0)

    spent_xp = models.TextField(default="")

    class Meta:
        verbose_name = "Mortal"
        verbose_name_plural = "Mortals"

    def get_absolute_url(self):
        return reverse("exalted:characters:character", args=[str(self.id)])

    def get_update_url(self):
        return reverse(
            "exalted:characters:mortal:update_mortal", kwargs={"pk": self.pk}
        )

    def random_name(self):
        return self.set_name(f"Mortal {ExMortal.objects.count()}")

    def has_concept(self):
        return self.concept != ""

    def set_concept(self, concept):
        self.concept = concept
        return True

    def random_concept(self):
        return self.set_concept("Random")

    def has_attributes(self, primary=6, secondary=4, tertiary=3):
        triple = [primary + 3, secondary + 3, tertiary + 3]
        other_triple = [
            self.total_physical_attributes(),
            self.total_mental_attributes(),
            self.total_social_attributes(),
        ]
        triple.sort()
        other_triple.sort()
        return triple == other_triple

    def add_attribute(self, attribute, maximum=5):
        return add_dot(self, attribute, maximum=maximum)

    def get_attributes(self):
        tmp = {}
        tmp.update(self.get_social_attributes())
        tmp.update(self.get_mental_attributes())
        tmp.update(self.get_physical_attributes())
        return tmp

    def total_attributes(self):
        return sum(v for k, v in self.get_attributes().items())

    def filter_attributes(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_attributes().items() if minimum <= v <= maximum
        }

    def get_mental_attributes(self):
        return {
            "perception": self.perception,
            "intelligence": self.intelligence,
            "wits": self.wits,
        }

    def total_mental_attributes(self):
        return sum(v for k, v in self.get_mental_attributes().items())

    def get_physical_attributes(self):
        return {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "stamina": self.stamina,
        }

    def total_physical_attributes(self):
        return sum(v for k, v in self.get_physical_attributes().items())

    def get_social_attributes(self):
        return {
            "charisma": self.charisma,
            "manipulation": self.manipulation,
            "appearance": self.appearance,
        }

    def total_social_attributes(self):
        return sum(v for k, v in self.get_social_attributes().items())

    def random_attribute(self):
        d = self.get_attributes()
        choice = weighted_choice(d)
        return self.add_attribute(choice)

    def random_attributes(self, primary=6, secondary=4, tertiary=3):
        attribute_types = [primary, secondary, tertiary]
        random.shuffle(attribute_types)
        while self.total_physical_attributes() < attribute_types[0] + 3:
            attribute_choice = weighted_choice(
                self.get_physical_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        if attribute_types[0] == tertiary:
            self.tertiary = self.get_physical_attributes
        while self.total_social_attributes() < attribute_types[1] + 3:
            attribute_choice = weighted_choice(
                self.get_social_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        if attribute_types[1] == tertiary:
            self.tertiary = self.get_social_attributes
        while self.total_mental_attributes() < attribute_types[2] + 3:
            attribute_choice = weighted_choice(
                self.get_mental_attributes(), floor=3, ceiling=3
            )
            add_dot(self, attribute_choice, 5)
        if attribute_types[2] == tertiary:
            self.tertiary = self.get_mental_attributes

    def add_ability(self, ability, maximum=5):
        if (
            not self.merits.filter(name="Martial Artist").exists()
            and ability == "martial_arts"
        ):
            return False
        return add_dot(self, ability, maximum=maximum)

    def get_abilities(self):
        return {
            "archery": self.archery,
            "athletics": self.athletics,
            "awareness": self.awareness,
            "brawl": self.brawl,
            "bureaucracy": self.bureaucracy,
            "craft": self.craft,
            "dodge": self.dodge,
            "integrity": self.integrity,
            "investigation": self.investigation,
            "larceny": self.larceny,
            "linguistics": self.linguistics,
            "lore": self.lore,
            "martial_arts": self.martial_arts,
            "medicine": self.medicine,
            "melee": self.melee,
            "occult": self.occult,
            "performance": self.performance,
            "presence": self.presence,
            "resistance": self.resistance,
            "ride": self.ride,
            "sail": self.sail,
            "socialize": self.socialize,
            "stealth": self.stealth,
            "survival": self.survival,
            "thrown": self.thrown,
            "war": self.war,
        }

    def has_abilities(self):
        return self.total_abilities() == 28

    def total_abilities(self):
        return sum(v for k, v in self.get_abilities().items())

    def filter_abilities(self, minimum=0, maximum=5):
        return {
            k: v for k, v in self.get_abilities().items() if minimum <= v <= maximum
        }

    def random_ability(self, preference=None, maximum=5):
        d = self.get_abilities()
        if preference is not None:
            new_d = self.ability_types()[preference]()
            for k, v in new_d.items():
                d[k] += v
        choice = weighted_choice(d)
        return self.add_ability(choice, maximum=maximum)

    def random_abilities(self):
        preference = random.choice(list(self.ability_types().keys()))
        while not self.has_abilities():
            self.random_ability(preference=preference, maximum=3)

    def ability_types(self):
        return {
            "combat": self.get_combat_abilities,
            "crafting": self.get_crafting_abilities,
            "social": self.get_social_abilities,
            "sorcery": self.get_sorcery_abilities,
        }

    def get_combat_abilities(self):
        return {
            "archery": self.archery,
            "athletics": self.athletics,
            "awareness": self.awareness,
            "brawl": self.brawl,
            "dodge": self.dodge,
            "martial_arts": self.martial_arts,
            "melee": self.melee,
            "resistance": self.resistance,
            "ride": self.ride,
            "stealth": self.stealth,
            "thrown": self.thrown,
            "war": self.war,
        }

    def get_crafting_abilities(self):
        return {
            "craft": self.craft,
            "lore": self.lore,
            "occult": self.occult,
        }

    def get_social_abilities(self):
        return {
            "integrity": self.integrity,
            "linguistics": self.linguistics,
            "performance": self.performance,
            "presence": self.presence,
            "socialize": self.socialize,
        }

    def get_sorcery_abilities(self):
        return {"occult": self.occult}

    def has_specialties(self):
        return self.specialties.count() == 4

    def filter_specialties(self):
        possible_abilities = self.filter_abilities(minimum=1)
        return ExSpecialty.objects.filter(ability__in=possible_abilities).exclude(
            pk__in=self.specialties.all()
        )

    def add_specialty(self, specialty):
        if (
            self.get_abilities()[specialty.ability] > 0
            and specialty not in self.specialties.all()
        ):
            self.specialties.add(specialty)
            self.save()
            return True
        return False

    def random_specialty(self, ability=None):
        specialties = self.filter_specialties()
        if ability is not None:
            specialties = specialties.filter(ability=ability)
        return self.add_specialty(specialties.order_by("?").first())

    def random_specialties(self):
        while self.specialties.count() < 4:
            self.random_specialty()

    def has_intimacies(self):
        has_four = self.intimacies.count() >= 4
        one_defining = self.intimacies.filter(strength="defining").exists()
        one_major = self.intimacies.filter(strength="major").exists()
        one_negative = self.intimacies.filter(is_negative=True).exists()
        return has_four and one_defining and one_major and one_negative

    def add_intimacy(self, intimacy):
        self.intimacies.add(intimacy)
        return True

    def random_intimacy(self, intimacy_type=None, strength=None, is_negative=None):
        if intimacy_type is None:
            intimacy_type = random.choice(["tie", "principle"])
        if strength is None:
            strength = random.choice(["minor", "major", "defining"])
        if is_negative is None:
            is_negative = random.choice([True, False])
        i = Intimacy.objects.create(
            name=f"Intimacy {Intimacy.objects.count()}",
            intimacy_type=intimacy_type,
            strength=strength,
            is_negative=is_negative,
        )
        return self.add_intimacy(i)

    def random_intimacies(self):
        self.random_intimacy(strength="defining")
        self.random_intimacy(strength="major")
        self.random_intimacy()
        if self.intimacies.filter(is_negative=True).count() == 0:
            self.random_intimacy(is_negative=True)
        else:
            self.random_intimacy()

    def total_merits(self):
        return sum(x.rating for x in MeritRating.objects.filter(character=self))

    def has_merits(self, target_num=7):
        return self.total_merits() == target_num

    def add_merit(self, merit):
        if merit in self.merits.all():
            merit_rating = MeritRating.objects.get(character=self, merit=merit)
            if merit_rating.rating == max(merit.ratings):
                return False
            new_rating = min(x for x in merit.ratings if x > merit_rating.rating)
            merit_rating.rating = new_rating
            merit_rating.save()
            return True
        MeritRating.objects.create(
            character=self, merit=merit, rating=min(merit.ratings)
        )
        return True

    def filter_merits(self, dots=1000, merit_type=None, supernatural_permitted=False):
        if merit_type is None:
            merits = ExMerit.objects.all()
        else:
            merits = ExMerit.objects.filter(merit_type=merit_type)
        if not supernatural_permitted:
            merits = merits.exclude(merit_class="supernatural")

        new_merits = merits.exclude(pk__in=self.merits.all())
        old_merits = [
            x.merit.id
            for x in MeritRating.objects.filter(character=self)
            if x.rating < x.merit.max_rating
        ]
        old_merits = ExMerit.objects.filter(pk__in=old_merits)
        valid_merits = new_merits | old_merits
        output = [
            x
            for x in valid_merits
            if len([y for y in x.ratings if dots >= y > self.merit_rating(x)]) != 0
        ]
        return output

    def merit_rating(self, name):
        if not self.merits.filter(name=name).exists():
            return 0
        merit = ExMerit.objects.get(name=name)
        merit_rating = MeritRating.objects.get(character=self, merit=merit)
        return merit_rating.rating

    def random_merit(self, dots=7, list_of_merits=None):
        merit_candidates = self.filter_merits(dots=dots)
        if list_of_merits is not None:
            merit_candidates = [x for x in merit_candidates if x.name in list_of_merits]
        if len(merit_candidates) != 0:
            merit_candidates = {k: k.count_prereqs(self) for k in merit_candidates}
            choice = weighted_choice(merit_candidates, floor=0, ceiling=100)
            return self.add_merit(choice)
        return False

    def random_merits(self, num_dots=7, list_of_merits=None):
        dots = num_dots
        while not self.has_merits(target_num=num_dots):
            self.random_merit(dots=dots, list_of_merits=list_of_merits)
            dots = num_dots - self.total_merits()

    def has_finishing_touches(self):
        return self.willpower == 3 and self.health_levels == 7 and self.essence == 0

    def apply_finishing_touches(self):
        self.willpower = 3
        self.health_levels = 7
        self.essence = 0
        self.save()
        return True

    def add_willpower(self):
        return add_dot(self, "willpower", maximum=10)

    def bonus_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "specialty": 1,
            "merit": 1,
            "willpower": 1,
        }

    def random_bonus_functions(self):
        return {
            "attribute": self.random_bonus_attribute,
            "ability": self.random_bonus_ability,
            "specialty": self.random_bonus_specialty,
            "merit": self.random_bonus_merit,
            "willpower": self.random_bonus_willpower,
        }

    def random_bonus_attribute(self):
        trait = weighted_choice(self.get_attributes())
        return self.spend_bonus_points(trait)

    def random_bonus_ability(self):
        trait = weighted_choice(self.get_abilities())
        return self.spend_bonus_points(trait)

    def random_bonus_specialty(self):
        trait = random.choice(self.filter_specialties())
        return self.spend_bonus_points(trait.name)

    def random_bonus_merit(self):
        trait = random.choice(self.filter_merits())
        return self.spend_bonus_points(trait.name)

    def random_bonus_willpower(self):
        return self.spend_bonus_points("willpower")

    def bonus_cost(self, trait_type):
        if trait_type == "primary attribute":
            return 4
        if trait_type == "secondary attribute":
            return 4
        if trait_type == "tertiary attribute":
            return 3
        if trait_type == "ability":
            return 2
        if trait_type == "specialty":
            return 1
        if trait_type == "merit":
            return 1
        if trait_type == "willpower":
            return 2
        return 10000

    def spend_bonus_points(self, trait):
        if trait in self.get_attributes():
            if trait in self.tertiary():
                cost = self.bonus_cost("tertiary attribute")
            else:
                cost = self.bonus_cost("primary attribute")
            if cost <= self.bonus_points:
                if self.add_attribute(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if trait in self.get_abilities():
            cost = self.bonus_cost("ability")
            if cost <= self.bonus_points:
                if self.add_ability(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if ExSpecialty.objects.filter(name=trait).exists():
            cost = self.bonus_cost("specialty")
            if cost <= self.bonus_points:
                trait = ExSpecialty.objects.get(name=trait)
                if self.add_specialty(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if ExMerit.objects.filter(name=trait).exists():
            trait = ExMerit.objects.get(name=trait)
            new_rating = min(x for x in trait.ratings if x > self.merit_rating(trait))
            cost = self.bonus_cost("merit") * new_rating
            if cost <= self.bonus_points:
                if self.add_merit(trait):
                    self.bonus_points -= cost
                    return True
                return False
            return False
        if trait == "willpower":
            cost = self.bonus_cost("willpower")
            if cost <= self.bonus_points:
                if self.add_willpower():
                    self.bonus_points -= cost
                    return True
                return False
            return False
        return False

    def random_spend_bonus_points(self):
        frequencies = self.bonus_frequencies()
        counter = 0
        while counter < 100 and self.bonus_points > 0:
            choice = weighted_choice(frequencies)
            spent = self.random_bonus_functions()[choice]()
            if not spent:
                counter += 1

    def xp_frequencies(self):
        return {
            "attribute": 1,
            "ability": 1,
            "specialty": 1,
            "merit": 1,
            "willpower": 1,
        }

    def add_to_spend(self, trait, value, cost):
        trait = trait.replace("_", " ").title()
        new_term = f"{trait} {value} ({cost} XP)"
        spent = self.spent_xp.split(", ")
        spent.append(new_term)
        spent = [x for x in spent if len(x) != 0]
        self.spent_xp = ", ".join(spent)

    def random_xp_functions(self):
        return {
            "attribute": self.random_xp_attribute,
            "ability": self.random_xp_ability,
            "specialty": self.random_xp_specialty,
            "merit": self.random_xp_merit,
            "willpower": self.random_xp_willpower,
        }

    def random_xp_attribute(self):
        trait = weighted_choice(self.get_attributes())
        return self.spend_xp(trait)

    def random_xp_ability(self):
        trait = weighted_choice(self.get_abilities())
        return self.spend_xp(trait)

    def random_xp_specialty(self):
        trait = random.choice(self.filter_specialties())
        return self.spend_xp(trait.name)

    def random_xp_merit(self):
        trait = random.choice(self.filter_merits(merit_type="purchased"))
        return self.spend_xp(trait.name)

    def random_xp_willpower(self):
        return self.spend_bonus_points("willpower")

    def xp_cost(self, trait_type):
        if trait_type == "attribute":
            return 4
        if trait_type == "ability":
            return 2
        if trait_type == "new ability":
            return 3
        if trait_type == "specialty":
            return 3
        if trait_type == "merit":
            return 3
        if trait_type == "willpower":
            return 8
        return 10000

    def spend_xp(self, trait):
        if trait in self.get_attributes():
            cost = self.xp_cost("attribute") * self.get_attributes()[trait]
            if cost <= self.xp:
                if self.add_attribute(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if trait in self.get_abilities():
            current_rating = self.get_abilities()[trait]
            if current_rating == 0:
                cost = self.xp_cost("new ability")
            else:
                cost = self.xp_cost("ability") * current_rating
            if cost <= self.xp:
                if self.add_ability(trait):
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        if ExSpecialty.objects.filter(name=trait).exists():
            cost = self.xp_cost("specialty")
            if cost <= self.xp:
                if self.add_specialty(ExSpecialty.objects.get(name=trait)):
                    self.xp -= cost
                    self.add_to_spend(trait, 3, cost)
                    return True
                return False
            return False
        if ExMerit.objects.filter(name=trait).exists():
            merit = ExMerit.objects.get(name=trait)
            new_rating = min(x for x in merit.ratings if x > self.merit_rating(merit))
            cost = new_rating * self.xp_cost("merit")
            if cost <= self.xp:
                if self.add_merit(merit):
                    self.xp -= cost
                    self.add_to_spend(trait, self.merit_rating(merit), cost)
                    return True
                return False
            return False
        if trait == "willpower":
            cost = self.xp_cost("willpower")
            if cost <= self.xp:
                if self.add_willpower():
                    self.xp -= cost
                    self.add_to_spend(trait, getattr(self, trait), cost)
                    return True
                return False
            return False
        return False

    def random_spend_xp(self):
        frequencies = self.xp_frequencies()
        counter = 0
        while counter < 10000 and self.xp > 1:
            choice = weighted_choice(frequencies)
            spent = self.random_xp_functions()[choice]()
            if not spent:
                counter += 1

    def random(self, bonus_points=21, xp=0):
        self.update_status("Ran")
        self.bonus_points = bonus_points
        self.xp = xp
        self.random_name()
        self.random_concept()
        self.random_attributes()
        self.random_abilities()
        self.random_specialties()
        self.random_merits()
        self.random_intimacies()
        self.random_spend_bonus_points()
        self.random_spend_xp()
        self.apply_finishing_touches()


class ExSpecialty(Model):
    type = "specialty"

    ability = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

    def get_absolute_url(self):
        return reverse("exalted:characters:mortal:specialty", args=[str(self.id)])

    def get_update_url(self):
        return reverse(
            "exalted:characters:mortal:update_specialty", kwargs={"pk": self.pk}
        )

    def __str__(self):
        return f"{self.name} ({self.ability})"


class Intimacy(Model):
    type = "intimacy"

    intimacy_type = models.CharField(
        max_length=20, choices=[("tie", "Tie"), ("principle", "Principle"),],
    )
    strength = models.CharField(
        max_length=20,
        choices=[("minor", "Minor"), ("major", "Major"), ("defining", "Defining"),],
    )
    is_negative = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Intimacy"
        verbose_name_plural = "Intimacies"

    def get_absolute_url(self):
        return reverse("exalted:characters:mortal:intimacy", args=[str(self.id)])

    def get_update_url(self):
        return reverse(
            "exalted:characters:mortal:update_intimacy", kwargs={"pk": self.pk}
        )


class ExMerit(ModelWithPrereqs):
    type = "merit"

    merit_type = models.CharField(
        max_length=20,
        choices=[("innate", "Innate"), ("purchased", "Purchased"), ("story", "Story"),],
    )
    ratings = models.JSONField(default=list)
    merit_class = models.CharField(
        max_length=20,
        choices=[("standard", "Standard"), ("supernatural", "Supernatural"),],
        default="standard",
    )
    max_rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Merit"
        verbose_name_plural = "Merits"

    def get_absolute_url(self):
        return reverse("exalted:characters:mortal:merit", args=[str(self.id)])

    def get_update_url(self):
        return reverse("exalted:characters:mortal:update_merit", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.max_rating = max(self.ratings)
        return super().save(*args, **kwargs)

    def prereq_satisfied(self, prereq, character):
        if prereq[0] in character.get_attributes().keys():
            if character.get_attributes()[prereq[0]] < prereq[1]:
                return False
            return True
        if prereq[0] in character.get_abilities().keys():
            if character.get_abilities()[prereq[0]] < prereq[1]:
                return False
            return True
        if ExMerit.objects.filter(name=prereq[0]).exists():
            m = ExMerit.objects.get(name=prereq[0])
            if character.merit_rating(m) < prereq[1]:
                return False
            return True
        return False


class MeritRating(models.Model):
    character = models.ForeignKey(ExMortal, on_delete=models.CASCADE)
    merit = models.ForeignKey(ExMerit, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Merit Rating"
        verbose_name_plural = "Merit Ratings"
