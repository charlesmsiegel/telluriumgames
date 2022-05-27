from django.contrib import admin

from wod.models.characters.human import Archetype, Character, Human
from wod.models.characters.mage import (
    Instrument,
    Mage,
    MageFaction,
    Paradigm,
    Practice,
    Resonance,
    Rote,
)
from wod.models.items.human import Item
from wod.models.items.mage import Grimoire, Library, Wonder
from wod.models.locations.human import City, Location
from wod.models.locations.mage import Node, NodeMeritFlaw

# Register your models here.
# @admin.register(Character)
# class CharacterAdmin(admin.ModelAdmin):
#     list_display = ("name", "player", "status")


# @admin.register(Human)
# class HumanCharacterAdmin(admin.ModelAdmin):
#     list_display = ("name", "player", "status")


# @admin.register(Mage)
# class MageAdmin(admin.ModelAdmin):
#     list_display = ("name", "player", "status", "arete", "faction")


# @admin.register(MageFaction)
# class MageFactionAdmin(admin.ModelAdmin):
#     list_display = ("name", "parent")


# @admin.register(Paradigm)
# class ParadigmAdmin(admin.ModelAdmin):
#     list_display = ("name",)


# @admin.register(Practice)
# class PracticeAdmin(admin.ModelAdmin):
#     list_display = ("name",)


# @admin.register(Instrument)
# class InstrumentAdmin(admin.ModelAdmin):
#     list_display = ("name",)


# @admin.register(Resonance)
# class ResonanceAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "correspondence",
#         "entropy",
#         "forces",
#         "life",
#         "matter",
#         "mind",
#         "prime",
#         "spirit",
#         "time",
#     )

# @admin.register(Rote)
# class RoteAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "correspondence",
#         "entropy",
#         "forces",
#         "life",
#         "matter",
#         "mind",
#         "prime",
#         "spirit",
#         "time",
#     )

# admin.site.register(Location)
# admin.site.register(City)
# admin.site.register(Node)


# @admin.register(Wonder)
# class WonderAdmin(admin.ModelAdmin):
#     list_display = ("name", "rank", "background_cost", "quintessence_max")


# @admin.register(Grimoire)
# class GrimoireAdmin(admin.ModelAdmin):
#     list_display = ("name", "rank", "primer", "medium")


# admin.site.register(Library)
