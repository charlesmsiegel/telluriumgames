from django.urls import path

from cod import views

urls = [
    path("create/mage/", views.MageCreateView.as_view(), name="create_mage"),
    path("create/proximi/", views.ProximiCreateView.as_view(), name="create_proximi",),
    path(
        "create/proximifamily/",
        views.ProximiFamilyCreateView.as_view(),
        name="create_proximifamily",
    ),
    path(
        "proximifamily/<pk>/",
        views.ProximiFamilyDetailView.as_view(),
        name="proximifamily",
    ),
    path("legacies/<pk>/", views.LegacyDetailView.as_view(), name="legacy"),
    path("orders/<pk>/", views.OrderDetailView.as_view(), name="order"),
    path("paths/<pk>/", views.PathDetailView.as_view(), name="path"),
    path("rotes/<pk>/", views.RoteDetailView.as_view(), name="rote"),
]
