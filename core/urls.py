from django.urls import path

from core import views

# Create your URLs here
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("language/<pk>/", views.LanguageDetailView.as_view(), name="language"),
    path(
        "language/create/", views.LanguageCreateView.as_view(), name="create_language",
    ),
    path(
        "language/update/<pk>/",
        views.LanguageUpdateView.as_view(),
        name="update_language",
    ),
    path("material/<pk>/", views.MaterialDetailView.as_view(), name="material"),
    path(
        "material/create/", views.MaterialCreateView.as_view(), name="create_material",
    ),
    path(
        "material/update/<pk>/",
        views.MaterialUpdateView.as_view(),
        name="update_material",
    ),
    path("medium/<pk>/", views.MediumDetailView.as_view(), name="medium"),
    path("medium/create/", views.MediumCreateView.as_view(), name="create_medium",),
    path(
        "medium/update/<pk>/", views.MediumUpdateView.as_view(), name="update_medium",
    ),
]
