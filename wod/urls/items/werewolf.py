from django.urls import include, path

from wod import views

urls = [
    path(
        "fetish/create/",
        views.items.werewolf.FetishCreateView.as_view(),
        name="create_fetish",
    ),
    path(
        "fetish/update/<pk>/",
        views.items.werewolf.FetishUpdateView.as_view(),
        name="update_fetish",
    ),
]
