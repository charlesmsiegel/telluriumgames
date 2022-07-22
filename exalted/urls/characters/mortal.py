from django.urls import include, path

from exalted import views

urls = [
    path("create/mortal/", views.MortalCreateView.as_view(), name="create_mortal",),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
    path("intimacies/<pk>/", views.IntimacyDetailView.as_view(), name="intimacy"),
    path("merits/<pk>/", views.MeritDetailView.as_view(), name="merit"),
]
