from django.urls import include, path

from wod import views

urls = [
    path(
        "item/create/", views.items.human.ItemCreateView.as_view(), name="create_item"
    ),
    path(
        "item/update/<pk>/",
        views.items.human.ItemUpdateView.as_view(),
        name="update_item",
    ),
]
