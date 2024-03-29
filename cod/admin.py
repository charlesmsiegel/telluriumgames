from django.contrib import admin

from cod.models.characters.ephemera import Ephemera, Numina
from cod.models.characters.mage import (
    Attainment,
    CoDRote,
    KnownPraxis,
    KnownRote,
    Legacy,
    Mage,
    Order,
    Path,
    Proximi,
    ProximiFamily,
)
from cod.models.characters.mortal import (
    CoDMerit,
    CoDSpecialty,
    Condition,
    MeritRating,
    Mortal,
    Tilt,
)
from cod.models.items.mortal import Equipment, Item

# Register your models here.
admin.site.register(Attainment)
admin.site.register(CoDRote)
admin.site.register(KnownPraxis)
admin.site.register(KnownRote)
admin.site.register(MeritRating)
admin.site.register(Condition)
admin.site.register(Ephemera)


@admin.register(Mortal)
class MortalAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")


@admin.register(CoDSpecialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "skill")


@admin.register(CoDMerit)
class MeritAdmin(admin.ModelAdmin):
    list_display = ("name", "ratings")


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "path", "order", "gnosis")


@admin.register(Proximi)
class ProximiAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "family")


@admin.register(ProximiFamily)
class ProximiFamilyAdmin(admin.ModelAdmin):
    list_display = ("name", "path", "blessing_arcana")


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ("name", "ruling_arcana", "inferior_arcanum")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "rote_skills")


@admin.register(Legacy)
class LegacyAdmin(admin.ModelAdmin):
    list_display = ("name", "ruling_arcanum", "is_left_handed")


@admin.register(Tilt)
class TiltAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Item)
admin.site.register(Equipment)
admin.site.register(Numina)
