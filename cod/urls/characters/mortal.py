from django.urls import path

from cod import views

# Create your URLs here
urls = [
    path(
        "mortal/create/",
        views.characters.mortal.MortalCreateView.as_view(),
        name="create_mortal",
    ),
    path(
        "mortal/update/<pk>/",
        views.characters.mortal.MortalUpdateView.as_view(),
        name="create_mortal",
    ),
    path(
        "conditions/create/",
        views.characters.mortal.ConditionCreateView.as_view(),
        name="create_item",
    ),
    path(
        "conditions/update/<pk>/",
        views.characters.mortal.ConditionUpdateView.as_view(),
        name="update_item",
    ),
    path(
        "conditions/<pk>/",
        views.characters.mortal.ConditionDetailView.as_view(),
        name="condition",
    ),
    path(
        "merits/create/",
        views.characters.mortal.MeritCreateView.as_view(),
        name="create_item",
    ),
    path(
        "merits/update/<pk>/",
        views.characters.mortal.MeritUpdateView.as_view(),
        name="update_item",
    ),
    path(
        "merits/<pk>/", views.characters.mortal.MeritDetailView.as_view(), name="merit"
    ),
    path(
        "specialties/create/",
        views.characters.mortal.SpecialtyCreateView.as_view(),
        name="create_item",
    ),
    path(
        "specialties/update/<pk>/",
        views.characters.mortal.SpecialtyUpdateView.as_view(),
        name="update_item",
    ),
    path(
        "specialties/<pk>/",
        views.characters.mortal.SpecialtyDetailView.as_view(),
        name="specialty",
    ),
]
