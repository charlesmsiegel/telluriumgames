import datetime
import math
import random
from tkinter import N

from django.db import models
from django.db.models import Q

from core.models import Language, Material, Medium
from core.utils import weighted_choice
from wod.models.characters.mage import (
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Rote,
)
from wod.models.items.human import Item


# Create your models here.
class Wonder(Item):
    type = "wonder"

    rank = models.IntegerField(default=0)
    background_cost = models.IntegerField(default=0)
    quintessence_max = models.IntegerField(default=0)


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
    rotes = models.ManyToManyField(Rote, blank=True)

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
            ability_dict = Mage(name="TMP").get_abilities()
            if self.practices.count() > 0:
                for practice in self.practices.all():
                    for ability in practice.abilities:
                        ability_dict[ability] += 1
            abilities.append(weighted_choice(ability_dict))
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
            faction = MageFaction.objects.order_by("?").first()
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

    def set_rotes(self, rotes):
        self.rotes.set(rotes)
        self.save()
        return True

    def has_rotes(self):
        return self.rotes.count() != 0

    def random_rotes(self, rotes=None):
        if rotes is None:
            rotes = []
            spheres = []
            if len(self.spheres) != 0:
                spheres = self.spheres

            kwargs = {f"{sphere}__gt": 0 for sphere in spheres}
            q_objects = Q()
            for key, value in kwargs.items():
                q_objects |= Q(**{key: value})
            rotes = Rote.objects.filter(q_objects)

            kwargs = {
                f"{sphere}__lte": self.rank for sphere in Mage(name="TMP").get_spheres()
            }
            for key, value in kwargs.items():
                rotes = rotes.filter(Q(**{key: value}))
            num_rotes = 1
            while random.random() < 0.4 or num_rotes < self.rank:
                num_rotes += 1
            rotes = list(rotes.order_by("?")[:num_rotes])
        self.set_rotes(rotes)

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
            sphere_dict = Mage(name="TMP").get_spheres()
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
        rotes=None,
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
        self.random_rotes(rotes)
        self.save()


class Library(Wonder):
    type = "library"

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

    def random_book(self):
        book = Grimoire.objects.create(name=f"Random Book {self.num_books() + 1}")
        book.random(rank=self.rank)
        return self.add_book(book)

    def num_books(self):
        return self.books.count()
