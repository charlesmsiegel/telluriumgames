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



    path(
        "weapon/create/", views.items.human.WeaponCreateView.as_view(), name="create_weapon"
    ),
    path(
        "weapon/update/<pk>/",
        views.items.human.WeaponUpdateView.as_view(),
        name="update_weapon",
    ),
    path(
        "meleeweapon/create/", views.items.human.MeleeWeaponCreateView.as_view(), name="create_meleeweapon"
    ),
    path(
        "meleeweapon/update/<pk>/",
        views.items.human.MeleeWeaponUpdateView.as_view(),
        name="update_meleeweapon",
    ),
    path(
        "rangedweapon/create/", views.items.human.RangedWeaponCreateView.as_view(), name="create_rangedweapon"
    ),
    path(
        "rangedweapon/update/<pk>/",
        views.items.human.RangedWeaponUpdateView.as_view(),
        name="update_rangedweapon",
    ),
    path(
        "thrownweapon/create/", views.items.human.ThrownWeaponCreateView.as_view(), name="create_thrownweapon"
    ),
    path(
        "thrownweapon/update/<pk>/",
        views.items.human.ThrownWeaponUpdateView.as_view(),
        name="update_thrownweapon",
    ),
]
