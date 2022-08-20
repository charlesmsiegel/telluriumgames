from django.urls import include, path

from exalted import views

urls = [
    path(
        "solar/create/",
        views.characters.solars.SolarCharmCreateView.as_view(),
        name="create_solar",
    ),
    path(
        "solar/update/<pk>/",
        views.characters.solars.SolarUpdateView.as_view(),
        name="update_solar",
    ),
    path(
        "solarcharm/create/",
        views.characters.solars.SolarCharmCreateView.as_view(),
        name="create_solarcharm",
    ),
    path(
        "solarcharm/update/<pk>/",
        views.characters.solars.SolarCharmUpdateView.as_view(),
        name="update_solarcharm",
    ),
    path(
        "solarcharm/<pk>/",
        views.characters.solars.SolarCharmDetailView.as_view(),
        name="solarcharm",
    ),
]
