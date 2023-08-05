from django.urls import include, path

from exalted import views

urls = [
    path(
        "location/create/",
        views.locations.mortals.ExLocationCreateView.as_view(),
        name="create_location",
    ),
    path(
        "location/update/<pk>/",
        views.locations.mortals.ExLocationUpdateView.as_view(),
        name="update_location",
    ),
]
