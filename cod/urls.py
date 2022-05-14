from django.urls import path

from cod import views

# Create your URLs here
urlpatterns = [
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
]
