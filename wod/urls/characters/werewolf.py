from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path("create/pack/", views.PackCreateView.as_view(), name="create_pack"),
    path(
        "create/werewolf/", views.WerewolfCreateView.as_view(), name="create_werewolf",
    ),
    path("camps/<pk>/", views.CampDetailView.as_view(), name="camp"),
    path("charms/<pk>/", views.CharmDetailView.as_view(), name="charm"),
    path("gifts/<pk>/", views.GiftDetailView.as_view(), name="gift"),
    path(
        "renownincidents/<pk>/",
        views.RenownIncidentDetailView.as_view(),
        name="renownincident",
    ),
    path("rites/<pk>/", views.RiteDetailView.as_view(), name="rite"),
    path("totems/<pk>/", views.TotemDetailView.as_view(), name="totem"),
    path("tribes/<pk>/", views.TribeDetailView.as_view(), name="tribe"),
]
