from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("", include((mage.urls, "wod"), namespace="mage")),
    path("", include((werewolf.urls, "wod"), namespace="werewolf")),
    path("", include((human.urls, "wod"), namespace="human")),
    path("", views.LocationIndexView.as_view(), name="index"),
    path("random/", views.RandomLocationView.as_view(), name="random"),
    path("<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
]
