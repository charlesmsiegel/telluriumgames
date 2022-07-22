from django.urls import include, path

from cod import views

from . import mage, mortal

urls = [
    path("", include((mortal.urls, "cod"), namespace="mortal")),
    path("", include((mage.urls, "cod"), namespace="mage")),
    path("", views.CharacterIndexView.as_view(), name="index"),
    path("random/", views.RandomCharacterView.as_view(), name="random",),
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
