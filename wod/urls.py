from django.urls import path

from wod import views

# Create your URLs here
urlpatterns = [
    path("characters/", views.CharacterIndexView.as_view(), name="characters_index"),
    path(
        "characters/random/",
        views.RandomCharacterView.as_view(),
        name="random_character",
    ),
    path(
        "characters/<pk>/", views.GenericCharacterDetailView.as_view(), name="character"
    ),
    path("locations/", views.LocationIndexView.as_view(), name="location_index"),
    path(
        "locations/random/", views.RandomLocationView.as_view(), name="random_location"
    ),
    path("locations/<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
    path("items/", views.ItemIndexView.as_view(), name="item_index"),
    path("items/random/", views.RandomItemView.as_view(), name="random_item"),
    path("items/<pk>/", views.GenericItemDetailView.as_view(), name="item"),
]
