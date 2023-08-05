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
        "charm/create/",
        views.items.mage.CharmCreateView.as_view(),
        name="create_charm",
    ),
    path(
        "charm/update/<pk>/",
        views.items.mage.CharmUpdateView.as_view(),
        name="update_charm",
    ),
    path(
        "artifact/create/",
        views.items.mage.ArtifactCreateView.as_view(),
        name="create_artifact",
    ),
    path(
        "artifact/update/<pk>/",
        views.items.mage.ArtifactUpdateView.as_view(),
        name="update_artifact",
    ),
    path(
        "talisman/create/",
        views.items.mage.TalismanCreateView.as_view(),
        name="create_talisman",
    ),
    path(
        "talisman/update/<pk>/",
        views.items.mage.TalismanUpdateView.as_view(),
        name="update_talisman",
    ),
]
