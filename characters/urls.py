from django.urls import path

from characters import views

# Create your URLs here
urlpatterns = [
    path("", views.IndexView.as_view(), name="characters_index"),
    path("<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
