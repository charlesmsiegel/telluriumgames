from django.urls import include, path

from exalted import views

from . import mortals

urls = [
    path("", include((mortals.urls, "exalted"), namespace="mortals")),
    path("", views.locations.LocationIndexView.as_view(), name="index"),
    path("<pk>/", views.locations.GenericLocationDetailView.as_view(), name="location"),
]
