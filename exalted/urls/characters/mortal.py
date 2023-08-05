from django.urls import include, path

from exalted import views

urls = [
    path(
        "mortal/create/",
        views.characters.mortal.MortalCreateView.as_view(),
        name="create_mortal",
    ),
    path(
        "mortal/update/<pk>/",
        views.characters.mortal.MortalUpdateView.as_view(),
        name="update_mortal",
    ),
    path(
        "specialties/create/",
        views.characters.mortal.SpecialtyCreateView.as_view(),
        name="create_specialty",
    ),
    path(
        "specialties/update/<pk>/",
        views.characters.mortal.SpecialtyUpdateView.as_view(),
        name="update_specialty",
    ),
    path(
        "specialties/<pk>/",
        views.characters.mortal.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
    path(
        "intimacies/create/",
        views.characters.mortal.IntimacyCreateView.as_view(),
        name="create_intimacy",
    ),
    path(
        "intimacies/update/<pk>/",
        views.characters.mortal.IntimacyUpdateView.as_view(),
        name="update_intimacy",
    ),
    path(
        "intimacies/<pk>/",
        views.characters.mortal.IntimacyDetailView.as_view(),
        name="intimacy",
    ),
    path(
        "merits/create/",
        views.characters.mortal.MeritCreateView.as_view(),
        name="create_merit",
    ),
    path(
        "merits/update/<pk>/",
        views.characters.mortal.MeritUpdateView.as_view(),
        name="update_merit",
    ),
    path(
        "merits/<pk>/", views.characters.mortal.MeritDetailView.as_view(), name="merit"
    ),
]
