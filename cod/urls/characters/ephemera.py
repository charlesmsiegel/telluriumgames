from django.urls import path

from cod import views

urls = [
    path(
        "ephemera/create/",
        views.characters.ephemera.EphemeraCreateView.as_view(),
        name="create_ephemera",
    ),
    path(
        "ephemera/update/<pk>/",
        views.characters.ephemera.EphemeraUpdateView.as_view(),
        name="update_ephemera",
    ),
    path(
        "ephemera/<pk>/",
        views.characters.ephemera.EphemeraDetailView.as_view(),
        name="ephemera",
    ),
    path(
        "numina/create/",
        views.characters.ephemera.NuminaCreateView.as_view(),
        name="create_numina",
    ),
    path(
        "numina/update/<pk>/",
        views.characters.ephemera.NuminaUpdateView.as_view(),
        name="update_numina",
    ),
    path(
        "numina/<pk>/",
        views.characters.ephemera.NuminaDetailView.as_view(),
        name="numina",
    ),
]
