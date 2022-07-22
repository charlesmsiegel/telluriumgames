from django.urls import include, path

from tc import views

urls = [
    path("create/talent/", views.TalentCreateView.as_view(), name="create_talent",),
    path("gifts/<pk>/", views.GiftDetailView.as_view(), name="gift"),
    path(
        "momentofinspirations/<pk>/",
        views.MomentOfInspirationDetailView.as_view(),
        name="momentofinspiration",
    ),
]
