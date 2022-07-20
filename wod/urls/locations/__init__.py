from django.urls import include, path

from wod import views

urls = [
    path(
        "create/location/", views.LocationCreateView.as_view(), name="create_location",
    ),
    path("create/sector/", views.SectorCreateView.as_view(), name="create_sector"),
    path("create/city/", views.CityCreateView.as_view(), name="create_city"),
    path("create/node/", views.NodeCreateView.as_view(), name="create_node"),
    path("create/chantry/", views.ChantryCreateView.as_view(), name="create_chantry"),
    path("", views.LocationIndexView.as_view(), name="index"),
    path("random/", views.RandomLocationView.as_view(), name="random"),
    path("<pk>/", views.GenericLocationDetailView.as_view(), name="location"),
]
