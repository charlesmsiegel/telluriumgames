from django.urls import include, path

from exalted import views

from . import dragonblooded, mortal, solars

urls = [
    path("", include((mortal.urls, "exalted"), namespace="mortal")),
    path("", include((solars.urls, "exalted"), namespace="solars")),
    path("", include((dragonblooded.urls, "dragonblooded"), namespace="dragonblooded")),
    path("", views.characters.IndexView.as_view(), name="index"),
    path("random/", views.characters.RandomCharacterView.as_view(), name="random",),
    path(
        "<pk>/", views.characters.GenericCharacterDetailView.as_view(), name="character"
    ),
]
