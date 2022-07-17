from django.urls import path

from core import views

# Create your URLs here
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("language/<pk>/", views.LanguageDetailView.as_view(), name="language"),
    path("material/<pk>/", views.MaterialDetailView.as_view(), name="material"),
    path("medium/<pk>/", views.MediumDetailView.as_view(), name="medium"),
    
    ]
