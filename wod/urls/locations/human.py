from django.urls import include, path

from wod import views

urls = [
    path(
        "location/create/",
        views.locations.human.LocationCreateView.as_view(),
        name="create_location",
    ),
    path(
        "location/update/<pk>/",
        views.locations.human.LocationUpdateView.as_view(),
        name="update_location",
    ),
    path(
        "city/create/",
        views.locations.human.CityCreateView.as_view(),
        name="create_city",
    ),
    path(
        "city/update/<pk>/",
        views.locations.human.CityUpdateView.as_view(),
        name="update_city",
    ),
]
