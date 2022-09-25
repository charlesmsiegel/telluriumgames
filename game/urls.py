from django.urls import path

from game import views

# Create your URLs here
urlpatterns = [
    path("chronicle/<pk>", views.ChronicleDetailView.as_view(), name="chronicle"),
]
