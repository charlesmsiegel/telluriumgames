from django.urls import include, path

from tc import views

urls = [
    path("aberrant/create/", views.characters.aberrant.AberrantCreateView.as_view(), name="create_aberrant"),
    path("aberrant/update/", views.characters.aberrant.AberrantUpdateView.as_view(), name="update_aberrant"),
    path("megaedges/create/", views.characters.aberrant.MegaEdgeCreateView.as_view(), name="create_megaedge"),
    path("megaedges/update/<pk>/", views.characters.aberrant.MegaEdgeUpdateView.as_view(), name="update_megaedge"),
    path("megaedges/<pk>/", views.characters.aberrant.MegaEdgeDetailView.as_view(), name="megaedge"),
    path("powers/create/", views.characters.aberrant.PowerCreateView.as_view(), name="create_power"),
    path("powers/update/<pk>/", views.characters.aberrant.PowerUpdateView.as_view(), name="update_power"),
    path("powers/<pk>/", views.characters.aberrant.PowerDetailView.as_view(), name="power"),
    path("tags/create/", views.characters.aberrant.TagCreateView.as_view(), name="create_tag"),
    path("tags/update/<pk>/", views.characters.aberrant.TagUpdateView.as_view(), name="update_tag"),
    path("tags/<pk>/", views.characters.aberrant.TagDetailView.as_view(), name="tag"),
    path("transformations/create/", views.characters.aberrant.TransformationCreateView.as_view(), name="create_transformations"),
    path("transformations/update/<pk>/", views.characters.aberrant.TransformationUpdateView.as_view(), name="update_transformations"),
    path("transformations/<pk>/", views.characters.aberrant.TransformationDetailView.as_view(), name="transformation"),
]
