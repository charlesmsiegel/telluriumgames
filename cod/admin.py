from django.contrib import admin

from cod.models.character.mortal import Merit, Mortal, Specialty


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
