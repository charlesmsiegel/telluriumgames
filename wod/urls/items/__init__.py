from django.urls import include, path

from wod import views

urls = [
    path(
        "create/grimoire/", views.GrimoireCreateView.as_view(), name="create_grimoire",
    ),
    path("create/item/", views.ItemCreateView.as_view(), name="create_item"),
    path("create/wonder/", views.WonderCreateView.as_view(), name="create_wonder"),
    path("create/library/", views.LibraryCreateView.as_view(), name="create_library",),
    path("", views.ItemIndexView.as_view(), name="index"),
    path("random/", views.RandomItemView.as_view(), name="random"),
    path("<pk>/", views.GenericItemDetailView.as_view(), name="item"),
]
