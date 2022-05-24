import math
import random

from django.db import models

from core.models import Language, Material, Medium
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

    def random_abilities(self):
        pass

    def set_date_written(self, date_written):
        self.date_written = date_written
        return True

    def has_date_written(self):
        return self.date_written != -5000

    def random_date_written(self):
        pass

    def set_faction(self, faction):
        self.faction = faction
        return True

    def has_faction(self):
        return self.faction is not None

    def random_faction(self):
        pass

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

    def random_focus(self):
        pass

    def set_language(self, language):
        self.language = language
        return True

    def has_language(self):
        return self.language is not None

    def random_language(self):
        pass

    def set_length(self, length):
        self.length = length
        return True

    def has_length(self):
        return self.length != 0

    def random_length(self):
        pass

    def set_materials(self, cover_material, inner_material):
        self.cover_material = cover_material
        self.inner_material = inner_material
        return True

    def has_materials(self):
        return self.cover_material is not None and self.inner_material is not None

    def random_material(self):
        pass

    def set_medium(self, medium):
        self.medium = medium
        return True

    def has_medium(self):
        return self.medium is not None

    def random_medium(self):
        pass

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

    def random_rotes(self):
        pass

    def set_spheres(self, spheres):
        if not isinstance(spheres, list):
            return False
        self.spheres = spheres
        return True

    def has_spheres(self):
        return self.spheres != []

    def random_spheres(self):
        pass

    def set_is_primer(self, is_primer):
        self.is_primer = is_primer
        return True

    def random_is_primer(self):
        pass

    def random(self, rank=None):
        pass


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
