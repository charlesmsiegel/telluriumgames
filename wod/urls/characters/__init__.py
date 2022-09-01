from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("", include((mage.urls, "wod"), namespace="mage")),
    path("", include((werewolf.urls, "wod"), namespace="werewolf")),
    path("", include((human.urls, "wod"), namespace="human")),
    path("", views.characters.CharacterIndexView.as_view(), name="index"),
    path(
        "random/",
        views.characters.RandomCharacterView.as_view(),
        name="random",
    ),
    path(
        "groups/<pk>/", views.characters.GenericGroupDetailView.as_view(), name="group"
    ),
    path(
        "<pk>/", views.characters.GenericCharacterDetailView.as_view(), name="character"
    ),
    path(
        "ajax/load-character-types/",
        views.characters.load_character_types,
        name="ajax_load_character_types",
    ),
]
