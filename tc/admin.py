from django.contrib import admin

from tc.models.character.human import Human, Path, Edge, Trick, Specialty, EnhancedEdge
from tc.models.character.talent import Talent, Gift, MomentOfInspiration
from tc.models.character.aberrant import Aberrant, MegaEdge

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
