from django.urls import path

from wod import views

# Create your URLs here
urlpatterns = [
    path("ajax/load_faction_details/", views.load_factions, name="ajax_load_factions"),
    path(
        "ajax/load_subfaction_details/",
        views.load_subfactions,
        name="ajax_load_subfactions",
    ),
    path(
        "locations/create/location/",
        views.LocationCreateView.as_view(),
        name="create_location",
    ),
    path("locations/create/sector/", views.SectorCreateView.as_view(), name="create_sector"),
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
