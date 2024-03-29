from django.contrib import admin

from wod.models.characters.changeling import (
    Changeling,
    CtDHuman,
    CtDLegacy,
    House,
    Kith,
    Motley,
)
from wod.models.characters.human import (
    Archetype,
    Character,
    Derangement,
    Group,
    Human,
    MeritFlaw,
    MeritFlawRating,
    WoDSpecialty,
)
from wod.models.characters.mage import (
    Cabal,
    Effect,
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    ResRating,
    Rote,
)
from wod.models.characters.mage.mtahuman import MtAHuman
from wod.models.characters.vampire import VtMHuman
from wod.models.characters.werewolf import (
    BattleScar,
    Camp,
    Fomor,
    FomoriPower,
    Gift,
    Kinfolk,
    Pack,
    RenownIncident,
    Rite,
    SpiritCharacter,
    SpiritCharm,
    Totem,
    Tribe,
    Werewolf,
    wtahuman,
)
from wod.models.characters.werewolf.wtahuman import WtAHuman
from wod.models.characters.wraith import WtOHuman
from wod.models.items.human import (
    MeleeWeapon,
    RangedWeapon,
    ThrownWeapon,
    Weapon,
    WoDItem,
)
from wod.models.items.mage import (
    Artifact,
    Charm,
    Grimoire,
    Talisman,
    Wonder,
    WonderResonanceRating,
)
from wod.models.items.werewolf import Fetish
from wod.models.locations.human import City, Location
from wod.models.locations.mage import (
    Chantry,
    HorizonRealm,
    Library,
    Node,
    NodeMeritFlaw,
    NodeMeritFlawRating,
    NodeResonanceRating,
    Sector,
)
from wod.models.locations.werewolf import Caern


# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "chronicle")


@admin.register(Human)
class HumanCharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "chronicle")


@admin.register(Archetype)
class ArchetypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MeritFlaw)
class MeritFlawAdmin(admin.ModelAdmin):
    list_display = ("name", "human", "garou", "mage")
    list_filter = ("human", "garou", "mage")


@admin.register(WoDSpecialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "stat")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "leader", "chronicle")


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "arete",
        "affiliation",
        "faction",
        "subfaction",
        "essence",
        "affinity_sphere",
        "chronicle",
    )
    list_filter = ("owner", "arete", "essence", "affinity_sphere", "chronicle")


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


@admin.register(Effect)
class EffectAdmin(admin.ModelAdmin):
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


@admin.register(WoDItem)
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
    list_display = ("name", "rank", "faction", "parent")


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


@admin.register(Kinfolk)
class KinfolkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "breed",
        "tribe",
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


@admin.register(SpiritCharm)
class SpiritCharmAdmin(admin.ModelAdmin):
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


@admin.register(Fomor)
class FomorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(FomoriPower)
class FomoriPowerAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Weapon)
admin.site.register(RangedWeapon)
admin.site.register(MeleeWeapon)
admin.site.register(ThrownWeapon)


@admin.register(Changeling)
class ChangelingAdmin(admin.ModelAdmin):
    list_display = ("name", "kith")


admin.site.register(CtDLegacy)
admin.site.register(CtDHuman)
admin.site.register(House)
admin.site.register(Kith)
admin.site.register(Motley)
admin.site.register(MeritFlawRating)
admin.site.register(ResRating)
admin.site.register(Rote)
admin.site.register(WonderResonanceRating)
admin.site.register(Charm)
admin.site.register(Talisman)
admin.site.register(Artifact)
admin.site.register(NodeMeritFlawRating)
admin.site.register(NodeResonanceRating)
admin.site.register(MtAHuman)
admin.site.register(WtAHuman)
admin.site.register(HorizonRealm)
admin.site.register(VtMHuman)
admin.site.register(WtOHuman)
