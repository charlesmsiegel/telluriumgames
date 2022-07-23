from django.urls import include, path

from cod import views

from . import mage, mortal

urls = [
    path("", include((mortal.urls, "cod"), namespace="mortal")),
    path("", include((mage.urls, "cod"), namespace="mage")),
    path("", views.characters.CharacterIndexView.as_view(), name="index"),
    path("random/", views.characters.RandomCharacterView.as_view(), name="random",),
    path("<pk>/", views.characters.GenericCharacterDetailView.as_view(), name="character"),
]
