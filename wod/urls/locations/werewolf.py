from django.urls import include, path

from wod import views

urls = [
    path(
        "caern/create/",
        views.locations.werewolf.CaernCreateView.as_view(),
        name="create_caern",
    ),
    path(
        "caern/update/<pk>/",
        views.locations.werewolf.CaernUpdateView.as_view(),
        name="update_caern",
    ),
]
