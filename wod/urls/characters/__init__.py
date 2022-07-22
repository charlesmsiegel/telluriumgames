from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("", include((mage.urls, "wod"), namespace="mage")),
    path("", include((werewolf.urls, "wod"), namespace="werewolf")),
    path("", include((human.urls, "wod"), namespace="human")),
    path("", views.CharacterIndexView.as_view(), name="index"),
    path("random/", views.RandomCharacterView.as_view(), name="random",),
    path("groups/<pk>/", views.GenericGroupDetailView.as_view(), name="group"),
    path("<pk>/", views.GenericCharacterDetailView.as_view(), name="character"),
]
