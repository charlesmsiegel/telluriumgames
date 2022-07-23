from django.urls import include, path

from tc import views

urls = [
    path(
        "talent/create/",
        views.characters.talent.TalentCreateView.as_view(),
        name="create_talent",
    ),
    path(
        "talent/update/<pk>/",
        views.characters.talent.TalentCreateView.as_view(),
        name="update_talent",
    ),
    path(
        "gifts/create/",
        views.characters.talent.GiftCreateView.as_view(),
        name="create_gift",
    ),
    path(
        "gifts/update/<pk>/",
        views.characters.talent.GiftUpdateView.as_view(),
        name="update_gift",
    ),
    path("gifts/<pk>/", views.characters.talent.GiftDetailView.as_view(), name="gift"),
    path(
        "momentofinspirations/create/",
        views.characters.talent.MomentOfInspirationCreateView.as_view(),
        name="create_momentofinspiration",
    ),
    path(
        "momentofinspirations/update/<pk>/",
        views.characters.talent.MomentOfInspirationUpdateView.as_view(),
        name="update_momentofinspiration",
    ),
    path(
        "momentofinspirations/<pk>/",
        views.characters.talent.MomentOfInspirationDetailView.as_view(),
        name="momentofinspiration",
    ),
]
