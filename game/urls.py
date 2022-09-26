from django.urls import path

from game import views

# Create your URLs here
urlpatterns = [
    path("chronicle/<pk>", views.ChronicleDetailView.as_view(), name="chronicle"),
    path("story/<pk>", views.StoryDetailView.as_view(), name="story"),
    path("scene/<pk>", views.SceneDetailView.as_view(), name="scene"),
]
