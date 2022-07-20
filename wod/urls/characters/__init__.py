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
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
