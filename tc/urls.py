from django.urls import path

from tc import views

# Create your URLs here
urlpatterns = [
    path(
        "characters/create/human/", views.HumanCreateView.as_view(), name="create_human"
    ),
    path(
        "characters/create/talent/",
        views.TalentCreateView.as_view(),
        name="create_talent",
    ),
    path(
        "characters/create/aberrant/",
        views.AberrantCreateView.as_view(),
        name="create_aberrant",
    ),
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path(
        "characters/random/",
        views.RandomCharacterView.as_view(),
        name="random_character",
    ),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
