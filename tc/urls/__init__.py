from django.urls import include, path

from tc import views

from . import characters, items, locations

# Create your URLs here
urlpatterns = [
    path("characters/", include((characters.urls, "wod"), namespace="characters")),
    path("items/", include((items.urls, "wod"), namespace="items")),
    path("locations/", include((locations.urls, "wod"), namespace="locations")),
]
