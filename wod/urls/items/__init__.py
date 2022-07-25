from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("", include((mage.urls, "wod"), namespace="mage")),
    path("", include((werewolf.urls, "wod"), namespace="werewolf")),
    path("", include((human.urls, "wod"), namespace="human")),
    path("", views.items.ItemIndexView.as_view(), name="index"),
    path("random/", views.items.RandomItemView.as_view(), name="random"),
    path("<pk>/", views.items.GenericItemDetailView.as_view(), name="item"),
    path(
        "ajax/load-item-types/",
        views.items.load_item_types,
        name="ajax_load_item_types",
    ),
]
