from django.urls import include, path

from wod import views

urls = [
    path(
        "sector/create/",
        views.locations.mage.SectorCreateView.as_view(),
        name="create_sector",
    ),
    path(
        "sector/update/<pk>/",
        views.locations.mage.SectorUpdateView.as_view(),
        name="update_sector",
    ),
    path(
        "node/create/",
        views.locations.mage.NodeCreateView.as_view(),
        name="create_node",
    ),
    path(
        "node/update/<pk>/",
        views.locations.mage.NodeUpdateView.as_view(),
        name="update_node",
    ),
    path(
        "chantry/create/",
        views.locations.mage.ChantryCreateView.as_view(),
        name="create_chantry",
    ),
    path(
        "chantry/update/<pk>/",
        views.locations.mage.ChantryUpdateView.as_view(),
        name="update_chantry",
    ),
    path(
        "nodemeritflaw/<pk>/",
        views.locations.mage.NodeMeritFlawDetailView.as_view(),
        name="nodemeritflaw",
    ),
    path(
        "nodemeritflaw/create/",
        views.locations.mage.NodeMeritFlawCreateView.as_view(),
        name="create_nodemeritflaw",
    ),
    path(
        "nodemeritflaw/update/<pk>/",
        views.locations.mage.NodeMeritFlawUpdateView.as_view(),
        name="update_nodemeritflaw",
    ),
]
