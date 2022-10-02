import imp

from django.contrib import admin

from exalted.models.characters.charms import (
    DragonBloodedCharm,
    MartialArtsCharm,
    MartialArtsStyle,
    SolarCharm,
)
from exalted.models.characters.dragonblooded import DragonBlooded
from exalted.models.characters.mortals import ExMerit, ExMortal, ExSpecialty, Intimacy, MeritRating
from exalted.models.characters.solars import Solar
from exalted.models.locations.mortals import ExLocation


# Register your models here.
@admin.register(ExMortal)
class MortalAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(ExSpecialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "ability")


@admin.register(Intimacy)
class IntimacyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "strength", "is_negative")


@admin.register(ExMerit)
class MeritAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "merit_class")


@admin.register(Solar)
class SolarAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "caste")


@admin.register(DragonBlooded)
class DragonBloodedAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "aspect")


admin.site.register(SolarCharm)
admin.site.register(DragonBloodedCharm)
admin.site.register(MartialArtsCharm)
admin.site.register(MartialArtsStyle)
admin.site.register(ExLocation)
admin.site.register(MeritRating)
