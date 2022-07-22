from django.urls import include, path

from tc import views

urls = [
    path("create/human/", views.HumanCreateView.as_view(), name="create_human"),
    path("edges/<pk>/", views.EdgeDetailView.as_view(), name="edge"),
    path(
        "enhancededges/<pk>/",
        views.EnhancedEdgeDetailView.as_view(),
        name="enhancededge",
    ),
    path("paths/<pk>/", views.PathDetailView.as_view(), name="path"),
    path(
        "pathconnections/<pk>/",
        views.PathConnectionDetailView.as_view(),
        name="pathconnection",
    ),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
    path("tricks/<pk>/", views.TrickDetailView.as_view(), name="trick"),
]
