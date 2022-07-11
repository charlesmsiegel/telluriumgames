from django.urls import path

from cod import views

# Create your URLs here
urlpatterns = [
    path(
        "characters/create/mortal/",
        views.MortalCreateView.as_view(),
        name="create_mortal",
    ),
    path("characters/create/mage/", views.MageCreateView.as_view(), name="create_mage"),
    path(
        "characters/create/proximi/",
        views.ProximiCreateView.as_view(),
        name="create_proximi",
    ),
    path(
        "characters/create/proximifamily/",
        views.ProximiFamilyCreateView.as_view(),
        name="create_proximifamily",
    ),
    path(
        "proximifamily/<pk>/",
        views.ProximiFamilyDetailView.as_view(),
        name="proximifamily",
    ),
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path(
        "characters/random/",
        views.RandomCharacterView.as_view(),
        name="random_character",
    ),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
