from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("", include((mage.urls, "wod"), namespace="mage")),
    path("", include((werewolf.urls, "wod"), namespace="werewolf")),
    path("", include((human.urls, "wod"), namespace="human")),
    path("", views.locations.LocationIndexView.as_view(), name="index"),
    path("random/", views.locations.RandomLocationView.as_view(), name="random"),
    path("<pk>/", views.locations.GenericLocationDetailView.as_view(), name="location"),
    path(
        "ajax/load-location-types/",
        views.locations.load_location_types,
        name="ajax_load_location_types",
    ),
]
