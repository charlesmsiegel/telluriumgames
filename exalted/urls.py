from django.urls import path

from exalted import views

# Create your URLs here
urlpatterns = [
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path(
        "characters/random/",
        views.RandomCharacterView.as_view(),
        name="random_character",
    ),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
