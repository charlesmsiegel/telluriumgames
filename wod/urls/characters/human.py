from django.urls import include, path

from wod import views

urls = [
    path(
        "character/create/",
        views.characters.human.CharacterCreateView.as_view(),
        name="create_character",
    ),
    path(
        "character/update/<pk>/",
        views.characters.human.CharacterUpdateView.as_view(),
        name="update_character",
    ),
    path(
        "group/create/",
        views.characters.human.GroupCreateView.as_view(),
        name="create_group",
    ),
    path(
        "group/update/<pk>/",
        views.characters.human.GroupUpdateView.as_view(),
        name="update_group",
    ),
    path(
        "human/create/",
        views.characters.human.HumanCreateView.as_view(),
        name="create_human",
    ),
    path(
        "human/update/<pk>/",
        views.characters.human.HumanUpdateView.as_view(),
        name="update_human",
    ),
    path(
        "archetypes/<pk>/",
        views.characters.human.ArchetypeDetailView.as_view(),
        name="archetype",
    ),
    path(
        "archetypes/create/",
        views.characters.human.ArchetypeCreateView.as_view(),
        name="create_archetype",
    ),
    path(
        "archetypes/update/<pk>/",
        views.characters.human.ArchetypeUpdateView.as_view(),
        name="update_archetype",
    ),
    path(
        "meritflaws/<pk>/",
        views.characters.human.MeritFlawDetailView.as_view(),
        name="meritflaw",
    ),
    path(
        "meritflaws/create/",
        views.characters.human.MeritFlawCreateView.as_view(),
        name="create_meritflaw",
    ),
    path(
        "meritflaws/update/<pk>/",
        views.characters.human.MeritFlawUpdateView.as_view(),
        name="update_meritflaw",
    ),
    path(
        "specialties/<pk>/",
        views.characters.human.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
    path(
        "specialties/create/",
        views.characters.human.SpecialtyCreateView.as_view(),
        name="create_specialty",
    ),
    path(
        "specialties/update/<pk>/",
        views.characters.human.SpecialtyUpdateView.as_view(),
        name="update_specialty",
    ),
    path(
        "derangement/<pk>/",
        views.characters.human.DerangementDetailView.as_view(),
        name="derangement",
    ),
    path(
        "derangement/create/",
        views.characters.human.DerangementCreateView.as_view(),
        name="create_derangement",
    ),
    path(
        "derangement/update/<pk>/",
        views.characters.human.DerangementUpdateView.as_view(),
        name="update_derangement",
    ),
]
