import datetime
import math
import random

from django.db import models

from core.models import Language, Material, Medium
from core.utils import weighted_choice
from wod.models.characters.mage import Instrument, MageFaction, Paradigm, Practice, Rote
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
        pass

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
                        self.faction.founded, datetime.datetime.now().year + 1
                    )
            date_written = random.randint(
                datetime.datetime.now().year - 100, datetime.datetime.now().year + 1
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

    def random_focus(self, paradigms=None, practices=None, instruments=None):
        pass

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
                else:
                    languages = Language.objects.all()
            else:
                languages = Language.objects.all()
        else:
            language = weighted_choice({x: x.frequency for x in languages})
        self.set_language(language)

    def set_length(self, length):
        self.length = length
        return True

    def has_length(self):
        return self.length != 0

    def random_length(self, length=None):
        pass

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
        pass

    def set_spheres(self, spheres):
        if not isinstance(spheres, list):
            return False
        self.spheres = spheres
        return True

    def has_spheres(self):
        return self.spheres != []

    def random_spheres(self, spheres=None):
        pass

    def set_is_primer(self, is_primer):
        self.is_primer = is_primer
        return True

    def random_is_primer(self, is_primer=None):
        if is_primer is None:
            if random.random() < 0.1:
                is_primer = True
            is_primer = False
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
