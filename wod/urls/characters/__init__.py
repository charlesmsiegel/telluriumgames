from django.urls import include, path

from wod import views

urls = [
    path("create/cabal/", views.CabalCreateView.as_view(), name="create_cabal"),
    path(
        "create/character/",
        views.CharacterCreateView.as_view(),
        name="create_character",
    ),
    path("create/group/", views.GroupCreateView.as_view(), name="create_group"),
    path("create/human/", views.HumanCreateView.as_view(), name="create_human"),
    path("create/mage/", views.MageCreateView.as_view(), name="create_mage"),
    path("create/pack/", views.PackCreateView.as_view(), name="create_pack"),
    path(
        "create/werewolf/", views.WerewolfCreateView.as_view(), name="create_werewolf",
    ),
    path("", views.CharacterIndexView.as_view(), name="index"),
    path("random/", views.RandomCharacterView.as_view(), name="random",),
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
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
