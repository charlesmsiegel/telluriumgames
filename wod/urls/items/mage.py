from django.urls import include, path

from wod import views

urls = [
    path(
        "grimoire/create/",
        views.items.mage.GrimoireCreateView.as_view(),
        name="create_grimoire",
    ),
    path(
        "grimoire/update/<pk>/",
        views.items.mage.GrimoireUpdateView.as_view(),
        name="update_grimoire",
    ),
    path(
        "wonder/create/",
        views.items.mage.WonderCreateView.as_view(),
        name="create_wonder",
    ),
    path(
        "wonder/update/<pk>/",
        views.items.mage.WonderUpdateView.as_view(),
        name="update_wonder",
    ),
    path(
        "library/create/",
        views.items.mage.LibraryCreateView.as_view(),
        name="create_library",
    ),
    path(
        "library/update/<pk>/",
        views.items.mage.LibraryUpdateView.as_view(),
        name="update_library",
    ),
]
