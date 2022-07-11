from django.urls import path

from wod import views

# Create your URLs here
urlpatterns = [
    path(
        "locations/create/location/",
        views.LocationCreateView.as_view(),
        name="create_location",
    ),
    path("locations/create/city/", views.CityCreateView.as_view(), name="create_city"),
    path("locations/create/node/", views.NodeCreateView.as_view(), name="create_node"),
    path(
        "locations/create/chantry/",
        views.ChantryCreateView.as_view(),
        name="create_chantry",
    ),
    path(
        "items/create/grimoire/",
        views.GrimoireCreateView.as_view(),
        name="create_grimoire",
    ),
    path("items/create/item/", views.ItemCreateView.as_view(), name="create_item"),
    path(
        "items/create/wonder/", views.WonderCreateView.as_view(), name="create_wonder"
    ),
    path(
        "items/create/library/",
        views.LibraryCreateView.as_view(),
        name="create_library",
    ),
    path(
        "characters/create/cabal/", views.CabalCreateView.as_view(), name="create_cabal"
    ),
    path(
        "characters/create/character/",
        views.CharacterCreateView.as_view(),
        name="create_character",
    ),
    path(
        "characters/create/group/", views.GroupCreateView.as_view(), name="create_group"
    ),
    path(
        "characters/create/human/", views.HumanCreateView.as_view(), name="create_human"
    ),
    path("characters/create/mage/", views.MageCreateView.as_view(), name="create_mage"),
    path("characters/create/pack/", views.PackCreateView.as_view(), name="create_pack"),
    path(
        "characters/create/werewolf/",
        views.WerewolfCreateView.as_view(),
        name="create_werewolf",
    ),
    path(
        "ajax/load-character-types/",
        views.load_character_types,
        name="ajax_load_character_types",
    ),
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
    path("groups/<pk>/", views.GenericGroupDetailView.as_view(), name="group"),
]
