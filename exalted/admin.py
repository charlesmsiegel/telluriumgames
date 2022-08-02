from django.contrib import admin

from exalted.models.characters.mortals import ExMortal, Intimacy, Merit, Specialty


# Register your models here.
@admin.register(ExMortal)
class MortalAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "ability")


@admin.register(Intimacy)
class IntimacyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "strength", "is_negative")


@admin.register(Merit)
class MeritAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "merit_class")
