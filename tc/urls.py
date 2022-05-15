from django.urls import path

from tc import views

# Create your URLs here
urlpatterns = [
    path("", views.IndexView.as_view(), name="characters_index"),
    path("characters/<pk>/", views.AberrantDetailView.as_view(), name="character"),
]
