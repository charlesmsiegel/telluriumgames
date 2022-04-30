from django.urls import path

from cod import views

# Create your URLs here
urlpatterns = [
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
