from cod.models import Merit, Mortal, Specialty
from django.contrib import admin

# Register your models here.
@admin.register(Mortal)
class MortalProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "status")


@admin.register(Specialty)
class SpecialtyProfileAdmin(admin.ModelAdmin):
    list_display = ("specialty", "skill")


@admin.register(Merit)
class MeritProfileAdmin(admin.ModelAdmin):
    pass
