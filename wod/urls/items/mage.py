from django.urls import include, path

from wod import views

urls = [
    path(
        "create/grimoire/", views.GrimoireCreateView.as_view(), name="create_grimoire",
    ),
    path("create/wonder/", views.WonderCreateView.as_view(), name="create_wonder"),
    path("create/library/", views.LibraryCreateView.as_view(), name="create_library",),
]
