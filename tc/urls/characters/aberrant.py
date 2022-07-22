from django.urls import include, path

from tc import views

urls = [
    path(
        "create/aberrant/", views.AberrantCreateView.as_view(), name="create_aberrant",
    ),
    path("megaedges/<pk>/", views.MegaEdgeDetailView.as_view(), name="megaedge"),
    path("powers/<pk>/", views.PowerDetailView.as_view(), name="power"),
    path("tags/<pk>/", views.TagDetailView.as_view(), name="tag"),
    path(
        "transformations/<pk>/",
        views.TransformationDetailView.as_view(),
        name="transformation",
    ),
]
