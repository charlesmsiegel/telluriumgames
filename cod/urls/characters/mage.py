from django.urls import path

from cod import views

urls = [
    path("mage/create/", views.characters.mage.MageCreateView.as_view(), name="create_mage"),
    path("mage/update/<pk>/", views.characters.mage.MageUpdateView.as_view(), name="update_mage"),
    path("proximi/create/", views.characters.mage.ProximiCreateView.as_view(), name="create_proximi",),
    path("proximi/update/<pk>/", views.characters.mage.ProximiUpdateView.as_view(), name="update_proximi"),
    path("proximifamily/create/", views.characters.mage.ProximiFamilyCreateView.as_view(), name="create_proximifamily"),
    path("proximifamily/update/<pk>/", views.characters.mage.ProximiFamilyUpdateView.as_view(), name="update_proximifamily"),
    path("proximifamily/<pk>/", views.characters.mage.ProximiFamilyDetailView.as_view(), name="proximifamily"),
    path("legacies/create/", views.characters.mage.LegacyCreateView.as_view(), name="create_legacy"),
    path("legacies/update/<pk>/", views.characters.mage.LegacyUpdateView.as_view(), name="update_legacy"),
    path("legacies/<pk>/", views.characters.mage.LegacyDetailView.as_view(), name="legacy"),
    path("orders/create/", views.characters.mage.OrderCreateView.as_view(), name="create_order"),
    path("orders/update/<pk>/", views.characters.mage.OrderUpdateView.as_view(), name="update_order"),
    path("orders/<pk>/", views.characters.mage.OrderDetailView.as_view(), name="order"),
    path("paths/create/", views.characters.mage.PathCreateView.as_view(), name="create_path"),
    path("paths/update/<pk>/", views.characters.mage.PathUpdateView.as_view(), name="update_path"),
    path("paths/<pk>/", views.characters.mage.PathDetailView.as_view(), name="path"),
    path("rotes/create/", views.characters.mage.RoteCreateView.as_view(), name="create_rote"),
    path("rotes/update/<pk>/", views.characters.mage.RoteUpdateView.as_view(), name="update_rote"),
    path("rotes/<pk>/", views.characters.mage.RoteDetailView.as_view(), name="rote"),
]
