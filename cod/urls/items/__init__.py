from django.urls import include, path

from cod import views

from . import mortal

urls = [
    path("", include((mortal.urls, "cod"), namespace="mortal")),
    path("", views.ItemIndexView.as_view(), name="index"),
    path("<pk>/", views.GenericItemDetailView.as_view(), name="item"),
]
