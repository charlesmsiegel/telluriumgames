import datetime
import math
import random
from typing import List

from core.models import Language, Material, Medium
from django.db import models
from django.db.models import Q
from polymorphic.models import PolymorphicModel
from wod.models.characters.mage import (
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Rote,
)


# Create your models here.
class Wonder(PolymorphicModel):
    """Class for the Wonder model."""

    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=1)
    background_cost = models.IntegerField(default=0)
    quintessence_max = models.IntegerField(default=0)
    description = models.TextField(default="")
    type = "wonder"

    def __str__(self):
        return self.name


class Grimoire(Wonder):
    """Class for the Grimoire model."""

    faction = models.ForeignKey(
        MageFaction, on_delete=models.CASCADE, null=True, blank=True
    )
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE, null=True, blank=True)
    primer = models.BooleanField(default=False)
    paradigms = models.ManyToManyField(Paradigm, blank=True)
    practices = models.ManyToManyField(Practice, blank=True)
    instruments = models.ManyToManyField(Instrument, blank=True)
    length = models.IntegerField(null=True, blank=True)
    cover_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="cover_of",
    )
    inner_material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="inside_of",
    )
    date_written = models.IntegerField(default=2021, null=True, blank=True)
    spheres = models.JSONField(null=True)
    abilities = models.JSONField(null=True)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=True, blank=True
    )
    rotes = models.ManyToManyField(Rote, blank=True)

    type = "grimoire"

    def random_faction(self, faction):
        if faction is not None:
            return faction
        return MageFaction.objects.order_by("?").first()

    def random_primer(self, primer):
        if primer is None:
            if random.random() < 0.1:
                return True
            return False
        return primer

    def random_rank(self, rank):
        if rank is None:
            roll = 1 / random.random()
            roll = int(math.log(roll, 10))
            return max(min(roll, 5), 1)
        return rank

    def random_time_written(self, date_written):
        if date_written is None:
            if self.faction is not None:
                if self.faction.founded is not None:
                    date_written = random.choice(
                        range(self.faction.founded, datetime.datetime.now().year + 1)
                    )
            date_written = random.choice(
                range(
                    datetime.datetime.now().year - 100, datetime.datetime.now().year + 1
                )
            )
        return date_written

    def random_medium(self, medium):
        if medium is None:
            if self.faction.media.count() != 0:
                return self.faction.media.order_by("?").first()
            else:
                return Medium.objects.order_by("?").first()
        return medium

    def random_material(self, material):
        if material is None:
            if self.faction.materials.count() > 0:
                return self.faction.materials.order_by("?").first()
            else:
                return Material.objects.order_by("?").first()
        return material

    def random_focus(self, paradigms, practices, instruments):
        if paradigms is None:
            paradigms = []
            options = []
            if self.faction is not None:
                current = self.faction
                while current is not None:
                    options.extend(current.paradigms.all())
                    current = current.parent
            options *= 4
            options.extend(Paradigm.objects.all())
            paradigms.append(random.choice(options))
            while random.random() < 0.1 and len(options) > 0:
                options = [x for x in options if x not in paradigms]
                if len(options) != 0:
                    paradigms.append(random.choice(options))
        if practices is None:
            practices = []
            options = []
            for para in paradigms:
                options.extend(para.practices.all())
            if self.faction is not None:
                current = self.faction
                while current is not None:
                    options.extend(current.practices.all())
                    current = current.parent
            options *= 4
            options.extend(Practice.objects.all())
            practices.append(random.choice(options))
            while random.random() < 0.25 and len(options) > 0:
                options = [x for x in options if x not in practices]
                if len(options) != 0:
                    practices.append(random.choice(options))
        if instruments is None:
            instruments = []
            options = []
            for practice in practices:
                options.extend(practice.instruments.all())
            options *= 4
            options.extend(Instrument.objects.all())
            instruments.append(random.choice(options))
            while random.random() < 0.3 and len(options) > 0:
                options = [x for x in options if x not in instruments]
                if len(options) != 0:
                    instruments.append(random.choice(options))
        return paradigms, practices, instruments

    def random_length(self, length):
        if length is None:
            length = int(200 * (random.random() + random.random()) + 50)
            if self.primer:
                length += 50
            if self.medium.length_modifier_type == "division":
                length /= self.medium.length_modifier
            elif self.medium.length_modifier_type == "addition":
                length += self.medium.length_modifier
            else:
                raise ValueError("Unknown length modifier type")
            return int(length)
        return int(length)

    def random_language(self, language):
        if language is None:
            if self.faction.languages.count() > 0:
                return self.faction.languages.order_by("?").first()
            return Language.objects.order_by("?").first()
        return language

    def random_abilities(self, abilities):
        if abilities is None:
            abilities = []
            all_abilities = Mage.talents() + Mage.skills() + Mage.knowledges()
            if self.practices.count() > 0:
                for practice in self.practices.all():
                    all_abilities.extend(practice.abilities)
            ability = random.choice(all_abilities)
            abilities.append(ability)
            while random.random() < 0.1:
                all_abilities = [x for x in all_abilities if x != ability]
                ability = random.choice(all_abilities)
                abilities.append(ability)
            return abilities
        return abilities

    def random_spheres(self, spheres):
        if spheres is None:
            full_list = [
                "correspondence",
                "time",
                "spirit",
                "mind",
                "entropy",
                "prime",
                "forces",
                "matter",
                "life",
            ]
            spheres = []
            if self.faction is not None:
                if self.faction.parent is not None:
                    if self.faction.parent.name == "Technocratic Union":
                        full_list.extend(
                            ["data", "dimensional_science", "primal_utility"]
                        )
                if self.faction.name == "Virtual Adepts":
                    full_list.append("data")
            sphere = random.choice(full_list)
            spheres.append(sphere)
            while random.random() < 0.1:
                full_list = [x for x in full_list if x != sphere]
                sphere = random.choice(full_list)
                spheres.append(sphere)
            return spheres
        return spheres

    def random_rotes(self, rotes):
        if rotes is None:
            rotes = []
            spheres = self.spheres
            if "data" in spheres:
                spheres.remove("data")
                spheres.append("correspondence")
            if "primal_utility" in spheres:
                spheres.remove("primal_utility")
                spheres.append("prime")
            if "dimensional_science" in spheres:
                spheres.remove("dimensional_science")
                spheres.append("spirit")
            all_rotes = Rote.objects.all()

            kwargs = {f"{sphere}__gt": 0 for sphere in spheres}
            q_objects = Q()  # Create an empty Q object to start with
            for key, value in kwargs.items():
                q_objects |= Q(**{key: value})
            rotes = all_rotes.filter(q_objects)

            spheres = [
                "correspondence",
                "time",
                "spirit",
                "mind",
                "entropy",
                "prime",
                "forces",
                "matter",
                "life",
            ]
            kwargs = {f"{sphere}__lte": self.rank for sphere in spheres}
            for key, value in kwargs.items():
                rotes = rotes.filter(Q(**{key: value}))
            num_rotes = 1
            while random.random() < 0.4 or num_rotes < self.rank:
                num_rotes += 1
            return list(rotes.order_by("?")[:num_rotes])
        return rotes

    def random(
        self,
        rank=None,
        primer=None,
        faction=None,
        paradigms=None,
        practices=None,
        instruments=None,
        year_written=None,
        medium=None,
        cover_material=None,
        inner_material=None,
        length=None,
        language=None,
        abilities=None,
        spheres=None,
        rotes=None,
    ):
        self.rank = self.random_rank(rank)
        self.background_cost = 2 * self.rank
        self.quintessence_max = 5 * self.rank
        self.primer = self.random_primer(primer)
        self.faction = self.random_faction(faction)
        self.medium = self.random_medium(medium)
        self.save()
        self.cover_material = self.random_material(cover_material)
        self.inner_material = self.random_material(inner_material)
        self.length = self.random_length(length)
        paradigms, practices, instruments = self.random_focus(
            paradigms, practices, instruments
        )
        self.paradigms.add(*paradigms)
        self.practices.add(*practices)
        self.instruments.add(*instruments)
        self.date_written = self.random_time_written(year_written)
        self.abilities = self.random_abilities(abilities)
        self.language = self.random_language(language)
        self.spheres = self.random_spheres(spheres)
        self.rotes.set(self.random_rotes(rotes))
        self.save()


class Library(models.Model):
    """Class for the Library model."""

    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=1)
    books = models.ManyToManyField(Grimoire, blank=True)

    def __len__(self):
        return self.books.count()

    def increase_size(self, book):
        if book is None:
            book = Grimoire(name=f"Book {len(self)}")
            book.save()
            book.random(rank=self.rank + 1)
            book.save()
        self.books.add(book)
        self.rank += 1
        self.save()
