from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("create/sector/", views.SectorCreateView.as_view(), name="create_sector"),
    path("create/node/", views.NodeCreateView.as_view(), name="create_node"),
    path("create/chantry/", views.ChantryCreateView.as_view(), name="create_chantry"),
]
