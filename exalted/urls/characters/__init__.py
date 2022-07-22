from django.urls import include, path

from exalted import views

from . import mortal

urls = [
    path("", include((mortal.urls, "exalted"), namespace="mortal")),
    path("", views.IndexView.as_view(), name="index"),
    path("random/", views.RandomCharacterView.as_view(), name="random",),
    path("<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
