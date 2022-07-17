from django.urls import path

from tc import views

# Create your URLs here
urlpatterns = [
    path(
        "characters/create/human/", views.HumanCreateView.as_view(), name="create_human"
    ),
    path(
        "characters/create/talent/",
        views.TalentCreateView.as_view(),
        name="create_talent",
    ),
    path(
        "characters/create/aberrant/",
        views.AberrantCreateView.as_view(),
        name="create_aberrant",
    ),
    path("characters/", views.IndexView.as_view(), name="characters_index"),
    path(
        "characters/random/",
        views.RandomCharacterView.as_view(),
        name="random_character",
    ),
    path("characters/<pk>/", views.CharacterDetailView.as_view(), name="character"),
    path("edges/<pk>/", views.EdgeDetailView.as_view(), name="edge"),
    path(
        "enhancededges/<pk>/",
        views.EnhancedEdgeDetailView.as_view(),
        name="enhancededge",
    ),
    path("gifts/<pk>/", views.GiftDetailView.as_view(), name="gift"),
    path("megaedges/<pk>/", views.MegaEdgeDetailView.as_view(), name="megaedge"),
    path(
        "momentofinspirations/<pk>/",
        views.MomentOfInspiration.as_view(),
        name="momentofinspiration",
    ),
    path("paths/<pk>/", views.PathDetailView.as_view(), name="path"),
    path(
        "pathconnections/<pk>/",
        views.PathConnectionDetailView.as_view(),
        name="pathconnection",
    ),
    path("powers/<pk>/", views.PowerDetailView.as_view(), name="power"),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
    path("tags/<pk>/", views.TagDetailView.as_view(), name="tag"),
    path(
        "transformations/<pk>/",
        views.TransformationDetailView.as_view(),
        name="transformation",
    ),
    path("tricks/<pk>/", views.TrickDetailView.as_view(), name="trick"),
]
