from django.urls import path

from wod import views

# Create your URLs here
urlpatterns = [
    path("characters/", views.CharacterIndexView.as_view(), name="characters_index"),
    path(
        "characters/<pk>/", views.GenericCharacterDetailView.as_view(), name="character"
    ),
    path("locations/", views.LocationIndexView.as_view(), name="location_index"),
    path("locations/<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
    path("items/<pk>/", views.GenericItemDetailView.as_view(), name="item"),
    path("items/", views.ItemIndexView.as_view(), name="item_index"),
]
