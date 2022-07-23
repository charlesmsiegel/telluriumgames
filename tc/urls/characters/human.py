from django.urls import include, path

from tc import views

urls = [
    path("human/create/", views.characters.human.HumanCreateView.as_view(), name="create_human"),
    path("human/update/<pk>/", views.characters.human.HumanUpdateView.as_view(), name="update_human"),
    path("edges/create/", views.characters.human.EdgeCreateView.as_view(), name="create_edge"),
    path("edges/update/<pk>/", views.characters.human.EdgeUpdateView.as_view(), name="update_edge"),
    path("edges/<pk>/", views.characters.human.EdgeDetailView.as_view(), name="edge"),
    path("enhancededges/create/", views.characters.human.EnhancedEdgeCreateView.as_view(), name="create_enhancededge"),
    path("enhancededges/update/<pk>/", views.characters.human.EnhancedEdgeUpdateView.as_view(), name="update_enhancededge"),
    path("enhancededges/<pk>/", views.characters.human.EnhancedEdgeDetailView.as_view(), name="enhancededge"),
    path("paths/create/", views.characters.human.PathConnectionCreateView.as_view(), name="create_path"),
    path("paths/update/<pk>/", views.characters.human.PathConnectionUpdateView.as_view(), name="update_path"),
    path("paths/<pk>/", views.characters.human.PathDetailView.as_view(), name="path"),
    path("pathconnections/create/", views.characters.human.PathConnectionCreateView.as_view(), name="create_pathconnection"),
    path("pathconnections/update/<pk>/", views.characters.human.PathConnectionUpdateView.as_view(), name="update_pathconnection"),
    path("pathconnections/<pk>/", views.characters.human.PathConnectionDetailView.as_view(), name="pathconnection"),
    path("specialties/create/", views.characters.human.SpecialtyCreateView.as_view(), name="create_specialty"),
    path("specialties/update/<pk>/", views.characters.human.SpecialtyUpdateView.as_view(), name="update_specialty"),
    path("specialties/<pk>/", views.characters.human.SpecialtyDetailView.as_view(), name="specialty"),
    path("tricks/create/", views.characters.human.TrickCreateView.as_view(), name="create_trick"),
    path("tricks/update/<pk>/", views.characters.human.TrickUpdateView.as_view(), name="update_trick"),
    path("tricks/<pk>/", views.characters.human.TrickDetailView.as_view(), name="trick"),
]
