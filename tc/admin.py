from django.contrib import admin

from tc.models.character.aberrant import Aberrant, MegaEdge, Power, Tag, Transformation
from tc.models.character.human import Edge, EnhancedEdge, Human, Path, Specialty, Trick
from tc.models.character.talent import Gift, MomentOfInspiration, Talent

# Register your models here.
admin.site.register(Human)
admin.site.register(Path)
admin.site.register(Edge)
admin.site.register(Trick)
admin.site.register(Specialty)
admin.site.register(EnhancedEdge)
admin.site.register(Talent)
admin.site.register(Gift)
admin.site.register(MomentOfInspiration)
admin.site.register(Aberrant)
admin.site.register(MegaEdge)
admin.site.register(Power)
admin.site.register(Tag)
admin.site.register(Transformation)
