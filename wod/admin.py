from django.contrib import admin

from wod.models.characters import (
    Cabal,
    Character,
    HumanCharacter,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    ResRating,
)
from wod.models.locations import City, Location, Node
from wod.models.objects.mage import Grimoire, Library, Wonder


# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """ Class controlling the display of Character in admin site """

    list_display = ("name", "player", "status")


@admin.register(HumanCharacter)
class HumanCharacterAdmin(admin.ModelAdmin):
    """ Class controlling the display of HumanCharacter in admin site """

    list_display = ("name", "player", "status")


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    """ Class controlling the display of Mage in admin site """

    list_display = ("name", "player", "status", "arete", "faction")


@admin.register(MageFaction)
class MageFactionAdmin(admin.ModelAdmin):
    """ Class controlling the display of MageFaction in admin site """

    list_display = ("name", "parent")


@admin.register(Paradigm)
class ParadigmAdmin(admin.ModelAdmin):
    """ Class controlling the display of Paradigm in admin site """

    list_display = ("name",)


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    """ Class controlling the display of Practice in admin site """

    list_display = ("name",)


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    """ Class controlling the display of Instrument in admin site """

    list_display = ("name",)


@admin.register(Resonance)
class ResonanceAdmin(admin.ModelAdmin):
    """ Class controlling the display of Resonance in admin site """

    list_display = (
        "name",
        # "correspondence",
        # "entropy",
        # "forces",
        # "life",
        # "matter",
        # "mind",
        # "prime",
        # "spirit",
        # "time",
        # "data",
        # "dimensional_science",
        # "primal_utility",
    )


@admin.register(ResRating)
class ResRatingAdmin(admin.ModelAdmin):
    """ Class controlling the display of ResRating in admin site """

    list_display = ("mage", "resonance", "rating")


@admin.register(Cabal)
class CabalAdmin(admin.ModelAdmin):
    """ Class controlling the display of Cabal in admin site """

    list_display = ("name", "leader")


admin.site.register(Location)
admin.site.register(City)
admin.site.register(Node)

@admin.register(Wonder)
class WonderAdmin(admin.ModelAdmin):
    """Class for Wonder admin."""

    list_display = ("name", "rank", "background_cost", "quintessence_max")


@admin.register(Grimoire)
class GrimoireAdmin(admin.ModelAdmin):
    """Class for Grimoire admin."""

    list_display = ("name", "rank", "primer", "medium")


admin.site.register(Library)
