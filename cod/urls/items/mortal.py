from django.urls import path

from cod import views

urls = [
    path(
        "item/create/", views.items.mortal.ItemCreateView.as_view(), name="create_item"
    ),
    path(
        "item/update/<pk>/",
        views.items.mortal.ItemUpdateView.as_view(),
        name="update_item",
    ),
    path(
        "equipment/create/",
        views.items.mortal.EquipmentCreateView.as_view(),
        name="create_equipment",
    ),
    path(
        "equipment/update/<pk>/",
        views.items.mortal.EquipmentUpdateView.as_view(),
        name="update_equipment",
    ),
]
