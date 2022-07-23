from django.urls import include, path

from cod import views

from . import mortal

urls = [
    path("", include((mortal.urls, "cod"), namespace="mortal")),
    path("", views.items.ItemIndexView.as_view(), name="index"),
    path("<pk>/", views.items.GenericItemDetailView.as_view(), name="item"),
]
