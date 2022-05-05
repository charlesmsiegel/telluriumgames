from django.urls import path
from tc import views

# Create your URLs here
urlpatterns = [
    path("", views.IndexView.as_view(), name="characters_index"),
    path("edges/", views.EdgeListView.as_view(), name="edges_index"),
    path(
        "enhancededges/",
        views.EnhancedEdgeListView.as_view(),
        name="enhanced_edges_index",
    ),
    path("megaedges/", views.MegaEdgeListView.as_view(), name="mega_edges_index"),
    path("paths/", views.PathListView.as_view(), name="paths_index"),
    path("powers/", views.PowerListView.as_view(), name="powers_index"),
    path("tags/", views.TagListView.as_view(), name="tags_index"),
    path(
        "transformations/",
        views.TransformationListView.as_view(),
        name="transformations_index",
    ),
    path("tricks/", views.TrickListView.as_view(), name="tricks_index"),
    path("create/", views.AberrantCreateView.as_view(), name="create"),
    path("edge/<pk>/", views.EdgeDetailView.as_view(), name="edge"),
    path(
        "enhancededge/<pk>/",
        views.EnhancedEdgeDetailView.as_view(),
        name="enhancededge",
    ),
    path("megaedge/<pk>/", views.MegaEdgeDetailView.as_view(), name="megaedge"),
    path("path/<pk>/", views.PathDetailView.as_view(), name="path"),
    path("power/<pk>/", views.PowerDetailView.as_view(), name="power"),
    path("tag/<pk>/", views.TagDetailView.as_view(), name="tag"),
    path(
        "transformation/<pk>/",
        views.TransformationDetailView.as_view(),
        name="transformation",
    ),
    path("trick/<pk>/", views.TrickDetailView.as_view(), name="trick"),
    path("random/", views.RandomCreateView.as_view(), name="random"),
    path("characters/<pk>/", views.AberrantDetailView.as_view(), name="character"),
]
