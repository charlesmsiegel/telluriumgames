from django.urls import include, path

from . import characters, items, locations

from wod import views

# Create your URLs here
urlpatterns = [
    path("characters/", include((characters.urls, "wod"), namespace="characters")),
    path("items/", include((items.urls, "wod"), namespace="items")),
    path("locations/", include((locations.urls, "wod"), namespace="locations")),
    path("ajax/load_faction_details/", views.load_factions, name="ajax_load_factions"),
    path(
        "ajax/load_subfaction_details/",
        views.load_subfactions,
        name="ajax_load_subfactions",
    ),
    path(
        "ajax/load-character-types/",
        views.load_character_types,
        name="ajax_load_character_types",
    ),
    path("groups/<pk>/", views.GenericGroupDetailView.as_view(), name="group"),
    path("archetypes/<pk>/", views.ArchetypeDetailView.as_view(), name="archetype"),
    path("camps/<pk>/", views.CampDetailView.as_view(), name="camp"),
    path("charms/<pk>/", views.CharmDetailView.as_view(), name="charm"),
    path("gifts/<pk>/", views.GiftDetailView.as_view(), name="gift"),
    path("instruments/<pk>/", views.InstrumentDetailView.as_view(), name="instrument"),
    path(
        "magefactions/<pk>/", views.MageFactionDetailView.as_view(), name="magefaction"
    ),
    path("meritflaws/<pk>/", views.MeritFlawDetailView.as_view(), name="meritflaw"),
    path("paradigms/<pk>/", views.ParadigmDetailView.as_view(), name="paradigm"),
    path("practices/<pk>/", views.PracticeDetailView.as_view(), name="practice"),
    path(
        "renownincidents/<pk>/",
        views.RenownIncidentDetailView.as_view(),
        name="renownincident",
    ),
    path("resonances/<pk>/", views.ResonanceDetailView.as_view(), name="resonance"),
    path("rites/<pk>/", views.RiteDetailView.as_view(), name="rite"),
    path("rotes/<pk>/", views.RoteDetailView.as_view(), name="rote"),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
    path("totems/<pk>/", views.TotemDetailView.as_view(), name="totem"),
    path("tribes/<pk>/", views.TribeDetailView.as_view(), name="tribe"),
]
