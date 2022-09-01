from django.urls import include, path

from tc import views

from . import aberrant, human, talent

urls = [
    path("", include((aberrant.urls, "tc"), namespace="aberrant")),
    path("", include((talent.urls, "tc"), namespace="talent")),
    path("", include((human.urls, "tc"), namespace="human")),
    path("", views.characters.IndexView.as_view(), name="index"),
    path(
        "random/",
        views.characters.RandomCharacterView.as_view(),
        name="random",
    ),
    path("<pk>/", views.characters.CharacterDetailView.as_view(), name="character"),
    path(
        "ajax/load-character-types/",
        views.characters.load_character_types,
        name="ajax_load_character_types",
    ),
]
