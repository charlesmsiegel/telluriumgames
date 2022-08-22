import datetime
import math
import random
from tkinter import N

from django.db import models
from django.db.models import Q

from core.models import Language, Material, Medium, Noun
from core.utils import weighted_choice
from wod.models.characters.mage.faction import MageFaction
from wod.models.characters.mage.focus import Instrument, Paradigm, Practice
from wod.models.characters.mage.resonance import Resonance
from wod.models.characters.mage.rote import Effect
from wod.models.characters.mage.utils import (
    ABILITY_LIST,
    SPHERE_LIST,
    weighted_random_faction,
)
from wod.models.items.human import WoDItem


# Create your models here.
class WonderResonanceRating(models.Model):
    wonder = models.ForeignKey("Wonder", on_delete=models.CASCADE)
    resonance = models.ForeignKey(Resonance, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Wonder(WoDItem):
    type = "wonder"

    rank = models.IntegerField(default=0)
    background_cost = models.IntegerField(default=0)
    quintessence_max = models.IntegerField(default=0)

    resonance = models.ManyToManyField(
        Resonance, blank=True, through=WonderResonanceRating
    )

    def random_points(self):
        return 3 * (self.rank - 1) + random.randint(1, 3)

    def set_rank(self, rank):
        self.rank = rank
        return True

    def has_rank(self):
        return self.rank != 0

    def random_rank(self, rank=None):
        if rank is None:
            rank = random.randint(1, 5)
        return self.set_rank(rank)

    def add_resonance(self, resonance):
        r, _ = WonderResonanceRating.objects.get_or_create(
            resonance=resonance, wonder=self
        )
        if r.rating == 5:
            return False
        r.rating += 1
        r.save()
        return True

    def resonance_rating(self, resonance):
        if resonance in self.resonance.all():
            return WonderResonanceRating.objects.get(
                wonder=self, resonance=resonance
            ).rating
        return 0

    def filter_resonance(self, minimum=0, maximum=5):
        all_res = Resonance.objects.all()

        maxed_resonance = [
            x.id
            for x in WonderResonanceRating.objects.filter(
                wonder=self, rating__gt=maximum
            )
        ]
        mined_resonance = [
            x.id
            for x in WonderResonanceRating.objects.filter(
                wonder=self, rating__lt=minimum
            )
        ]
        all_res = all_res.exclude(pk__in=maxed_resonance)
        all_res = all_res.exclude(pk__in=mined_resonance)
        if minimum > 0:
            all_res = all_res.filter(
                pk__in=[
                    x.resonance.id
                    for x in WonderResonanceRating.objects.filter(
                        node=self, rating__gt=0
                    )
                ]
            )
        return all_res

    def total_resonance(self):
        return sum(x.rating for x in WonderResonanceRating.objects.filter(wonder=self))

    def random_resonance(self):
        if random.random() < 0.7:
            possible = self.filter_resonance(minimum=1, maximum=4)
            if len(possible) > 0:
                choice = random.choice(possible)
                if self.add_resonance(choice):
                    return True
        while True:
            index = random.randint(1, Resonance.objects.last().id)
            if Resonance.objects.filter(pk=index).exists():
                choice = Resonance.objects.get(pk=index)
                if self.add_resonance(choice):
                    return True

    def has_resonance(self):
        return self.total_resonance() >= self.rank

    def random(self, rank=None, name=None):
        self.random_name(name=name)
        self.random_rank(rank=rank)
        while not self.has_resonance():
            self.random_resonance()
        self.background_cost = 2 * self.rank


class Charm(Wonder):
    type = "charm"

    arete = models.IntegerField(default=0)
    power = models.ForeignKey(Effect, blank=True, null=True, on_delete=models.CASCADE)

    def set_power(self, power):
        self.power = power
        return True

    def has_power(self):
        return self.power is not None

    def random_power(self):
        e = Effect.objects.filter(max_sphere=self.rank).order_by("?").first()
        return self.set_power(e)

    def random(self, name=None, rank=None):
        super().random(rank=rank, name=name)
        self.random_power()
        self.arete = self.rank
        self.background_cost = self.rank


class Artifact(Wonder):
    type = "artifact"

    power = models.ForeignKey(Effect, blank=True, null=True, on_delete=models.CASCADE)

    def set_power(self, power):
        self.power = power
        return True

    def has_power(self):
        return self.power is not None

    def random_power(self):
        e = Effect.objects.filter(max_sphere=self.rank).order_by("?").first()
        return self.set_power(e)

    def random(self, name=None, rank=None):
        super().random(rank=rank, name=name)
        self.random_power()
        self.quintessence_max = 5 * self.rank
        self.background_cost = 2 * self.rank


class Talisman(Wonder):
    type = "talisman"

    arete = models.IntegerField(default=0)
    powers = models.ManyToManyField(Effect, blank=True)

    def add_power(self, power):
        self.powers.add(power)
        return True

    def has_powers(self):
        return self.powers.count() == self.rank

    def random_power(self, rank):
        e = Effect.objects.filter(max_sphere=rank).order_by("?").first()
        return self.add_power(e)

    def random_powers(self):
        self.random_power(self.rank)
        while not self.has_powers():
            self.random_power(random.randint(1, self.rank))

    def random(self, name=None, rank=None):
        super().random(rank=rank, name=name)
        self.random_powers()
        self.quintessence_max = 5 * self.rank
        self.background_cost = 2 * self.rank
        self.arete = self.rank
        while random.random() < 0.3:
            self.arete += 1
            self.background_cost += 1
            self.quintessence_max += 5


class Grimoire(Wonder):
    type = "grimoire"

    abilities = models.JSONField(default=list)
    spheres = models.JSONField(default=list)
    date_written = models.IntegerField(default=-5000)
    faction = models.ForeignKey(
        MageFaction, null=True, blank=True, on_delete=models.CASCADE
    )
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)
    is_primer = models.BooleanField(default=False)
    language = models.ForeignKey(
        Language, null=True, blank=True, on_delete=models.CASCADE
    )
    length = models.IntegerField(default=0)
    cover_material = models.ForeignKey(
        Material,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="is_cover",
    )
    inner_material = models.ForeignKey(
        Material,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="is_inner",
    )
    medium = models.ForeignKey(Medium, null=True, blank=True, on_delete=models.CASCADE)
    effects = models.ManyToManyField(Effect, blank=True)

    def set_abilities(self, abilities):
        if not isinstance(abilities, list):
            return False
        self.abilities = abilities
        return True

    def has_abilities(self):
        return self.abilities != []

    def random_abilities(self, abilities=None):
        if abilities is None:
            abilities = []
            ability_dict = {x: 1 for x in ABILITY_LIST}
            if self.practices.count() > 0:
                for practice in self.practices.all():
                    for ability in practice.abilities:
                        ability_dict[ability] += 4
            abilities.append(weighted_choice(ability_dict, ceiling=20))
            while random.random() < 0.1:
                abilities.append(
                    weighted_choice(
                        {k: v for k, v in ability_dict.items() if k not in abilities}
                    )
                )
        self.set_abilities(abilities)

    def set_date_written(self, date_written):
        self.date_written = date_written
        return True

    def has_date_written(self):
        return self.date_written != -5000

    def random_date_written(self, date_written=None):
        if date_written is None:
            if self.faction is not None:
                if self.faction.founded is not None:
                    date_written = random.randint(
                        self.faction.founded, datetime.datetime.now().year
                    )
            date_written = random.randint(
                datetime.datetime.now().year - 100, datetime.datetime.now().year
            )
        self.set_date_written(date_written)

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def random_faction(self, faction=None):
        if faction is None:
            faction = weighted_random_faction()
        self.set_faction(faction)

    def set_focus(self, paradigms, practices, instruments):
        self.paradigms.set(paradigms)
        self.practices.set(practices)
        self.instruments.set(instruments)
        self.save()
        return True

    def has_focus(self):
        return (
            self.paradigms.count() != 0
            and self.practices.count() != 0
            and self.instruments.count() != 0
        )

    def random_paradigms(self, paradigms):
        if paradigms is None:
            if self.faction is not None:
                paradigms = self.faction.get_all_paradigms()
            else:
                paradigms = Paradigm.objects.all()
            num_paradigms = 1
            while (
                random.random() < 0.1 and num_paradigms < paradigms.distinct().count()
            ):
                num_paradigms += 1
            paradigms = paradigms.order_by("?").distinct()[:num_paradigms]
        return paradigms

    def random_practices(self, practices, paradigms=None):
        if practices is None:
            if self.faction is not None:
                practices = self.faction.get_all_practices()
            else:
                practices = Practice.objects.all()
            if paradigms is not None:
                for paradigm in paradigms:
                    practices |= paradigm.practices.all()
            num_practices = 1
            while (
                random.random() < 0.25 and num_practices < practices.distinct().count()
            ):
                num_practices += 1
            practices = practices.order_by("?").distinct()[:num_practices]
        return practices

    def random_instruments(self, instruments, practices=None):
        if instruments is None:
            if practices is not None:
                instruments = Instrument.objects.none()
                for practice in practices:
                    instruments |= practice.instruments.all()
            else:
                instruments = Instrument.objects.all()
            num_instruments = 1
            while (
                random.random() < 0.3
                and num_instruments < instruments.distinct().count()
            ):
                num_instruments += 1
            instruments = instruments.order_by("?").distinct()[:num_instruments]
        return instruments

    def random_focus(self, paradigms=None, practices=None, instruments=None):
        paradigms = self.random_paradigms(paradigms)
        practices = self.random_practices(practices, paradigms=paradigms)
        instruments = self.random_instruments(instruments, practices=practices)
        self.set_focus(paradigms, practices, instruments)

    def set_language(self, language):
        self.language = language
        return True

    def has_language(self):
        return self.language is not None

    def random_language(self, language=None):
        if language is None:
            if self.faction is not None:
                if self.faction.languages.count() > 0:
                    languages = self.faction.languages.all()
                    language = weighted_choice({x: x.frequency for x in languages})
                else:
                    languages = Language.objects.all()
                    language = weighted_choice({x: x.frequency for x in languages})
            else:
                languages = Language.objects.all()
                language = weighted_choice({x: x.frequency for x in languages})
        self.set_language(language)

    def set_length(self, length):
        self.length = length
        return True

    def has_length(self):
        return self.length != 0

    def random_length(self, length=None):
        if length is None:
            length = int(200 * (random.random() + random.random()) + 50)
            if self.is_primer:
                length += 50
            if self.medium is not None:
                if self.medium.length_modifier_type == "/":
                    length /= self.medium.length_modifier
                elif self.medium.length_modifier_type == "+":
                    length += self.medium.length_modifier
                elif self.medium.length_modifier_type == "*":
                    length *= self.medium.length_modifier
                elif self.medium.length_modifier_type == "-":
                    length -= self.medium.length_modifier
            length = int(length)
        self.set_length(length)

    def set_materials(self, cover_material, inner_material):
        self.cover_material = cover_material
        self.inner_material = inner_material
        return True

    def has_materials(self):
        return self.cover_material is not None and self.inner_material is not None

    def random_material(self, cover_material=None, inner_material=None):
        if cover_material is None:
            if self.faction is None:
                if self.faction.materials.count() > 0:
                    cover_material = self.faction.materials.order_by("?").first()
                else:
                    cover_material = Material.objects.order_by("?").first()
            else:
                cover_material = Material.objects.order_by("?").first()
        if inner_material is None:
            if self.faction is None:
                if self.faction.materials.count() > 0:
                    inner_material = self.faction.materials.order_by("?").first()
                else:
                    inner_material = Material.objects.order_by("?").first()
            else:
                inner_material = Material.objects.order_by("?").first()
        self.set_materials(cover_material, inner_material)

    def set_medium(self, medium):
        self.medium = medium
        return True

    def has_medium(self):
        return self.medium is not None

    def random_medium(self, medium=None):
        if medium is None:
            if self.faction is not None:
                if self.faction.media.count() != 0:
                    medium = self.faction.media.order_by("?").first()
                else:
                    medium = Medium.objects.order_by("?").first()
            else:
                medium = Medium.objects.order_by("?").first()
        self.set_medium(medium)

    def set_rank(self, rank):
        rank = min(5, rank)
        rank = max(1, rank)
        self.rank = rank
        return True

    def has_rank(self):
        return self.rank != 0

    def random_rank(self, rank=None):
        if rank is None:
            roll = 1 / random.random()
            roll = int(math.log(roll, 10))
            rank = max(min(roll, 5), 1)
        self.set_rank(rank)

    def set_effects(self, effects):
        self.effects.set(effects)
        self.save()
        return True

    def has_effects(self):
        return self.effects.count() != 0

    def random_effects(self, effects=None):
        if effects is None:
            effects = []
            spheres = []
            if len(self.spheres) != 0:
                spheres = self.spheres

            kwargs = {f"{sphere}__gt": 0 for sphere in spheres}
            q_objects = Q()
            for key, value in kwargs.items():
                q_objects |= Q(**{key: value})
            effects = Effect.objects.filter(q_objects)

            kwargs = {f"{sphere}__lte": self.rank for sphere in SPHERE_LIST}
            for key, value in kwargs.items():
                effects = effects.filter(Q(**{key: value}))
            num_effects = 1
            while random.random() < 0.4 or num_effects < self.rank:
                num_effects += 1
            effects = list(effects.order_by("?")[:num_effects])
        self.set_effects(effects)

    def set_spheres(self, spheres):
        if not isinstance(spheres, list):
            return False
        self.spheres = spheres
        return True

    def has_spheres(self):
        return self.spheres != []

    def random_spheres(self, spheres=None):
        if spheres is None:
            spheres = []
            sphere_dict = {x: 1 for x in SPHERE_LIST}
            if self.faction is not None:
                for sphere in self.faction.affinities:
                    sphere_dict[sphere] += 1
            spheres.append(weighted_choice(sphere_dict))
            while random.random() < 0.1:
                spheres.append(
                    weighted_choice(
                        {k: v for k, v in sphere_dict.items() if k not in spheres}
                    )
                )
        self.set_spheres(spheres)

    def set_is_primer(self, is_primer):
        self.is_primer = is_primer
        return True

    def random_is_primer(self, is_primer=None):
        if is_primer is None:
            is_primer = random.random() < 0.1
        self.set_is_primer(is_primer)

    def random_name(self):
        name = ""
        if not self.has_name():
            while Grimoire.objects.filter(name=name).exists() or name == "":
                sphere = random.choice(self.spheres)
                noun = Noun.objects.order_by("?").first().name.title()
                noun2 = Noun.objects.order_by("?").first().name.title()
                resonance = (
                    Resonance.objects.filter(Q(**{sphere: True}))
                    .order_by("?")
                    .first()
                    .name.title()
                )
                sphere = sphere.title()
                forms = [
                    f"Book of {resonance} {noun}",
                    f"{resonance} {sphere} Grmoire",
                    f"{resonance} {self.medium} of {sphere}",
                    f"{noun} of {resonance} {noun2}",
                ]
                name = random.choice(forms)
            return self.set_name(name)
        return False

    def random(
        self,
        rank=None,
        is_primer=None,
        faction=None,
        paradigms=None,
        practices=None,
        instruments=None,
        date_written=None,
        medium=None,
        cover_material=None,
        inner_material=None,
        length=None,
        language=None,
        abilities=None,
        spheres=None,
        effects=None,
    ):
        self.random_rank(rank)
        self.background_cost = 2 * self.rank
        self.quintessence_max = 5 * self.rank
        self.random_is_primer(is_primer)
        self.random_faction(faction)
        self.random_medium(medium)
        self.random_material(cover_material)
        self.random_material(inner_material)
        self.random_length(length)
        self.random_focus(paradigms, practices, instruments)
        self.random_date_written(date_written)
        self.random_abilities(abilities)
        self.random_language(language)
        self.random_spheres(spheres)
        self.random_effects(effects)
        self.random_name()
        self.save()


class Library(Wonder):
    type = "library"

    faction = models.ForeignKey(
        MageFaction, null=True, blank=True, on_delete=models.CASCADE
    )
    books = models.ManyToManyField(Grimoire, blank=True)

    def add_book(self, grimoire):
        self.books.add(grimoire)
        self.save()
        return True

    def increase_rank(self, book=None):
        if book is None or book in self.books.all():
            self.rank += 1
            self.random_book()
        else:
            self.rank += 1
            self.add_book(book)

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def random_faction(self, faction=None):
        if faction is None:
            faction = weighted_random_faction()
        self.set_faction(faction)

    def random_book(self):
        book = Grimoire.objects.create(name="")
        rank = random.randint(1, self.rank)
        if (
            random.random() < 0.5
            and MageFaction.objects.filter(parent=self.faction).exists()
        ):
            f = MageFaction.objects.filter(parent=self.faction).order_by("?").first()
        else:
            f = self.faction
        book.random(rank=rank, faction=f)
        return self.add_book(book)

    def num_books(self):
        return self.books.count()

    def random(self, faction=None):
        self.random_faction(faction=faction)
        while self.num_books() < self.rank:
            self.random_book()
