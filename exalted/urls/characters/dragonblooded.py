from django.urls import include, path

from exalted import views

urls = [
    path(
        "dragonblooded/create/",
        views.characters.dragonblooded.DragonBloodedCreateView.as_view(),
        name="create_dragonblooded",
    ),
    path(
        "dragonblooded/update/<pk>/",
        views.characters.dragonblooded.DragonBloodedUpdateView.as_view(),
        name="update_dragonblooded",
    ),
    path(
        "dragonbloodedcharm/create/",
        views.characters.dragonblooded.DragonBloodedCharmCreateView.as_view(),
        name="create_dragonbloodedcharm",
    ),
    path(
        "dragonbloodedcharm/update/<pk>/",
        views.characters.dragonblooded.DragonBloodedCharmUpdateView.as_view(),
        name="update_dragonbloodedcharm",
    ),
    path(
        "dragonbloodedcharm/<pk>/",
        views.characters.dragonblooded.DragonBloodedCharmDetailView.as_view(),
        name="dragonbloodedcharm",
    ),
]
