from django.contrib import admin

from cod.models.characters.mortal import Merit, Mortal, Specialty
from cod.models.characters.mage import Mage, ProximiFamily, Proximi


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

admin.site.register(Mage)
admin.site.register(Proximi)
admin.site.register(ProximiFamily)
