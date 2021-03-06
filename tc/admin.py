from django.contrib import admin

from tc.models.characters.aberrant import Aberrant, MegaEdge, Power, Tag, Transformation
from tc.models.characters.human import (
    Edge,
    EnhancedEdge,
    Human,
    Path,
    PathConnection,
    Specialty,
    Trick,
)
from tc.models.characters.talent import Gift, MomentOfInspiration, Talent


# Register your models here.
@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ("name", "player")


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


@admin.register(Edge)
class EdgeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Trick)
class TrickAdmin(admin.ModelAdmin):
    list_display = ("name", "skill")


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "skill")


@admin.register(EnhancedEdge)
class EnhancedEdgeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PathConnection)
class PathConnectionAdmin(admin.ModelAdmin):
    list_display = ("name", "path")


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "intuitive", "reflective", "destructive")


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(MomentOfInspiration)
class MomentOfInspirationAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Aberrant)
class AberrantAdmin(admin.ModelAdmin):
    list_display = ("name", "player", "quantum", "flux", "transcendence")


@admin.register(MegaEdge)
class MegaEdgeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Transformation)
class TransformationAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
