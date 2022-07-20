from django.urls import include, path

from wod import views

from . import characters, items, locations

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
]
