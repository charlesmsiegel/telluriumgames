from django.contrib import admin

from exalted.models.characters.mortals import ExMerit, ExMortal, ExSpecialty, Intimacy
from exalted.models.characters.solars import (
    MartialArtsCharm,
    MartialArtsStyle,
    Solar,
    SolarCharm,
)


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


admin.site.register(SolarCharm)
admin.site.register(MartialArtsCharm)
admin.site.register(MartialArtsStyle)
