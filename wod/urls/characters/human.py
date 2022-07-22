from django.urls import include, path

from wod import views

from . import human, mage, werewolf

urls = [
    path(
        "create/character/",
        views.CharacterCreateView.as_view(),
        name="create_character",
    ),
    path("create/group/", views.GroupCreateView.as_view(), name="create_group"),
    path("create/human/", views.HumanCreateView.as_view(), name="create_human"),
    path("archetypes/<pk>/", views.ArchetypeDetailView.as_view(), name="archetype"),
    path("meritflaws/<pk>/", views.MeritFlawDetailView.as_view(), name="meritflaw"),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
]
