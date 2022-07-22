from django.urls import include, path

from wod import views

urls = [
    path(
        "create/location/", views.LocationCreateView.as_view(), name="create_location",
    ),
    path("create/city/", views.CityCreateView.as_view(), name="create_city"),
]
