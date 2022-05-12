from django.contrib import admin
from tc.models import (
    Aberrant,
    AttributePrereq,
    Edge,
    EdgePrereq,
    EdgeRating,
    EnhancedEdge,
    MegaAttributePrereq,
    MegaEdge,
    MegaEdgeRating,
    Path,
    PathConnection,
    PathConnectionRating,
    Power,
    PowerRating,
    SkillPrereq,
    Tag,
    TagRating,
    Transformation,
    Trick,
)

# Register your models here.
admin.site.register(Aberrant)
admin.site.register(Trick)
admin.site.register(Edge)
admin.site.register(EnhancedEdge)
admin.site.register(MegaEdge)
admin.site.register(Path)
admin.site.register(PathConnection)
admin.site.register(PathConnectionRating)
admin.site.register(Tag)
admin.site.register(Power)
admin.site.register(Transformation)
admin.site.register(EdgeRating)
admin.site.register(MegaEdgeRating)
admin.site.register(PowerRating)
admin.site.register(TagRating)
admin.site.register(AttributePrereq)
admin.site.register(MegaAttributePrereq)
admin.site.register(SkillPrereq)
admin.site.register(EdgePrereq)
