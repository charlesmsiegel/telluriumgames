from django.contrib import admin

from cod.models.characters.mage import Legacy, Mage, Order, Path, Proximi, ProximiFamily
from cod.models.characters.mortal import Merit, Mortal, Specialty


# Register your models here.
@admin.register(Mortal)
class MortalProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Specialty)
class SpecialtyProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "skill")


@admin.register(Merit)
class MeritProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "ratings")


@admin.register(Mage)
class MageProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "path", "order", "gnosis")


@admin.register(Proximi)
class ProximiProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "family")


@admin.register(ProximiFamily)
class ProximiFamilyProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "path", "blessing_arcana")


@admin.register(Path)
class PathProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "ruling_arcana", "inferior_arcanum")


@admin.register(Order)
class OrderProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "rote_skills")


@admin.register(Legacy)
class LegacyProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "ruling_arcanum", "is_left_handed")
