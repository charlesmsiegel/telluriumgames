from django.urls import path

from cod import views

# Create your URLs here
urls = [
    path("create/mortal/", views.MortalCreateView.as_view(), name="create_mortal",),
    path("conditions/<pk>/", views.ConditionDetailView.as_view(), name="condition"),
    path("merits/<pk>/", views.MeritDetailView.as_view(), name="merit"),
    path("specialties/<pk>/", views.SpecialtyDetailView.as_view(), name="specialty"),
]
