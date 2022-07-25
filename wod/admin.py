from django.contrib import admin

from wod.models.characters.human import (
    Archetype,
    Character,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    Specialty,
)
from wod.models.characters.mage import (
    Cabal,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    Rote,
)
from wod.models.characters.werewolf import (
    BattleScar,
    Camp,
    Charm,
    Gift,
    Pack,
    RenownIncident,
    Rite,
    SpiritCharacter,
    Totem,
    Tribe,
    Werewolf,
)
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.items.werewolf import Fetish
from wod.models.locations.human import City, Location
from wod.models.locations.mage import Chantry, Node, NodeMeritFlaw, Sector
from wod.models.locations.werewolf import Caern


# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Human)
class HumanCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MeritFlaw)
class MeritFlawAdmin(admin.ModelAdmin):
    list_display = ("name", "human", "garou", "mage")
    list_filter = ("human", "garou", "mage")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "stat")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "player",
        "arete",
        "affiliation",
        "faction",
        "subfaction",
        "essence",
        "affinity_sphere",
    )
    list_filter = (
        "player",
        "arete",
        "essence",
        "affinity_sphere",
    )


@admin.register(Cabal)
class CabalAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")


@admin.register(MageFaction)
class MageFactionAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


@admin.register(Paradigm)
class ParadigmAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Resonance)
class ResonanceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "correspondence",
        "entropy",
        "forces",
        "life",
        "matter",
        "mind",
        "prime",
        "spirit",
        "time",
    )


@admin.register(Rote)
class RoteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "correspondence",
        "entropy",
        "forces",
        "life",
        "matter",
        "mind",
        "prime",
        "spirit",
        "time",
    )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "parent")


@admin.register(NodeMeritFlaw)
class NodeMeritFlawAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Chantry)
class ChantryAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "parent", "faction")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Wonder)
class WonderAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "background_cost", "quintessence_max")


@admin.register(Grimoire)
class GrimoireAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "is_primer", "medium", "faction")


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "faction")


@admin.register(Totem)
class TotemAdmin(admin.ModelAdmin):
    list_display = ("name", "cost")


@admin.register(Tribe)
class TribeAdmin(admin.ModelAdmin):
    list_display = ("name", "willpower")


@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ("name", "tribe")


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "allowed")


@admin.register(Rite)
class RiteAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "type")


@admin.register(Werewolf)
class WerewolfAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "rank",
        "auspice",
        "breed",
        "tribe",
        "rage",
        "gnosis",
        "glory",
        "wisdom",
        "honor",
    )


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ("name", "leader", "totem")


@admin.register(RenownIncident)
class RenownIncidentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "glory",
        "honor",
        "wisdom",
        "posthumous",
        "only_once",
        "breed",
        "rite",
    )


@admin.register(Charm)
class CharmAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(SpiritCharacter)
class SpiritCharacterAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Fetish)
class FetishAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Caern)
class CaernAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(BattleScar)
class BattleScarAdmin(admin.ModelAdmin):
    list_display = ("name", "glory")


@admin.register(Derangement)
class DerangementAdmin(admin.ModelAdmin):
    list_display = ("name",)
