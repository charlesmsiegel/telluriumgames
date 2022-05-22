from django.db import models
from polymorphic.models import PolymorphicModel

from core.models import Language, Material, Medium
from wod.models.character.mage import Instrument, MageFaction, Paradigm, Practice, Rote


# Create your models here.
class Wonder(PolymorphicModel):
    type = "wonder"

    name = models.CharField(max_length=100, unique=True)
    rank = models.IntegerField(default=0)
    background_cost = models.IntegerField(default=0)
    quintessence_max = models.IntegerField(default=0)


class Grimoire(Wonder):
    type = "grimoire"

    abilities = models.JSONField(default=list)
    spheres = models.JSONField(default=list)
    date_written = models.IntegerField(default=2022)
    faction = models.ForeignKey(
        MageFaction, null=True, blank=True, on_delete=models.CASCADE
    )
    paradigms = models.ForeignKey(
        Paradigm, null=True, blank=True, on_delete=models.CASCADE
    )
    practices = models.ForeignKey(
        Practice, null=True, blank=True, on_delete=models.CASCADE
    )
    instruments = models.ForeignKey(
        Instrument, null=True, blank=True, on_delete=models.CASCADE
    )
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
        pass

    def has_abilities(self):
        pass

    def random_abilities(self):
        pass

    def set_date_written(self, date_written):
        pass

    def has_date_written(self):
        pass

    def random_date_written(self):
        pass

    def set_faction(self, faction):
        pass

    def has_faction(self):
        pass

    def random_faction(self):
        pass

    def set_focus(self, paradigms, practices, instruments):
        pass

    def has_focus(self):
        pass

    def random_focus(self):
        pass

    def set_language(self, language):
        pass

    def has_language(self):
        pass

    def random_language(self):
        pass

    def set_length(self, length):
        pass

    def has_length(self):
        pass

    def random_length(self):
        pass

    def set_materials(self, cover_material, inner_material):
        pass

    def has_materials(self):
        pass

    def random_material(self):
        pass

    def set_medium(self, medium):
        pass

    def has_medium(self):
        pass

    def random_medium(self):
        pass

    def set_rank(self, rank):
        pass

    def has_rank(self):
        pass

    def random_rank(self):
        pass

    def set_rotes(self, rotes):
        pass

    def has_rotes(self):
        pass

    def random_rotes(self):
        pass

    def set_spheres(self, spheres):
        pass

    def has_spheres(self):
        pass

    def random_spheres(self):
        pass

    def set_is_primer(self, is_primer):
        pass

    def random_is_primer(self):
        pass

    def random(self):
        pass


class Library(Wonder):
    type = "library"
    books = models.ManyToManyField(Grimoire, blank=True)

    def add_book(self, grimoire):
        pass

    def increase_rank(self):
        pass

    def __len__(self):
        return 0
