from django.contrib import admin

from cod.models.characters.mage import Legacy, Mage, Order, Path, Proximi, ProximiFamily
from cod.models.characters.mortal import Merit, Mortal, Specialty, Tilt


# Register your models here.
@admin.register(Mortal)
class MortalAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "skill")


@admin.register(Merit)
class MeritAdmin(admin.ModelAdmin):
    list_display = ("name", "ratings")


@admin.register(Mage)
class MageAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "path", "order", "gnosis")


@admin.register(Proximi)
class ProximiAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "family")


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
